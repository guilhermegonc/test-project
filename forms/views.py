import os
import requests
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .personasHelper import list_personas
from .personasHelper import find_persona

from .models import Personas
from .forms import BasicForm


def embed_form(request):
    return render(request, 'embed-form.html')


def custom_form(request):
    form = BasicForm()
    names = list_personas()
    payload = {'form': form, 'db_results': names}
    return render(request, 'custom-form.html', payload)


def populate_personas(request):
    if request.method == 'POST':
        form = BasicForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            number = form.cleaned_data['random_big_number']
            
            new_input = Personas(name=name, email=email, long_number=number)
            new_input.save()
            
    return HttpResponseRedirect('/custom-form')


def delete_persona(request, persona_id):
    persona = find_persona(persona_id)
    persona.delete()
    return HttpResponseRedirect('/custom-form')