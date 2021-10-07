from .models import UserGoals


def get_goals(user):
    return UserGoals.objects.filter(user=user).order_by('date')


def dict_goals(goals):
    return {'data': [parse_goals(g) for g in goals]}


def parse_goals(goal):
    return {
            'id': goal.id,
            'name': goal.name,
            'type': goal.type,
            'recurring': goal.recurring,
            'value': goal.value,
            'date': goal.date.strftime('%Y-%m-%d')
        }

def create_goal(payload):
    expense = UserGoals(user=payload['user'],name=payload['name'],type=payload['type'],
        date=payload['date'],value=payload['value'],recurring=payload['recurring'])
    expense.save()
    return

def edit_goal(payload):
    expense = UserGoals.objects.get(id=payload['id'], user=payload['user'])
    expense.user = payload['user']
    expense.name = payload['name']
    expense.type = payload['type']
    expense.date = payload['date']
    expense.value = payload['value']
    expense.recurring = payload['recurring']
    expense.save()
    return

def destroy_goal(payload):
    expense = UserGoals.objects.get(id=payload['id'], user=payload['user'])
    expense.delete()
    return
