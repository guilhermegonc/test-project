from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required

from app.facebookConversionAPIHelper import fb_view_content

from menu.userHelper import get_user
from .expensesHelper import get_expenses, dict_expenses

@login_required
def expenses(request):
    fb_view_content(request)
    user = get_user(request)
    payload = {'user': user}
    return render(request, 'expenses.html', payload)

def load_older_expenses(request):
    user = get_user(request)
    start = int(request.GET.get('start'))
    end = int(request.GET.get('end'))
    expenses = get_expenses(user.data.id, start, end)
    return JsonResponse(dict_expenses(expenses))
