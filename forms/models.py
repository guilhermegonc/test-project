from django.db import models

class Personas(models.Model):
    id = models.AutoField(primary_key=True)    
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    long_number = models.BigIntegerField(default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
