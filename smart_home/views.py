from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out

# Create your views here.

@login_required
def dashboard(request):
    return render(request, 'base.html')



# @login_required
# def dashboard(request):
#     user = request.user
#     auth0user = user.social_auth.get(provider='auth0')
#     userdata = {
#         'user_id': auth0user.uid,
#         'name': user.first_name,
#         'picture': auth0user.extra_data['picture'],
#         'email': auth0user.extra_data['email'],
#     }

#     return render(request, 'dashboard.html', {
#         'auth0User': auth0user,
#         'userdata': json.dumps(userdata, indent=4)
#     })