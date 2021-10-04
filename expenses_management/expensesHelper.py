from .models import UserExpenses


def get_expenses(user, start=0, end=50):
    expenses = UserExpenses.objects.filter(user=user).order_by('-id')[start:end]
    return expenses


def dict_expenses(expenses):
    return {'data': [parse_expense(e) for e in expenses]}


def parse_expense(e):
    return {
            'name': e.name,
            'type': e.type,
            'recurring': e.recurring,
            'value': e.value,
            'date': e.expense_date.strftime('%Y-%m-%d')
        }