from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out

import os, json, http.client

import auth0.api
from .models import Users, Accounts, Account_Users, Microcontrollers, Microcontrollers_Accounts, Microcontroller_Devices, Devices

@login_required
def dashboard(request):
    user = request.user
    authorized_user = auth0.api.get_auth0_user(user.email)
    
    user = Users.objects.get(auth0_id = authorized_user['user_id'])
    account_users = Account_Users.objects.get(user_id = user.id)

    micro_accounts = Microcontrollers_Accounts.objects.get(account_id = account_users.account_id)
    microcontroller = Microcontrollers.objects.get(id = micro_accounts.microcontroller_id)

    micro_devices = Microcontroller_Devices.objects.get(microcontroller_id = microcontroller.id)
    devices = Devices.objects.get(id = micro_devices.device_id)

    payload = {
        'user' : authorized_user['name'],
        'controllers': [microcontroller.token],
        'pins': [devices.pin]
    }
    return render(request, 'dashboard.html', payload)
