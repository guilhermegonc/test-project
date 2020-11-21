from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out

import os, json, http.client

import auth0.api
from .models import Users, Accounts, Account_Users
from .microcontrollers import get_microcontrollers

@login_required
def dashboard(request):
    user = request.user
    authorized_user = auth0.api.get_auth0_user(user.email)
    
    user = Users.objects.get(auth0_id = authorized_user['user_id'])
    account_users = Account_Users.objects.get(user_id = user.id)
    devices = get_microcontrollers(account_users.account_id)

    payload = {
        'user' : authorized_user['name'],
        'controllers': devices
    }

    return render(request, 'dashboard.html', payload)
