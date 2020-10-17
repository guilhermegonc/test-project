import os
import requests
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import Personas
from .forms import BasicForm
from .aws_connect import connect_to_s3


def index(request):
    return render(request, 'index.html')


def embed_form(request):
    return render(request, 'embed-form.html')


def custom_form(request):
    form = BasicForm()
    names = Personas.objects.filter().order_by('-id')[:10]

    return render(request, 'custom-form.html', {'form': form, 'db_results': names})


def tic_tac_toe(request):
    return render(request, 'tic-tac-toe.html')


def populate_personas(request):
    if request.method == 'POST':
        form = BasicForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            
            new_input = Personas(name=name, email=email)
            new_input.save()
            
    return HttpResponseRedirect('/custom-form/')


def atomic(request):
    return render(request, 'atomic.html')


def confirm_auth0(request):
    return


def logout(request):
    return