from django.db import models
from app.models import Users

class UserExpenses(models.Model):
    class Meta:
        db_table = 'user_expenses'
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    recurring = models.BooleanField(default=False)
    value = models.FloatField()
    expense_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class UserRecurringExpenses(models.Model):
    class Meta:
        db_table = 'user_recurring_expenses'
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    value = models.FloatField()
    active = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class UserSavings(models.Model):
    class Meta:
        db_table = 'user_savings'
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    objective = models.CharField(max_length=255)
    saving_date = models.DateField()
    unitary_value = models.FloatField()
    value = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class UserGoals(models.Model):
    class Meta:
        db_table = 'user_goals'
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateField()
    expenses = models.FloatField()
    savings = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class UserDarfs(models.Model):
    class Meta:
        db_table = 'user_darfs'
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date = models.DateField()
    value = models.FloatField()
    paid = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
