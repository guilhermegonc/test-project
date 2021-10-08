from .models import UserGoals


def get_goals(user):
    return UserGoals.objects.filter(user=user).order_by('date')


def create_goal(payload):
    goal = UserGoals(user=payload['user'],date=payload['date'],
                        expenses=payload['expense'],savings=payload['saving'])
    goal.save()
    return


def edit_goal(payload):
    goal = UserGoals.objects.get(id=payload['id'], user=payload['user'])
    goal.user = payload['user']
    goal.date = payload['date']
    goal.expenses = payload['expense']
    goal.savings = payload['saving']
    goal.save()
    return


def remove_goal(payload):
    goal = UserGoals.objects.get(id=payload['id'], user=payload['user'])
    goal.delete()
    return
