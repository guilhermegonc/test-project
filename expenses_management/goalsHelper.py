from .models import UserGoals


def get_goals(user):
    return UserGoals.objects.filter(user=user).order_by('date')


def create_goal(payload):
    goal = UserGoals(user=payload['user'],date=payload['date'],
                        expense=payload['expense'],saving=payload['saving'])
    goal.save()
    return


def edit_goal(payload):
    expense = UserGoals.objects.get(id=payload['id'], user=payload['user'])
    expense.user = payload['date']
    expense.name = payload['expense']
    expense.type = payload['saving']
    expense.save()
    return


def destroy_goal(payload):
    expense = UserGoals.objects.get(id=payload['id'], user=payload['user'])
    expense.delete()
    return
