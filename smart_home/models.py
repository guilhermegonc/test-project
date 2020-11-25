from django.db import models


class Accounts(models.Model):
    class Meta:
        db_table = 'accounts'
    token = models.CharField(max_length=255, null=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Users(models.Model):
    class Meta:
        db_table = 'users'
    auth0_id = models.CharField(max_length=255)
    role = models.CharField(max_length=31)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Account_Users(models.Model):
    class Meta:
        db_table = 'account_users'
    account = models.ForeignKey('Accounts', on_delete=models.CASCADE, primary_key = True)
    user = models.ForeignKey('Users', on_delete=models.CASCADE)
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
    microcontroller = models.ForeignKey('Microcontrollers', on_delete=models.CASCADE, primary_key=True)
    account = models.ForeignKey('Accounts', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Devices(models.Model):
    class Meta:
        db_table = 'devices'
    pin = models.CharField(max_length=31)
    name = models.CharField(max_length=31, null=True)
    active = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Microcontroller_Devices(models.Model):
    class Meta:
        db_table = 'microcontroller_devices'
    microcontroller = models.ForeignKey('Microcontrollers', on_delete=models.CASCADE, primary_key=True)
    device = models.ForeignKey('Devices', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
