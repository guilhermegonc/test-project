from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Users, Account_Users, Microcontrollers, Devices, Microcontroller_Devices, Microcontrollers_Accounts
from .microcontrollerRelations import get_microcontrollers, get_user, get_account
from .microcontrollerSetup import create_microcontroller, set_pins, set_account
from .forms import MicrcontrollerCreate, DevicesControl

@login_required
def dashboard(request):
    user, auth0_details = get_user(request)
    account = get_account(user.id)
    devices = get_microcontrollers(account.account_id)

    payload = {
        'user' : auth0_details['name'],
        'microcontrollers': devices
    }

    return render(request, 'dashboard.html', payload)

@login_required
def add_microcontroller(request):
    form = MicrcontrollerCreate()
    return render(request, 'add-microcontroller.html', {'form': form})

@login_required
def populate_microcontroller(request):
    if request.method == 'POST':
        answer = MicrcontrollerCreate(request.POST)

        if answer.is_valid():
            token = answer.cleaned_data['token']
            user, _ = get_user(request)
            account = get_account(user.id)

            microcontroller = create_microcontroller(token)
            set_pins(microcontroller.id)
            set_account(account.account_id, microcontroller.id)

    return HttpResponseRedirect('/dashboard/')

@login_required
def pins_settings(request):
    form = DevicesControl()
    user, _ = get_user(request)
    account = get_account(user.id)
    devices = get_microcontrollers(account.account_id)

    payload = {
        'form': form,
        'microcontrollers': devices
    }

    return render(request, 'pins-settings.html', payload)

@login_required
def update_pins(request):
    if request.method == 'POST':
        form = DevicesControl(request.POST)

        if form.is_valid():
            device_id = form.cleaned_data['device_id']
            name = form.cleaned_data['name']
            is_active = form.cleaned_data['active']
                
            device = Devices.objects.get(id=device_id)
            device.name = name
            device.save()

            device.active = is_active
            device.save()

    return HttpResponseRedirect('/dashboard/')
