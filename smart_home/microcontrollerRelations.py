from .models import Users, Account_Users, Microcontrollers, Microcontrollers_Accounts, Microcontroller_Devices, Devices
import auth0.api

def get_account(u_id):
    return Account_Users.objects.get(user_id=u_id)

def get_user(request):
    user = request.user
    authorized_user = auth0.api.get_auth0_user(user.email)
    return Users.objects.get(auth0_id=authorized_user['user_id']), authorized_user

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
    return [{'id':d.id, 'pin': d.pin, 'name': d.name, 'active': d.active, 'mtoken': m_token} for m in m_devices for d in Devices.objects.filter(id=m.device_id, active=True)]
