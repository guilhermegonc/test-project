from uuid import uuid4

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .models import Devices
from .models import Accounts
from .models import Account_Users

from .forms import JoinAccount
from .forms import CreateMicrocontroller
from .forms import UpdateMicrocontroller
from .forms import DevicesControl

from .accountHelper import get_account
from .accountHelper import  find_account
from .accountHelper import get_account_from_token

from .microcontrollerHelper import get_microcontroller_details
from .microcontrollerHelper import create_microcontroller
from .microcontrollerHelper import update
from .microcontrollerHelper import destroy
from .microcontrollerHelper import set_pins
from .microcontrollerHelper import set_account
from .microcontrollerHelper import user_has_permission
from .microcontrollerHelper import get_microcontroller_from_token

from app.userHelper import get_user


@login_required
def smart_home(request):
    user = get_user(request)
    account = get_account(user)
    if not account:
        return HttpResponseRedirect('/join')
    microcontrollers = get_microcontroller_details(account)
    payload = {'user':user.auth0_name, 'microcontrollers':microcontrollers}
    return render(request, 'smart-home.html', payload)

@login_required
def create_account(request):
    user = get_user(request)
    if not find_account(user):
        return HttpResponseRedirect('/smart-home')
    if request.method == 'POST':
        account = Accounts(token=uuid4().hex)
        account.save()
        account_user = Account_Users(account=account, user=user)
        account_user.save()
    return HttpResponseRedirect('/smart-home')

@login_required
def join(request):
    form = JoinAccount()
    payload = {'form': form}
    return render(request, 'join-account.html', payload)

@login_required
def join_account(request):
    user = get_user(request)
    if not find_account(user):
        return HttpResponseRedirect('/smart-home')
    if request.method == 'POST':
        answer = JoinAccount(request.POST)
        if answer.is_valid():
            a_token = answer.cleaned_data['token']
            account = get_account_from_token(a_token)
            account_user = Account_Users(account=account, user=user)
            account_user.save()
    return HttpResponseRedirect('/smart-home')

@login_required
def settings(request):
    user = get_user(request)
    account = get_account(user)
    payload = {'token': account.token}
    return render(request, 'settings.html', payload)

@login_required
def device_settings(request, microcontroller_token):
    first_pin = request.GET.get('pin') if request.GET.get('pin') else 'D0' 
    form = DevicesControl()
    user = get_user(request)
    account = get_account(user)
    microcontrollers = get_microcontroller_details(account)
    microcontrollers = [mc for mc in microcontrollers if mc.token == microcontroller_token]
    if len(microcontrollers) == 0:
        return HttpResponseRedirect('/smart-home')
    payload = {'form': form, 'microcontroller': microcontrollers[0], 'first_pin': first_pin}
    return render(request, 'device.html', payload)

@login_required
def update_device(request):
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
    return HttpResponseRedirect('/smart-home')

@login_required
def add_microcontroller(request):
    form = CreateMicrocontroller()
    return render(request, 'add-microcontroller.html', {'form': form})

@login_required
def populate_microcontroller(request):
    if request.method == 'POST':
        answer = CreateMicrocontroller(request.POST)
        if answer.is_valid():
            token = answer.cleaned_data['token']
            name = answer.cleaned_data['name']
            user = get_user(request)
            account = get_account(user)
            microcontroller = create_microcontroller(name, token)
            set_account(account, microcontroller)
            set_pins(microcontroller)
    return HttpResponseRedirect('/smart-home')

@login_required
def microcontroller(request, microcontroller_token):
    user = get_user(request)
    account = get_account(user)
    if not account:
        return HttpResponseRedirect('/smart-home')
    microcontrollers = get_microcontroller_details(account)
    microcontrollers = [mc for mc in microcontrollers if mc.token == microcontroller_token]
    if len(microcontrollers) == 0:
        return HttpResponseRedirect('/smart-home')
    form = UpdateMicrocontroller()
    payload = {'form': form, 'microcontroller': microcontrollers[0]}
    return render(request, 'microcontroller.html', payload)

@login_required
def update_microcontroller(request, microcontroller_token):
    if request.method == 'POST':
        answer = UpdateMicrocontroller(request.POST)
        if answer.is_valid():
            name = answer.cleaned_data['name']
            microcontroller = get_microcontroller_from_token(microcontroller_token)
            update(microcontroller, name)
    return HttpResponseRedirect('/smart-home')

@login_required
def destroy_microcontroller(request, microcontroller_token):
    user = get_user(request)
    account = get_account(user)
    microcontroller = get_microcontroller_from_token(microcontroller_token)
    if user_has_permission(account, microcontroller):
        destroy(microcontroller)
    return HttpResponseRedirect('/smart-home')
