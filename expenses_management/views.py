from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from app.userHelper import get_user, get_user_object
from .transactionsHelper import get_transactions, remove_transaction
from .goalsHelper import edit_goal, get_goals, get_monthly_goals
from .expensesHelper import edit_expense, get_expenses_by_category
from .savingsHelper import edit_saving, get_monthly_saving, summary_savings
from .recurringHelper import edit_recurring, get_recurring

from .forms import ExpenseForm, RecurringForm, GoalsForm, SavingsForm
from .models import UserExpenses, UserGoals, UserRecurringExpenses, UserSavings

import datetime
import sys

@login_required
def dashboard(request):
    user = get_user(request)
    year = datetime.datetime.now().year
    expenses_sum = get_expenses_by_category(user.data.id, year)
    savings_sum = get_monthly_saving(user.data.id, year)
    saving_balances = summary_savings(user.data.id)
    
    goals = get_monthly_goals(user.data.id, year)
    
    payload = {
        'expenses': expenses_sum,  
        'expenses_category': 1, 
        'savings': savings_sum, 
        'goals': goals, 
        'saving_balances': saving_balances, 
        'form_expense': ExpenseForm(), 
        'form_saving': SavingsForm()
    }
    
    return render(request, 'finance-dashboard.html', payload)


@login_required
def expenses(request):
    user = get_user(request)    
    payload = {
        'user': user, 
        'rows': get_transactions(UserExpenses, user.data.id),
        'form': ExpenseForm(), 
    }
    return render(request, 'expenses.html', payload)


@login_required
def savings(request):
    user = get_user(request)    
    payload = {
        'user': user, 
        'rows': get_transactions(UserSavings, user.data.id),
        'form': SavingsForm(), 
    }
    return render(request, 'savings.html', payload)


@login_required
def recurring(request):
    user = get_user(request)
    payload = {
        'user': user, 
        'rows': get_recurring(user.data.id),
        'form': RecurringForm(),
    }
    return render(request, 'recurring-payments.html', payload)


@login_required
def goals(request):
    user = get_user(request)    
    payload = {
        'user': user, 
        'rows': get_goals(user.data.id),
        'form': GoalsForm()
    }
    return render(request, 'goals.html', payload)


@login_required
def load_older(request, transaction_type):
    model = UserExpenses if transaction_type == 'expenses' else UserSavings
    user = get_user(request)
    start = int(request.GET.get('start'))
    end = int(request.GET.get('end'))
    transaction = get_transactions(model, user.data.id, start, end)
    transaction = {'data': list(transaction.values())}
    return JsonResponse(transaction)


@login_required
def destroy_transaction(request, transaction_type):
    if transaction_type == 'expense':
        model = UserExpenses
    if transaction_type == 'recurring':
        model = UserRecurringExpenses
    if transaction_type == 'goal':
        model = UserGoals
    if transaction_type == 'saving':
        model = UserSavings
    
    user = get_user_object(request)
    id = int(request.GET.get('id'))
    payload = {'user': user, 'id': id}
    remove_transaction(model, payload)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
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
            edit_expense(payload)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def update_recurring(request):
    user = get_user_object(request)

    if request.method == 'POST':
        form = RecurringForm(request.POST)

        if form.is_valid():
            payload = {
                'id': int(form.cleaned_data['id']),
                'user': user,
                'name': form.cleaned_data['name'],
                'type': form.cleaned_data['type'],
                'value': float(form.cleaned_data['value']),
                'active': bool(form.cleaned_data['active']),
            }
            edit_recurring(payload)
    return HttpResponseRedirect(request.path_info)


@login_required
def update_goal(request):
    user = get_user_object(request)

    if request.method == 'POST':
        form = GoalsForm(request.POST)

        if form.is_valid():
            payload = {
                'id': int(form.cleaned_data['id']),
                'user': user,
                'date': form.cleaned_data['month_date'],
                'saving': form.cleaned_data['savings'],
                'expense': form.cleaned_data['expenses'],
            }
            edit_goal(payload)
    return HttpResponseRedirect(request.path_info)


@login_required
def update_saving(request):
    user = get_user_object(request)

    if request.method == 'POST':
        form = SavingsForm(request.POST)

        if form.is_valid():
            payload = {
                'id': int(form.cleaned_data['id']),
                'user': user,
                'name': form.cleaned_data['name'],
                'objective': form.cleaned_data['objective'],
                'date': form.cleaned_data['date'],
                'value': float(form.cleaned_data['value']),
            }
            edit_saving(payload)
    return HttpResponseRedirect(request.path_info)
