from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from menu.userHelper import get_user, get_user_object
from .expensesHelper import get_expenses, dict_expenses
from .forms import ExpenseForm

@login_required
def expenses(request):
    user = get_user(request)
    form = ExpenseForm()
    payload = {'user': user, 'form': form}
    return render(request, 'expenses.html', payload)

@login_required
def load_older_expenses(request):
    user = get_user(request)
    start = int(request.GET.get('start'))
    end = int(request.GET.get('end'))
    expenses = get_expenses(user.data.id, start, end)
    return JsonResponse(dict_expenses(expenses))


def update_expenses(request):
    user = get_user_object(request)

    if request.method == 'POST':
        form = ExpenseForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            type = form.cleaned_data['type']
            date = form.cleaned_data['date']
            value = form.cleaned_data['value']
            recurring = form.cleaned_data['recurring']

    return HttpResponseRedirect('/expenses')
