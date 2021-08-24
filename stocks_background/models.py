from django.db import models


class StockRecommendations(models.Model):
    class Meta:
        db_table = 'stock_recommendations'
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=31)
    value = models.FloatField()
    growth = models.FloatField()
    month = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class IbovespaCompanies(models.Model):
    class Meta:
        db_table = 'ibovespa_companies'
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=31)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
