import os
import requests
from django.shortcuts import render
from django.http import HttpResponse

from .models import Personas


# Create your views here.
def index(request):
    return render(request, 'index.html')


def cta(request):
    return render(request, 'cta.html')

def template(request):
    return render(request, 'base.html')

def db(request):
    new_ind = Personas(name = 'Frederico')
    new_ind.save()

    names = Personas.objects.all()
    return render(request, 'db.html', {"db_results": names})
