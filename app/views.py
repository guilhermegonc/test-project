import os
import requests
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import Personas
from .forms import BasicForm
from .rd_token import get_valid_token
from .aws_connect import connect_to_s3



def index(request):
    return render(request, 'index.html')


def embed_form(request):
    return render(request, 'embed-form.html')


def custom_form(request):
    form = BasicForm()
    names = Personas.objects.filter().order_by('-id')[:10]

    return render(request, 'custom-form.html', {'form': form, 'db_results': names})


def api_name(request):
    auth = get_valid_token()
    url = 'https://api.rd.services/marketing/account_info'
    r = requests.get(url, headers=auth)
    return render(request, 'api-name.html', {'trk_url': r.json()})


def tic_tac_toe(request):
    return render(request, 'tic-tac-toe.html')


def auth_callback(request):
    s3 = connect_to_s3()
    api_code = request.GET.get('code', None)

    if not api_code:
        new_code = {
            'client_id': os.environ.get('RD_API_CLIENT_ID'),
            'client_secret': os.environ.get('RD_API_CLIENT_SECRET'),
            'code': api_code
        }

        s3.put_object(
            Body=json.dumps(new_code),
            Bucket='test-project-production',
            Key='not-public/rd_code.json'
        )
    
    # return HttpResponseRedirect('/')
    return render(request, 'auth-callback.html', {'rd_api_code': api_code})


def populate_personas(request):

    if request.method == 'POST':
        form = BasicForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            
            new_input = Personas(name=name, email=email)
            new_input.save()
            
    return HttpResponseRedirect('/custom-form/')
