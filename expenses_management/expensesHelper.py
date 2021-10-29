from django.db import connection
from .models import UserExpenses


def edit_expense(payload):
    if not UserExpenses.objects.filter(id=payload['id']).exists():
        expense = create_expense(payload)
    else:
        expense = UserExpenses.objects.get(id=payload['id'], user=payload['user'])
        expense.user = payload['user']
        expense.name = payload['name']
        expense.type = payload['type']
        expense.date = payload['date']
        expense.value = payload['value']
        expense.recurring = payload['recurring']
    expense.save()
    return expense


def create_expense(payload):
    return UserExpenses(
        user=payload['user'],
        name=payload['name'],
        type=payload['type'],
        date=payload['date'],
        value=payload['value'],
        recurring=payload['recurring']
    )


def get_expenses_by_category(user, year):
    summary = dict((f'{year}-{i+1:02d}-01', [{'': 0}]) for i in range(12))
    query = f'''
    SELECT DATE_TRUNC('month', date)::DATE::TEXT mth,
           type,
           sum(value) sum_value
    FROM user_expenses
    WHERE user_id = {user}
    AND date > '{year}-01-01'
    AND date < '{year + 1}-01-01'
    GROUP BY mth, type
    ORDER BY mth, type;
    '''
    with connection.cursor() as cursor:
        cursor.execute(query)
        expenses = cursor.fetchall()
    
    [dict_monthly_types(m, t, v, summary) for m, t, v in expenses]
    return summary


def dict_monthly_types(month, type, value, summary):
    summary[month].append({type : value})
    return
