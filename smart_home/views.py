from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import auth0.api
from .models import Users, Account_Users, Microcontrollers, Devices
from .microcontrollers import get_microcontrollers
from .forms import DeviceForm

@login_required
def dashboard(request):
    user = request.user
    authorized_user = auth0.api.get_auth0_user(user.email)
    user = Users.objects.get(auth0_id=authorized_user['user_id'])
    account_users = Account_Users.objects.get(user_id=user.id)
    devices = get_microcontrollers(account_users.account_id)

    payload = {
        'user' : authorized_user['name'],
        'controllers': devices
    }

    return render(request, 'dashboard.html', payload)

@login_required
def create_pin(request):
    form = DeviceForm()
    return render(request, 'pin.html', {'form': form})


def create_device(request):
    microcontroller = Microcontrollers(token='token')
    microcontroller.save()

    device_pins = ['D1', 'D2', 'D3', 'D4']
    for p in device_pins:
        device = Devices(pin=p)
        device.save()
