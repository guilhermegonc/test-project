import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')

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
