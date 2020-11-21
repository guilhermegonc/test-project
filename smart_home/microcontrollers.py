from .models import Users
from .models import Accounts, Account_Users
from .models import Microcontrollers, Microcontrollers_Accounts, Microcontroller_Devices
from .models import Devices

def get_microcontrollers(a_id):
    micro_account = Microcontrollers_Accounts.objects.filter(account_id = a_id)
    tokens = [get_token(m.microcontroller_id) for m in micro_account]
    devices = [tkn for t in tokens for tkn in t]
    devices.sort()
    return devices

def get_token(m_id):
    micros = Microcontrollers.objects.get(id = m_id)
    return get_pin(micros.token, micros.id)  

def get_pin(m_token, m_id):
    m_devices = Microcontroller_Devices.objects.filter(microcontroller_id = m_id)
    return [(d.pin, m_token) for m in m_devices for d in Devices.objects.filter(id=m.device_id)]
