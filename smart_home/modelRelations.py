from auth0.api_conn import get_auth0_user

from .models import Users, Microcontrollers, Devices, Accounts
from .models import Account_Users, Microcontrollers_Accounts, Microcontroller_Devices

def get_account(u_id):
    if not Account_Users.objects.filter(user=u_id).exists():
        return False
    account_user = Account_Users.objects.get(user_id=u_id)
    return Accounts.objects.get(id=account_user.account_id)

def get_account_from_token(token):
    return Accounts.objects.get(token=token)


def get_user(request):
    user = request.user
    authorized_user = get_auth0_user(user.email)
    if not Users.objects.filter(auth0_id=authorized_user['user_id']).exists():
        user = Users(auth0_id=authorized_user['user_id'], role='admin')
        user.save()
    else:
        user = Users.objects.get(auth0_id=authorized_user['user_id'])
    return user

def get_microcontrollers(a_id):
    micro_account = Microcontrollers_Accounts.objects.filter(account_id = a_id)
    tokens = [get_token(m.microcontroller_id) for m in micro_account]
    devices = [tkn for t in tokens for tkn in t]
    return devices

def get_token(m_id):
    micros = Microcontrollers.objects.get(id = m_id)
    return get_pin(micros.token, micros.id)  

def get_pin(m_token, m_id):
    m_devices = Microcontroller_Devices.objects.filter(microcontroller_id = m_id)
    return [{'id':d.id, 'pin': d.pin, 'name': d.name, 'active': d.active, 'mtoken': m_token} for m in m_devices for d in Devices.objects.filter(id=m.device_id)]
