from enum import auto
from datetime import date

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from menu.userHelper import get_user, get_user_object
from .stocksHelper import get_wallet, update_transactions, get_stock
from .recomendationHelper import get_momentum

from .forms import StockForm


@login_required
def wallet(request):
    user = get_user(request)
    stocks = get_wallet(user.data.id)
    form = StockForm()

    payload = {'user': user.auth0_name, 'stocks': stocks, 'form': form}
    return render(request, 'wallet.html', payload)

@login_required
def update_wallet(request):
    user = get_user_object(request)

    if request.method == 'POST':
        form = StockForm(request.POST)

        if form.is_valid():
            code = form.cleaned_data['code']
            action = form.cleaned_data['action']
            units = form.cleaned_data['quantity']
            value = form.cleaned_data['unit_price']

            update_transactions(user, action, code, units, value, date.today())
    return HttpResponseRedirect('/wallet')

@login_required
def recomendations(request):
    return render(request, 'recomendation.html')

@login_required
def get_recomendations(request, dt):
    recomendation = get_momentum(end_date=dt)
    return JsonResponse(recomendation)