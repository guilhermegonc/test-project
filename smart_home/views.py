from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from uuid import uuid4

from auth0.api_conn import get_auth0_user

from .models import Users, Microcontrollers, Devices, Accounts
from .models import Account_Users, Microcontroller_Devices, Microcontrollers_Accounts

from .modelRelations import get_microcontrollers, get_user, get_user, get_account, get_account_from_token, get_token, get_microcontrollers2, get_pins2
from .microcontrollerSetup import create_microcontroller, set_pins, set_account
from .forms import JoinAccount, MicrocontrollerCreate, DevicesControl

@login_required
def dashboard(request):
    auth0_data = get_auth0_user(request.user.email)
    user = get_user(request)
    account = get_account(user.id)
    if not account:
        return HttpResponseRedirect('/join/')
    microcontrollers = get_microcontrollers(account.id)

    microcontrollers2 = get_microcontrollers2(account.id)
    mc2_token = [{mc2.token: get_pins2(mc2)} for mc2 in microcontrollers2]

    m_tokens = [mc[0]['mtoken'] for mc in microcontrollers]
    microcontrollers = [[pin for pin in mc if pin['active'] == True] for mc in microcontrollers]
    payload = {'user':auth0_data['name'], 'microcontrollers':microcontrollers, 'm_tokens':m_tokens}
    return render(request, 'dashboard.html', payload)

@login_required
def settings(request):
    user = get_user(request)
    account = get_account(user.id)
    payload = {'token': account.token}
    return render(request, 'settings.html', payload)

@login_required
def pins_settings(request, microcontroller_token):
    first_pin = request.GET.get('pin') if request.GET.get('pin') else 'D0' 
    form = DevicesControl()
    user = get_user(request)
    account = get_account(user.id)
    devices = get_microcontrollers(account.id)
    devices = [[pin for pin in dev if pin['mtoken'] == microcontroller_token] for dev in devices]
    devices = [d for d in devices if d != []]
    if len(devices) == 0:
        return HttpResponseRedirect('/dashboard/')
    payload = {'form': form, 'microcontroller': devices[0], 'first_pin': first_pin}
    return render(request, 'pins.html', payload)

@login_required
def update_pins(request):
    if request.method == 'POST':
        form = DevicesControl(request.POST)
        if form.is_valid():
            device = form.cleaned_data['device']
            device = Devices.objects.get(id=device)
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
    return render(request, 'join-account.html', payload)

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
            name = answer.cleaned_data['name']
            user = get_user(request)
            account = get_account(user.id)

            microcontroller = create_microcontroller(name, token)
            set_pins(microcontroller.id)
            set_account(account.id, microcontroller.id)

    return HttpResponseRedirect('/dashboard/')
