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


def get_monthly_saving(user, year):
    summary = dict((f'{year}-{i+1:02d}-01', 0) for i in range(12))
    query = f'''
    SELECT DATE_TRUNC('month', date)::DATE::TEXT mth,
           sum(value) sum_value
    FROM user_savings
    WHERE user_id = {user}
    AND date > '{year}-01-01'
    AND date < '{year + 1}-01-01'
    GROUP BY mth;
    '''
    with connection.cursor() as cursor:
        cursor.execute(query)
        savings = cursor.fetchall()
    
    return {**summary, **dict((x,y) for x,y in savings)}


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

