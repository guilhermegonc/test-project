from .models import Accounts
from .models import Account_Users

def get_account(user):
    if not find_account(user):
        return False
    account_user = Account_Users.objects.get(user_id=user.data.id)
    return Accounts.objects.get(id=account_user.account_id)

def get_account_from_token(token):
    return Accounts.objects.get(token=token)

def find_account(user):
    return Account_Users.objects.filter(user=user.data.id).exists()
