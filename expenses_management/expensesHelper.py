from .models import UserExpenses


def get_expenses(user, start=0, end=20):
    expenses = UserExpenses.objects.filter(user=user).order_by('-id')[start:end]
    return expenses


def dict_expenses(expenses):
    return {'data': [parse_expense(e) for e in expenses]}


def parse_expense(e):
    return {
            'id': e.id,
            'name': e.name,
            'type': e.type,
            'recurring': e.recurring,
            'value': e.value,
            'date': e.expense_date.strftime('%Y-%m-%d')
        }

def create_expense(payload):
    expense = UserExpenses(user=payload['user'],name=payload['name'],type=payload['type'],
        expense_date=payload['date'],value=payload['value'],recurring=payload['recurring'])
    expense.save()
    return

def edit_expense(payload):
    expense = UserExpenses.objects.get(id=payload['id'])
    expense.user = payload['user']
    expense.name = payload['name']
    expense.type = payload['type']
    expense.expense_date = payload['date']
    expense.value = payload['value']
    expense.recurring = payload['recurring']
    expense.save()
    return