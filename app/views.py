import os
import requests
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def cta(request):
    return render(request, 'cta-page.html')