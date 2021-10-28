from .models import UserRecurringExpenses


def get_recurring(user, active=[True, False]):
    return UserRecurringExpenses.objects.filter(user=user, active__in=active).order_by('name')


def edit_recurring(payload):
    if not UserRecurringExpenses.objects.filter(id=payload['id']).exists():
        recurring = create_recurring(payload)
    else:
        recurring = UserRecurringExpenses.objects.get(id=payload['id'], user=payload['user'])
        recurring.user = payload['user']
        recurring.name = payload['name']
        recurring.type = payload['type']
        recurring.value = payload['value']
        recurring.active = payload['active']
    recurring.save()
    return recurring


def create_recurring(payload):
    return UserRecurringExpenses(
        user=payload['user'],
        name=payload['name'],
        type=payload['type'],
        value=payload['value'],
        active=payload['active']
    )
