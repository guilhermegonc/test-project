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
    ).save()


def get_expenses_averages(user):
    query = f'''
    WITH monthly_ticket AS (
        SELECT DATE_TRUNC('month', date)::DATE::TEXT mth, 
           type,
           sum(value) sum_value
        FROM user_expenses
        WHERE user_id = {user}
        AND date >= now() - INTERVAL '3 month'
        AND date < now()
        GROUP BY mth, type
        ORDER BY type
    )
    SELECT type,
           avg(sum_value) avg
    FROM monthly_ticket
    GROUP BY type
    ORDER BY type;
    '''
    with connection.cursor() as cursor:
        cursor.execute(query)
        expenses = cursor.fetchall()
    
    return dict((x,y) for x,y in expenses)


def get_expenses_by_category(user, min_date, max_date):
    query = f'''
    SELECT DATE_TRUNC('month', date)::DATE::TEXT mth,
           type,
           sum(value) sum_value
    FROM user_expenses
    WHERE user_id = {user}
    AND date >= '{min_date}'
    AND date <= '{max_date}'
    GROUP BY mth, type
    ORDER BY mth, type;
    '''
    with connection.cursor() as cursor:
        cursor.execute(query)
        expenses = cursor.fetchall()
    
    summary = {}
    [dict_monthly_types(m, t, v, summary) for m, t, v in expenses]
    return summary


def dict_monthly_types(month, type, value, summary):
    if summary.get(month) is None:
        summary[month] = {}
    summary[month][type] = value
    return


def empty_averages(user, min_date):
    query = f'''
    SELECT DISTINCT type
      FROM user_expenses
    WHERE user_id = {user}
    AND date >= '{min_date}'
    ORDER BY type;
    '''
    with connection.cursor() as cursor:
        cursor.execute(query)
        types = cursor.fetchall()
    
    return dict((t[0], 0) for t in types)
