def get_transactions(model, user, start=0, end=20):
    return model.objects.filter(user=user).order_by('-id')[start:end]


def remove_transaction(model, payload):
    transaction = model.objects.get(id=payload['id'], user=payload['user'])
    transaction.delete()
    return