from .models import UserStocksTransactions,\
                    UserStocks,\
                    TransactionProfit,\
                    StockValues

from stocks_background.recommendationHelper import get_recommendations


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
    unitary_profit=profit, transaction_date=transaction.transaction_date)
    profit.save()
    return profit


def get_wallet(user):
    stocks = UserStocks.objects.filter(user=user, quantity__gt=0).order_by('code')
    return [parse_stock(s) for s in stocks]


def parse_stock(stock_object):
    close = get_last_close(stock_object.code)
    recommendations = get_recommendations()
    rec = [r.code[:-3] for r in recommendations]
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
    return StockValues.objects.get(reference_date=last_date, code=stock)
