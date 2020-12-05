from .models import Devices
from .models import Microcontrollers
from .models import Microcontroller_Devices
from .models import Microcontrollers_Accounts

class Socket:
    def __init__(self, microcontroller, devices):
        self.token = microcontroller.token
        self.name = microcontroller.name
        self.device = devices

def create_microcontroller(name, token):
    microcontroller = Microcontrollers(name=name, token=token)
    microcontroller.save()
    return microcontroller

def set_pins(m_id):
    device_pins = ['D0', 'D1', 'D2', 'D3']
    for p in device_pins:
        device = Devices(pin=p)
        device.save()
        m_c = Microcontroller_Devices(microcontroller_id=m_id, device_id=device.id)
        m_c.save()
    return

def set_account(a_id, m_id):
    m_a = Microcontrollers_Accounts(account_id=a_id, microcontroller_id=m_id)
    m_a.save()
    return

def get_microcontroller_details(account):
    microcontrollers = get_microcontrollers(account)
    n_microcontrollers = len(microcontrollers)
    devices = [get_devices(m) for m in microcontrollers]
    return [Socket(microcontrollers[i], devices[i]) for i in range(n_microcontrollers)]

def get_microcontrollers(account):
    mc_account = Microcontrollers_Accounts.objects.filter(account_id=account.id)
    return [Microcontrollers.objects.get(id=mc.microcontroller_id) for mc in mc_account]

def get_devices(microcontroller):
    devices = Microcontroller_Devices.objects.filter(microcontroller=microcontroller.id)
    return  [Devices.objects.get(id=d.device_id) for d in devices]
