import os
import requests
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

def db(request):
    names = Personas.objects.all()
    return render(request, 'db.html', {"db_results": names})

def custom_form(request):
    form = BasicForm()
    names = Personas.objects.filter().order_by('-id')[:10]
    return render(request, 'custom-form.html', {'form': form, 'db_results': names})

def populate_personas(request):

    if request.method == 'POST':
        form = BasicForm(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']

            new_input = Personas(name=name)
            new_input.save()
            
            return HttpResponseRedirect('/custom-form/')
    return render(request, 'thank-you-page.html')
