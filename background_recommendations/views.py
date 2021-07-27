from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


@login_required
def recommendations(request):
    return render(request, 'recomendations.html')

@login_required
def get_recommendations(request):
    return HttpResponseRedirect('/wallet')
