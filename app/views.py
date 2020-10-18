import os
import requests
import json
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .aws_connect import connect_to_s3


def index(request):
    return render(request, 'index.html')