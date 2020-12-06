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

def update(microcontroller, name):
    microcontroller.name = name
    microcontroller.save()
    return microcontroller

def destroy(microcontroller):
    microcontroller.delete()
    devices = get_devices(microcontroller)
    devices = [d.delete() for d in devices]
    return microcontroller

def set_account(account, microcontroller):
    m_a = Microcontrollers_Accounts(account_id=account.id, microcontroller_id=microcontroller.id)
    m_a.save()
    return

def set_pins(microcontroller):
    pins = ['D0', 'D1', 'D2', 'D3']
    for p in pins:
        d = Devices(pin=p)
        d.save()
        mc_device = Microcontroller_Devices(microcontroller_id=microcontroller.id, device_id=d.id)
        mc_device.save()
    return 

def get_microcontroller_details(account):
    microcontrollers = get_microcontrollers(account)
    n_microcontrollers = len(microcontrollers)
    devices = [get_devices(m) for m in microcontrollers]
    return [Socket(microcontrollers[i], devices[i]) for i in range(n_microcontrollers)]

def get_microcontrollers(account):
    mc_account = Microcontrollers_Accounts.objects.filter(account_id=account.id)
    return [Microcontrollers.objects.get(id=mc.microcontroller_id) for mc in mc_account]

def get_microcontroller_from_token(token):
    return Microcontrollers.objects.get(token=token)

def get_devices(microcontroller):
    devices = Microcontroller_Devices.objects.filter(microcontroller=microcontroller.id)
    return  [Devices.objects.get(id=d.device_id) for d in devices]

def user_has_permission(account, microcontroller):
    return Microcontrollers_Accounts.objects.filter(account=account.id, microcontroller=microcontroller.id).exists()
