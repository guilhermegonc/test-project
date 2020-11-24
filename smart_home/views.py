from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from uuid import uuid4

from auth0.api_conn import get_auth0_user

from .models import Users, Microcontrollers, Devices, Accounts
from .models import Account_Users, Microcontroller_Devices, Microcontrollers_Accounts

from .modelRelations import get_microcontrollers, get_user, get_user, get_account, get_account_from_token
from .microcontrollerSetup import create_microcontroller, set_pins, set_account
from .forms import JoinAccount, MicrocontrollerCreate, DevicesControl

@login_required
def dashboard(request):
    auth0_data = get_auth0_user(request.user.email)
    user = get_user(request)
    account = get_account(user.id)
    if not account:
        return HttpResponseRedirect('/join/')
    devices = get_microcontrollers(account.id)
    devices = [d for d in devices if d['active'] == True]
    payload = {'user' : auth0_data['name'],'microcontrollers': devices}
    return render(request, 'dashboard.html', payload)

@login_required
def pins_settings(request):
    form = DevicesControl()
    user = get_user(request)
    account = get_account(user.id)
    devices = get_microcontrollers(account.id)
    payload = {'form': form, 'devices': devices}
    return render(request, 'pins-settings.html', payload)

@login_required
def update_pins(request):
    if request.method == 'POST':
        form = DevicesControl(request.POST)
        if form.is_valid():
            device_id = form.cleaned_data['device_id']
            device = Devices.objects.get(id=device_id)
            name = form.cleaned_data['name']
            device.name = name
            is_active = form.cleaned_data['active']
            device.active = is_active
            device.save()
    return HttpResponseRedirect('/dashboard/')

@login_required
def join(request):
    form = JoinAccount()
    payload = {'form': form}
    return render(request, 'join.html', payload)

@login_required
def join_account(request):
    user = get_user(request)
    if Account_Users.objects.filter(user=user.id).exists():
        return HttpResponseRedirect('/dashboard/')
    if request.method == 'POST':
        answer = JoinAccount(request.POST)
        if answer.is_valid():
            a_token = answer.cleaned_data['token']
            account = get_account_from_token(a_token)
            account_user = Account_Users(account=account, user=user)
            account_user.save()
    return HttpResponseRedirect('/dashboard/')

@login_required
def create_account(request):
    user = get_user(request)
    if Account_Users.objects.filter(user=user.id).exists():
        return HttpResponseRedirect('/dashboard/')
    if request.method == 'POST':
        account = Accounts(token=uuid4().hex)
        account.save()
        account_user = Account_Users(account=account, user=user)
        account_user.save()
    return HttpResponseRedirect('/dashboard/')

@login_required
def add_microcontroller(request):
    form = MicrocontrollerCreate()
    return render(request, 'add-microcontroller.html', {'form': form})

@login_required
def populate_microcontroller(request):
    if request.method == 'POST':
        answer = MicrocontrollerCreate(request.POST)

        if answer.is_valid():
            token = answer.cleaned_data['token']
            user = get_user(request.user.email)
            account = get_account(user.id)

            microcontroller = create_microcontroller(token)
            set_pins(microcontroller.id)
            set_account(account.id, microcontroller.id)

    return HttpResponseRedirect('/dashboard/')