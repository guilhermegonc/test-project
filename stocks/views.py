from datetime import date

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .stocksHelper import get_wallet, update_transactions, get_stocks_last_close
from .forms import StockForm
from menu.userHelper import get_user, get_user_object
from stocks_background.recommendationHelper import get_recommendations
from app.facebookConversionAPIHelper import fb_view_content


@login_required
def wallet(request):
    fb_view_content(request)
    user = get_user(request)
    stocks = get_wallet(user.data.id)
    stock_values = get_stocks_last_close()
    form = StockForm()

    payload = {'user': user.auth0_name, 
               'stocks': stocks, 
               'form': form, 
               'stock_values': stock_values}
    
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
def recommendations(request):
    fb_view_content(request)
    stocks = get_recommendations()
    payload = {'stocks': stocks}
    return render(request, 'recommendations.html', payload)
