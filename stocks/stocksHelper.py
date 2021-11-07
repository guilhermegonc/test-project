from django.db import connection
from stocks_background.recommendationHelper import get_recommendations
from .models import UserStocksTransactions,\
                    UserStocks,\
                    TransactionProfit,\
                    StockValues

import datetime
import sys

class EnrichedStock:
    def __init__(self, code, quantity, price, value, recommended, close_date):
        self.code = code
        self.quantity = quantity
        self.price = price
        self.value = value
        self.close_date = close_date,
        self.recommended = recommended 


def update_transactions(user, action, code, quantity, value, dt):
    transaction = UserStocksTransactions(action=action, user=user, 
    code=code, quantity=quantity, value=value, transaction_date=dt)    
    transaction.save()
    update_wallet(user, transaction)
    return transaction


def update_wallet(user, transaction):
    if not UserStocks.objects.filter(user=user, code=transaction.code).exists():
        create_user_stock(user, transaction.code)

    stock = UserStocks.objects.get(user=user, code=transaction.code)

    if transaction.action == 'buy':
        new_value = ((stock.quantity * stock.weighted_average_cost) + \
            (transaction.quantity * transaction.value)) / (stock.quantity + transaction.quantity)
        stock.weighted_average_cost = new_value
    
    if transaction.action == 'sell':
        profit = transaction.value - stock.weighted_average_cost
        register_profit(transaction, profit)
        transaction.quantity *= -1

    stock.quantity += transaction.quantity
    
    if stock.quantity < 0:
        raise ValueError('Insuficient Stocks')
    
    stock.save()
    return stock


def create_user_stock(user, code):
    stock = UserStocks(user=user, code=code,
                        quantity=0, weighted_average_cost=0) 
    stock.save()
    return stock


def register_profit(transaction, profit):
    profit = TransactionProfit(transaction=transaction, quantity=transaction.quantity, 
    unitary_profit=profit)
    profit.save()
    return profit


def get_wallet(user):
    stocks = UserStocks.objects.filter(user=user, quantity__gt=0).order_by('code')
    return [parse_stock(s) for s in stocks]


def parse_stock(stock_object):
    close = get_last_close(stock_object.code)
    recommendations = get_recommendations()
    rec = [r.code for r in recommendations] + ['IVVB11']
    return EnrichedStock(
        code=stock_object.code, 
        quantity=stock_object.quantity, 
        price=round(stock_object.weighted_average_cost, 2), 
        value=close.value,
        close_date=close.reference_date.strftime('%d/%m/%Y'),
        recommended=stock_object.code in rec
    )


def get_companies_in_wallets():
    stocks = UserStocks.objects.filter(quantity__gt = 0)\
        .order_by('code')\
        .distinct('code')\
        .values('code')
    return stocks


def get_last_close(stock):
    last_date = StockValues.objects.values('reference_date').last()
    last_date = last_date['reference_date'].strftime('%Y-%m-%d')
    try:
        return StockValues.objects.get(reference_date=last_date, code=stock)
    except: 
        return StockValues(code=stock, value=0, reference_date=datetime.date.today())


def total_invested(user):
    transactions = UserStocksTransactions.objects.filter(user=user, 
        transaction_date__lt=datetime.date.today())
    return sum_wallet(transactions)


def sum_wallet(transactions):
    values = [t.value * t.quantity if t.action == 'buy' else t.value * t.quantity * -1 \
        for t in transactions]
    return sum(values)


def wallet_chart(user):
    dates = get_valid_dates_from_range()
    return sum_daily_values(user, dates)


def get_valid_dates_from_range():
    end = datetime.date.today() - datetime.timedelta(days=1)
    start = end - datetime.timedelta(days=180)
    end = end.strftime('%Y-%m-%d')
    start = start.strftime('%Y-%m-%d')
    # Pegar primeira transacao, listar todos os dias ate hoje
    with connection.cursor() as cursor:
        cursor.execute(f'''
        SELECT DISTINCT reference_date
        FROM stock_values sv
        WHERE sv.reference_date > '{start}'
          AND sv.reference_date < '{end}'
        ''')
        dates = cursor.fetchall()
    return [d[0].strftime('%Y-%m-%d') for d in dates]


def sum_daily_values(user, dates):
    query = f'''
    SELECT DATE(reference_date) date,
        sum(CASE WHEN ust.action = 'buy' THEN ust.quantity * sv.value ELSE ust.quantity * sv.value * -1 END) / (SELECT SUM(CASE WHEN action = 'buy' THEN ROUND(quantity::FLOAT * ust.value::FLOAT) ELSE ROUND(quantity::FLOAT * ust.value::FLOAT) * -1 END) FROM user_stocks_transactions ust WHERE user_id = {user} AND transaction_date < '{dates[0]}') AS growth
    FROM user_stocks_transactions ust
    INNER JOIN stock_values sv on ust.code = sv.code
    WHERE ust.user_id = {user}
    AND ust.transaction_date < '{dates[0]}'
    AND sv.reference_date = '{dates[0]}'
    GROUP BY sv.reference_date
    HAVING sum(CASE WHEN ust.action = 'buy' THEN ust.quantity ELSE ust.quantity * -1 END) > 0
    '''
    for d in dates[1:]:
        query += f'''
        UNION ALL
        SELECT DATE(reference_date),
            sum(CASE WHEN ust.action = 'buy' THEN ust.quantity * sv.value ELSE ust.quantity * sv.value * -1 END) / (SELECT SUM(CASE WHEN action = 'buy' THEN ROUND(quantity::FLOAT * ust.value::FLOAT) ELSE ROUND(quantity::FLOAT * ust.value::FLOAT) * -1 END) FROM user_stocks_transactions ust WHERE user_id = {user} AND transaction_date < '{d}') AS growth
        FROM user_stocks_transactions ust
        INNER JOIN stock_values sv on ust.code = sv.code
        WHERE ust.user_id = {user}
        AND ust.transaction_date < '{d}'
        AND sv.reference_date = '{d}'
        GROUP BY sv.reference_date
        HAVING sum(CASE WHEN ust.action = 'buy' THEN ust.quantity ELSE ust.quantity * -1 END) > 0
        '''
    
    query += 'ORDER BY date ASC'
    
    with connection.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()
    return dict((d[0].strftime('%Y-%m-%d'), d[1]) for d in data)