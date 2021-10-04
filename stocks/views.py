from datetime import date

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .stocksHelper import get_wallet, update_transactions, total_invested, wallet_chart
from .forms import StockForm
from menu.userHelper import get_user, get_user_object
from stocks_background.recommendationHelper import get_recommendations,update_status


@login_required
def wallet(request):
    user = get_user(request)
    stocks = get_wallet(user.data.id)
    momentum = get_recommendations()
    form = StockForm()
    invested = total_invested(user.data.id)
    chart = wallet_chart(user.data.id)

    payload = {
        'user': user.auth0_name, 
        'stocks': stocks,
        'form': form,
        'momentum': momentum,
        'invested': invested,
        'chart': chart
    }
    
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
    stocks = get_recommendations([True, False])
    payload = {'stocks': stocks}
    return render(request, 'recommendations.html', payload)


@login_required
def change_recommendation_status(request):
    code = request.GET.get('code')
    status = request.GET.get('status')
    update_status(code, status)
    return HttpResponseRedirect('/recommendations')