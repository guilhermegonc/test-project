from .models import Devices, Microcontrollers, Microcontroller_Devices, Microcontrollers_Accounts


def create_microcontroller(token):
    microcontroller = Microcontrollers(token=token)
    # microcontroller.save()
    return microcontroller

def set_pins(m_id):
    device_pins = ['D1', 'D2', 'D3', 'D4']
    for p in device_pins:
        device = Devices(pin=p)
        # device.save()
        m_c = Microcontroller_Devices(microcontroller_id=m_id, device_id=device.id)
        # m_c.save()
    return

def set_account(a_id, m_id):
    m_a = Microcontrollers_Accounts(account_id=a_id, microcontroller_id=m_id)
    # m_a.save()
    return
