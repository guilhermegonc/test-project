import json

from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from app.userHelper import is_authenticated, get_user, anonimate_user
from auth0.api_conn import delete_auth0_user


def index(request):
    is_auth = is_authenticated(request)
    user = get_user(request) if is_auth else None
    payload = {'is_auth': is_auth, 'user': user}
    return render(request, 'index.html', payload)


def handler_404(request, *args, **kwargs):
   return render(request,'404.html')


@csrf_exempt
def webhook(request):
    if request.method == "POST":
        data = str(request.body)
        meta = request.META
        print("[Automation Webhook] Got POST from {}:{} with data: {}".format(meta['REMOTE_ADDR'], meta['REMOTE_PORT'],
                                                                              data))
        return HttpResponse(json.dumps({'webhook_got': data}))


@csrf_exempt
def automation_webhook(request):
    if request.method == "POST":
        data = str(request.body)
        meta = request.META
        print("[Automation Webhook] Got POST from {}:{} with data: {}".format(meta['REMOTE_ADDR'], meta['REMOTE_PORT'],
                                                                              data))
        return HttpResponse(json.dumps({'automation_webhook_got': data}))


def callback(request):
    return render(request, 'base.html')

@login_required
def profile(request):
    user = get_user(request)
    payload = {'user': user}
    return render(request, 'profile.html', payload)

@login_required
def destroy_user(request):
    user = get_user(request)
    delete_auth0_user(user.auth0_id)
    anonimate_user(user.data.id)
    return HttpResponseRedirect('/logout')
