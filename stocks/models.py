from django.db import models
from menu.models import Users


class UserStocks(models.Model):
    class Meta:
        db_table = 'user_stocks'
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    code = models.CharField(max_length=31)
    quantity = models.IntegerField()
    weighted_average_cost = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class UserStocksTransactions(models.Model):
    class Meta:
        db_table = 'user_stocks_transactions'
    id = models.AutoField(primary_key=True)
    action = models.CharField(max_length=31)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)    
    code = models.CharField(max_length=31)
    quantity = models.IntegerField()
    value = models.FloatField()
    transaction_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class TransactionProfit(models.Model):
    class Meta:
        db_table = 'transaction_profit'
    id = models.AutoField(primary_key=True)
    transaction = models.ForeignKey('UserStocksTransactions', on_delete=models.CASCADE)    
    quantity = models.FloatField()
    unitary_profit = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class StockValues(models.Model):
    class Meta:
        db_table = 'stock_values'
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=31)
    value = models.FloatField()
    reference_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
