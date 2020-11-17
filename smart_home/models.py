from django.db import models


class Accounts(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Users(models.Model):
    auth0_id = models.CharField(max_length=255)
    role = models.CharField(max_length=31)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Account_Users(models.Model):
    account_id = models.ForeignKey('Accounts', on_delete=models.CASCADE)
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Microcontrollers(models.Model):
    token = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Microcontrollers_Accounts(models.Model):
    microcontrollers_id = models.ForeignKey('Microcontrolllers', on_delete=models.CASCADE)
    accounts_id = models.ForeignKey('Accounts', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Devices(models.Model):
    pin = models.CharField(max_length=31)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Microcontroller_Devices(models.Model):
    microcontrollers_id = models.ForeignKey('Microcontrolllers', on_delete=models.CASCADE)
    device_id = models.ForeignKey('Devices', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)