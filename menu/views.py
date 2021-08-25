from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .userHelper import get_user
from app.facebookConversionAPIHelper import fb_view_content


@login_required
def dashboard(request):
    fb_view_content(request)
    user = get_user(request)
    payload = {'user':user.auth0_name}
    return render(request, 'dashboard.html', payload)
