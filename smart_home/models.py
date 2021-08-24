from django.db import models
from menu.models import Users


class Accounts(models.Model):
    class Meta:
        db_table = 'accounts'
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=255, null=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Account_Users(models.Model):
    class Meta:
        db_table = 'account_users'
    account = models.OneToOneField('Accounts', on_delete=models.CASCADE, primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Microcontrollers(models.Model):
    class Meta:
        db_table = 'microcontrollers'
    name = models.CharField(max_length=255, null=True)
    token = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Microcontrollers_Accounts(models.Model):
    class Meta:
        db_table = 'microcontrollers_accounts'
    microcontroller = models.OneToOneField('Microcontrollers', on_delete=models.CASCADE, primary_key=True)
    account = models.ForeignKey('Accounts', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Devices(models.Model):
    class Meta:
        db_table = 'devices'
    id = models.AutoField(primary_key=True)
    pin = models.CharField(max_length=31)
    name = models.CharField(max_length=31, null=True)
    active = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Microcontroller_Devices(models.Model):
    class Meta:
        db_table = 'microcontroller_devices'
    id = models.AutoField(primary_key=True)
    microcontroller = models.ForeignKey('Microcontrollers',on_delete=models.CASCADE)
    device = models.ForeignKey('Devices', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
