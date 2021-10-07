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
    expense = UserSavings(user=payload['user'],name=payload['name'],objective=payload['objective'],
        date=payload['date'],value=payload['value'])
    expense.save()
    return


def edit_saving(payload):
    expense = UserSavings.objects.get(id=payload['id'], user=payload['user'])
    expense.user = payload['user']
    expense.name = payload['name']
    expense.objective = payload['objective']
    expense.date = payload['date']
    expense.value = payload['value']
    expense.save()
    return


def destroy_saving(payload):
    expense = UserSavings.objects.get(id=payload['id'], user=payload['user'])
    expense.delete()
    return
