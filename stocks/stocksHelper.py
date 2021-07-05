from .models import UserStocksTransactions
from .models import UserStocks
from .models import TransactionProfit


def update_transactions(user, transaction_type, code, quantity, value, transaction_date):
    transaction = UserStocksTransactions(type=transaction_type, 
                                        user=user.data.id,
                                        code=code,
                                        quantity=quantity,
                                        value=value,
                                        transaction_date=transaction_date)
    update_wallet(user, code, transaction_type, value, quantity)
    transaction.save()
    return transaction

def update_wallet(user, code, transaction_type, value, quantity, transaction_date):
    if not UserStocks.objects.filter(user=user.data.id, code=code).exists():
        create_user_stock(user, code)

    stock = UserStocks.objects.get(user=user.data.id, code=code)
    stock.quantity += quantity

    if transaction_type == 'buy':
        new_value = ((stock.quantity * stock.weighted_average_cost) + \
            (quantity * value)) / stock.quantity
        stock.weighted_average_cost = new_value
    
    else:
        profit = value - stock.weighted_average_cost
        register_profit(quantity, profit, transaction_date)
    
    if stock.quantity < 0:
        raise ValueError('Insuficient Stocks')
    
    stock.save()
    return stock

def create_user_stock(user, code):
    stock = UserStocks(user=user.data.id, code=code,
                        quantity=0, weighted_average_cost=0)
    stock.save()
    return stock

def register_profit(quantity, value, transaction_date):
    profit = TransactionProfit(quantity=quantity, unitary_profit=value, transaction_date=transaction_date)
    profit.save()
    return profit

def get_wallet(user):
    stocks = UserStocks.objects.filter(user=user.data.id).order_by('code')
    return [s for s in stocks if s.quantity > 0]