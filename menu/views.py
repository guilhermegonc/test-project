from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from .userHelper import get_user

@login_required
def dashboard(request):
    user = get_user(request)
    payload = {'user':user.auth0_name}
    return render(request, 'dashboard.html', payload)