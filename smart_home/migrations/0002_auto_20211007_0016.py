# Generated by Django 3.2.6 on 2021-10-07 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '__first__'),
        ('smart_home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='token',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='devices',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='devices',
            name='name',
            field=models.CharField(max_length=31, null=True),
        ),
        migrations.AddField(
            model_name='microcontroller_devices',
            name='id',
            field=models.AutoField(default='', primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='microcontrollers',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='account_users',
            name='account',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='smart_home.accounts'),
        ),
        migrations.AlterField(
            model_name='account_users',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.users'),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='devices',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='microcontroller_devices',
            name='microcontroller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart_home.microcontrollers'),
        ),
        migrations.AlterField(
            model_name='microcontrollers_accounts',
            name='microcontroller',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='smart_home.microcontrollers'),
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
