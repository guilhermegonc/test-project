from django.http import HttpResponseRedirect
from django.contrib.auth import logout as log_out
from django.conf import settings
from urllib.parse import urlencode


def login(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def logout(request):
    log_out(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
                 (settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
    return HttpResponseRedirect(logout_url)
