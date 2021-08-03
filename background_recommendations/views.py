from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def recommendations(request):
    return render(request, 'recomendations.html')
