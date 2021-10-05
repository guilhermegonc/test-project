from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from app.userHelper import get_user, get_user_object
from .expensesHelper import create_expense, edit_expense, get_expenses, dict_expenses
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


def update_expense(request):
    user = get_user_object(request)

    if request.method == 'POST':
        form = ExpenseForm(request.POST)

        if form.is_valid():
            payload = {
                'id': int(form.cleaned_data['id']),
                'user': user,
                'name': form.cleaned_data['name'],
                'type': form.cleaned_data['type'],
                'date': form.cleaned_data['date'],
                'value': float(form.cleaned_data['value']),
                'recurring': bool(form.cleaned_data['recurring']),
            }
            create_expense(payload) if payload['id'] == 0 else edit_expense(payload)
    
    return HttpResponseRedirect('/expenses')
