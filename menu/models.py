from django.db import models


class Users(models.Model):
    class Meta:
        db_table = 'users'
    auth0_id = models.CharField(max_length=255)
    role = models.CharField(max_length=31)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)