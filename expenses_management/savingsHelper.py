from django.db import connection
from .models import UserSavings


def get_savings(user, start=0, end=20):
    return UserSavings.objects.filter(user=user).order_by('-id')[start:end]


def dict_savings(savings):
    return {'data': [parse_savings(s) for s in savings]}


def parse_savings(s):
    return {
            'id': s.id,
            'name': s.name,
            'objective': s.objective,
            'date': s.date.strftime('%d/%m/%Y'),
            'value': s.value
        }


def create_saving(payload):
    saving = UserSavings(user=payload['user'],name=payload['name'],objective=payload['objective'],
        date=payload['date'],value=payload['value'])
    saving.save()
    return


def edit_saving(payload):
    saving = UserSavings.objects.get(id=payload['id'], user=payload['user'])
    saving.user = payload['user']
    saving.name = payload['name']
    saving.objective = payload['objective']
    saving.date = payload['date']
    saving.value = payload['value']
    saving.save()
    return


def remove_saving(payload):
    saving = UserSavings.objects.get(id=payload['id'], user=payload['user'])
    saving.delete()
    return


def get_monthly_saving(user, year):
    summary = {}
    for i in range(12):
        summary[f'{year}-{i+1:02d}-01'] = 0

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
    
    [dict_monthly(m, v, summary) for m, v in savings]
    return summary


def dict_monthly(month, value, summary):
    summary[month] = value
    return


def summary_savings(user):
    summary = {}
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

    [dict_objectives(o, v, summary) for o, v in savings]
    return summary


def dict_objectives(objective, value, result):
    result[objective] = value
    return
