from .models import UserExpenses, UserRecurringExpenses


def get_recurring(user):
    expenses = UserRecurringExpenses.objects.filter(user=user).order_by('-id')
    return expenses


def dict_recurring(recurring):
    return {'data': [parse_recurring(r) for r in recurring]}


def parse_recurring(r):
    return {
            'id': r.id,
            'name': r.name,
            'type': r.type,
            'active': r.active,
            'value': r.value
        }

def create_recurring(payload):
    expense = UserRecurringExpenses(user=payload['user'],name=payload['name'],type=payload['type'],
        date=payload['date'],value=payload['value'],recurring=payload['recurring'])
    expense.save()
    return

def edit_recurring(payload):
    expense = UserRecurringExpenses.objects.get(id=payload['id'], user=payload['user'])
    expense.user = payload['user']
    expense.name = payload['name']
    expense.type = payload['type']
    expense.value = payload['value']
    expense.active = payload['active']
    expense.save()
    return

def destroy_recurring(payload):
    expense = UserRecurringExpenses.objects.get(id=payload['id'], user=payload['user'])
    expense.delete()
    return