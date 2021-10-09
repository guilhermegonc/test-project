from django.db import connection
from .models import UserExpenses
import sys


def get_expenses(user, start=0, end=20):
    return UserExpenses.objects.filter(user=user).order_by('-id')[start:end]


def dict_expenses(expenses):
    return {'data': [parse_expense(e) for e in expenses]}


def parse_expense(e):
    return {
            'id': e.id,
            'name': e.name,
            'type': e.type,
            'recurring': e.recurring,
            'value': e.value,
            'date': e.date.strftime('%d/%m/%Y')
        }


def create_expense(payload):
    expense = UserExpenses(user=payload['user'],name=payload['name'],type=payload['type'],
        date=payload['date'],value=payload['value'],recurring=payload['recurring'])
    expense.save()
    return


def edit_expense(payload):
    expense = UserExpenses.objects.get(id=payload['id'], user=payload['user'])
    expense.user = payload['user']
    expense.name = payload['name']
    expense.type = payload['type']
    expense.date = payload['date']
    expense.value = payload['value']
    expense.recurring = payload['recurring']
    expense.save()
    return


def remove_expense(payload):
    expense = UserExpenses.objects.get(id=payload['id'], user=payload['user'])
    expense.delete()
    return


def get_monthly_balance(user, year):
    query = f'''
    SELECT DATE_TRUNC('month', date)::DATE::TEXT mth,
           sum(value) sum_value
    FROM user_expenses
    WHERE user_id = {user}
    AND date > '{year}-01-01'
    AND date < '{year + 1}-01-01'
    GROUP BY mth;
    '''
    with connection.cursor() as cursor:
        cursor.execute(query)
        expenses = cursor.fetchall()
    
    summary = {}
    [dict_monthly(d, v, summary) for d,v in expenses]
    return summary


def dict_monthly(date, value, summary):
    summary[date] = value
    return
