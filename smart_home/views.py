from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out

# Create your views here.

@login_required
def dashboard(request):
    user = request.user
    return render(request, 'dashboard.html')
