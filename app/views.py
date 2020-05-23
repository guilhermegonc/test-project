import os
import requests
import simplejson as json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import Personas
from .forms import BasicForm

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

def youtube_live(request):
    return render(request, 'youtube.html')

def auth_callback(request):

    api_code = request.GET.get('code','')
    api_ids = {
        'client_id': os.environ.get('RD_API_CLIENT_ID'),
        'client_secret': os.environ.get('RD_API_CLIENT_SECRET'),
        'code': api_code
    }
    
    with open('api_secret.json') as file:
        json.dump(api_ids, file)
    
    return HttpResponseRedirect('/cta/')

def tic_tac_toe(request):
    return render(request, 'tic-tac-toe.html')