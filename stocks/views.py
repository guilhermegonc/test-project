from enum import auto
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from menu.userHelper import get_user
from stocks.stocksHelper import get_wallet


@login_required
def wallet(request):
    user = get_user(request)
    stocks = get_wallet(user)
    payload = {'user': user.auth0_name, 'stocks': stocks}
    return render(request, 'wallet.html', payload)
