# Generated by Django 3.2.6 on 2021-10-03 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0005_alter_stockvalues_reference_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactionprofit',
            name='transaction_date',
        ),
    ]