# Generated by Django 3.2.6 on 2021-08-24 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0003_stockvalues'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockvalues',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transactionprofit',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userstocks',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userstockstransactions',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
