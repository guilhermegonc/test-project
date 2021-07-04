from django.db import models

from menu.models import Users


class UserStocks(models.Model):
    class Meta:
        db_table = 'user_stocks'
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    code = models.CharField(max_length=31)
    quantity = models.IntegerField()
    wighted_average_cost = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class UserStocksTransactions(models.Model):
    class Meta:
        db_table = 'user_stocks_transactions'
    type = models.CharField(max_length=31)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, primary_key = True)    
    code = models.CharField(max_length=31)
    quantity = models.IntegerField()
    value = models.FloatField()
    transaction_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class TransactionProfit(models.Model):
    class Meta:
        db_table = 'transaction_profit'
    transaction = models.ForeignKey('UserStocksTransactions', on_delete=models.CASCADE, primary_key = True)    
    quantity = models.FloatField()
    unitary_profit = models.FloatField()
    transaction_date = models.DateTimeField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
