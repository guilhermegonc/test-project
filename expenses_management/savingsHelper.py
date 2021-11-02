from django.db import connection
from .models import UserSavings


def edit_saving(payload):
    if not UserSavings.objects.filter(id=payload['id']).exists():
        saving = create_saving(payload)
    else:
        saving = UserSavings.objects.get(id=payload['id'], user=payload['user'])
        saving.user = payload['user']
        saving.name = payload['name']
        saving.objective = payload['objective']
        saving.date = payload['date']
        saving.value = payload['value']
    saving.save()
    return


def create_saving(payload):
    return UserSavings(
        user=payload['user'],
        name=payload['name'],
        objective=payload['objective'],
        date=payload['date'],
        value=payload['value']
    )


def summary_savings(user):
    query = f'''
    SELECT objective,
           sum(value) sum_value
    FROM user_savings
    WHERE user_id = {user}
    GROUP BY objective;
    '''
    with connection.cursor() as cursor:
        cursor.execute(query)
        savings = cursor.fetchall()

    return dict((o, v) for o, v in savings)


def get_monthly_saving(user, min_date, max_date):
    query = f'''
    SELECT DATE_TRUNC('month', date)::DATE::TEXT mth,
           objective,
           sum(value) sum_value
    FROM user_savings
    WHERE user_id = {user}
    AND date >= '{min_date}'
    AND date <= '{max_date}'
    GROUP BY mth, objective
    ORDER BY mth, objective;
    '''
    with connection.cursor() as cursor:
        cursor.execute(query)
        savings = cursor.fetchall()
    
    summary = {}
    [dict_monthly_types(m, o, v, summary) for m, o, v in savings]
    return summary


def dict_monthly_types(month, objective, value, summary):
    if summary.get(month) is None:
        summary[month] = {}
    summary[month][objective] = value
    return
