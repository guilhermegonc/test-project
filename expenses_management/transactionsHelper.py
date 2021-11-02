from .expensesHelper import get_expenses_averages, empty_averages, get_expenses_by_category
from .savingsHelper import get_monthly_saving, summary_savings
from .goalsHelper import get_monthly_goals

import datetime
from dateutil.relativedelta import relativedelta


def get_transactions(model, user, start=0, end=20):
    transactions = model.objects.filter(user=user).order_by('-id')[start:end]
    return {'data': list(transactions.values())}


def remove_transaction(model, payload):
    transaction = model.objects.get(id=payload['id'], user=payload['user'])
    transaction.delete()
    return


def get_finances_summary(user):
    months_dict = list_months()
    first_month = list(months_dict.keys())[0]
    average_categories = empty_averages(user, first_month)
    summary = {
        'months': months_dict, 
        'averages': average_categories,
        }
    return populate_finance_data(summary, user)


def list_months():
    trunc_month = datetime.datetime.today().date()
    trunc_month = trunc_month.replace(day=1)
    min_date = trunc_month - relativedelta(months=12)
    months = [str_date(min_date + relativedelta(months=i)) for i in range(25)]
    return dict((m, empty_month()) for m in months)


def str_date(date):
    return date.strftime('%Y-%m-%d')


def empty_month():
    return {
        'expenses': {
            'total': 0,
            'goal': 0,
            'categories': {}
        },
        'savings': {
            'total': 0,
            'goal': 0,
            'categories': {}
        }
    }

def populate_finance_data(user_finances, user):
    min_date = list(user_finances['months'].keys())[0]
    max_date = list(user_finances['months'].keys())[-1]
    user_finances['averages'] = add_averages(user_finances['averages'], user)
    user_finances['savingsSum'] = summary_savings(user)

    expenses = load_expenses(user, min_date, max_date)
    [add_expenses(user_finances['months'][m]['expenses'], expenses, m)\
        for m in user_finances['months'].keys()]

    savings = load_savings(user, min_date, max_date)
    [add_savings(user_finances['months'][m]['savings'], savings, m)\
        for m in user_finances['months'].keys()]

    goals = load_goals(user, min_date, max_date)
    [add_goals(user_finances['months'][m], goals, m)\
        for m in user_finances['months'].keys()]

    return user_finances


def add_averages(empty_averages, user):
    user_averages = get_expenses_averages(user)
    return {**empty_averages, **user_averages}


def load_expenses(user, min_date, max_date):
    return get_expenses_by_category(user, min_date, max_date)


def add_expenses(expense_object, expenses, key):
    if expenses.get(key):
        expense_object['categories'] = expenses[key]
        expense_object['total'] = sum(expenses[key].values())
    return expense_object


def load_savings(user, min_date, max_date):
    return get_monthly_saving(user, min_date, max_date)


def add_savings(saving_object, savings, key):
    if savings.get(key):
        saving_object['categories'] = savings[key]
        saving_object['total'] = sum(savings[key].values())
    return saving_object


def load_goals(user, min_date, max_date):
    return get_monthly_goals(user, min_date, max_date)


def add_goals(goals_object, goals, key):
    if goals.get(key):
        goals_object['expenses']['goal'] = goals[key]['expenses']
        goals_object['savings']['goal'] = goals[key]['savings']
    return goals_object
