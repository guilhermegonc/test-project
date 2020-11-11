from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out

import os

@login_required
def dashboard(request):
    user = request.user
    payload = {
        'pin': 'D2',
        'token': os.environ.get('BLYNK_TOKEN')
    }
    return render(request, 'dashboard.html', payload)
