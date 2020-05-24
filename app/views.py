import os
import requests
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import Personas
from .forms import BasicForm
from .rd_token import get_valid_token


def index(request):
    return render(request, 'index.html')


def cta(request):
    return render(request, 'cta.html')

def template(request):
    return render(request, 'base.html')

def custom_form(request):
    form = BasicForm()
    names = Personas.objects.filter().order_by('-id')[:10]
    return render(request, 'custom-form.html', {'form': form, 'db_results': names})

def populate_personas(request):

    if request.method == 'POST':
        form = BasicForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            new_input = Personas(name=name, email=email)
            new_input.save()
            
    return HttpResponseRedirect('/custom-form/')

def trk_callback(request):
    auth = get_valid_token()
    url = 'https://api.rd.services/marketing/account_info'
    r = requests.get(url, headers=auth)
    return render(request, 'trk.html', {'trk_url': r.json()})

def tic_tac_toe(request):
    return render(request, 'tic-tac-toe.html')

def auth_callback(request):
    api_code = request.GET.get('code','Sem resposta')
    return render(request, 'auth-callback.html', {'rd_api_code': api_code})
