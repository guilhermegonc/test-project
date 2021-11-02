from django.db import connection
from .models import UserGoals


def get_goals(user, year):
    return UserGoals.objects.filter(user=user, 
        date__gte=f'{year}-01-01', 
        date__lt=f'{year + 1}-01-01').order_by('date')


def edit_goal(payload):
    if not UserGoals.objects.filter(id=payload['id']).exists():
        goal = create_goal(payload)
    else:
        goal = UserGoals.objects.get(id=payload['id'], user=payload['user'])
        goal.user = payload['user']
        goal.date = payload['date']
        goal.expenses = payload['expense']
        goal.savings = payload['saving']
    goal.save()
    return goal


def create_goal(payload):
    return UserGoals(
        user=payload['user'],
        date=payload['date'],
        expenses=payload['expense'],
        savings=payload['saving']
    )


def get_monthly_goals(user, min_date, max_date):
    query = f'''
    SELECT DATE_TRUNC('month', date)::DATE::TEXT mth,
           sum(expenses) sum_expenses,
           sum(savings) sum_savings
    FROM user_goals
    WHERE user_id = {user}
    AND date >= '{min_date}'
    AND date < '{max_date}'
    GROUP BY mth;
    '''
    with connection.cursor() as cursor:
        cursor.execute(query)
        goals = cursor.fetchall()

    summary={}
    [dict_monthly(m, e, s, summary) for m, e, s in goals]
    return summary


def dict_monthly(month, expenses, savings, summary):
    summary[month] = {'expenses': expenses, 'savings': savings}
    return
