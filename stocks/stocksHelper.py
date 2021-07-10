from .models import UserStocksTransactions
from .models import UserStocks
from .models import TransactionProfit


def update_transactions(user, action, code, quantity, value, transaction_date):
    transaction = UserStocksTransactions(action=action, user=user, 
    code=code, quantity=quantity, value=value, transaction_date=transaction_date)    
    update_wallet(user, transaction, code, quantity, value)
    new_transaction.save()
    return new_transaction

def update_wallet(user, transaction, code, quantity, value):
    if not UserStocks.objects.filter(user=user, code=code).exists():
        create_user_stock(user, code)

    stock = UserStocks.objects.get(user=user, code=code)

    if transaction.action == 'buy':
        new_value = ((stock.quantity * stock.weighted_average_cost) + \
            (quantity * value)) / (stock.quantity + quantity)
        stock.weighted_average_cost = new_value
    
    if transaction.action == 'sell':
        profit = value - stock.weighted_average_cost
        register_profit(transaction, quantity, profit)
        quantity *= -1

    stock.quantity += quantity
    
    if stock.quantity < 0:
        raise ValueError('Insuficient Stocks')
    
    stock.save()
    return stock

def create_user_stock(user, code):
    stock = UserStocks(user=user, code=code,
                        quantity=0, weighted_average_cost=0) 
    stock.save()
    return stock

def register_profit(transaction, quantity, value):
    profit = TransactionProfit(transaction=transaction, 
    quantity=quantity, unitary_profit=value, transaction_date=transaction.transaction_date)
    profit.save()
    return profit

def get_wallet(user):
    stocks = UserStocks.objects.filter(user=user).order_by('code')
    return [s for s in stocks if s.quantity > 0]

def get_stock(user, code):
    return UserStocks.objects.get(user=user, code=code)
