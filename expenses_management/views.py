from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from app.userHelper import get_user, get_user_object
from .goalsHelper import create_goal, edit_goal, remove_goal, get_goals, get_monthly_goals
from .expensesHelper import create_expense, edit_expense, remove_expense,\
    get_expenses, dict_expenses, get_monthly_balance, get_expenses_by_category

from .savingsHelper import create_saving, edit_saving, remove_saving,\
    get_savings, dict_savings, get_monthly_saving, summary_savings

from .recurringHelper import create_recurring, edit_recurring,\
    remove_recurring, get_recurring

from .forms import ExpenseForm, RecurringForm, GoalsForm, SavingsForm
import datetime


@login_required
def dashboard(request):
    user = get_user(request)
    year = datetime.datetime.now().year
    
    expenses_sum = get_monthly_balance(user.data.id, year)
    # expenses_category = get_expenses_by_category(user.data.id, year)
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
    form = ExpenseForm()
    expenses = get_expenses(user.data.id)
    payload = {'user': user, 'form': form, 'rows': expenses}
    return render(request, 'expenses.html', payload)


@login_required
def load_older_expenses(request):
    user = get_user(request)
    start = int(request.GET.get('start'))
    end = int(request.GET.get('end'))
    expenses = get_expenses(user.data.id, start, end)
    return JsonResponse(dict_expenses(expenses))

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
            create_expense(payload) if payload['id'] == 0 else edit_expense(payload)
    
    return HttpResponseRedirect('/expenses')


@login_required
def destroy_expense(request):
    user = get_user_object(request)
    id = int(request.GET.get('id'))
    payload = {'user': user, 'id': id}
    remove_expense(payload)
    return HttpResponseRedirect('/expenses')


@login_required
def recurring(request):
    user = get_user(request)
    form = RecurringForm()
    recurring = get_recurring(user.data.id)
    payload = {'user': user, 'form': form, 'rows': recurring}
    return render(request, 'recurring-payments.html', payload)


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
            create_recurring(payload) if payload['id'] == 0 else edit_recurring(payload)
    
    return HttpResponseRedirect('/recurring-payments')


@login_required
def destroy_recurring(request):
    user = get_user_object(request)
    id = int(request.GET.get('id'))
    payload = {'user': user, 'id': id}
    remove_recurring(payload)
    return HttpResponseRedirect('/recurring-payments')


@login_required
def goals(request):
    user = get_user(request)
    form = GoalsForm()
    goals = get_goals(user.data.id)
    payload = {'user': user, 'form': form, 'rows': goals}
    return render(request, 'goals.html', payload)


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
            create_goal(payload) if payload['id'] == 0 else edit_goal(payload)
    
    return HttpResponseRedirect('/goals')

@login_required
def destroy_goal(request):
    user = get_user_object(request)
    id = int(request.GET.get('id'))
    payload = {'user': user, 'id': id}
    remove_goal(payload)
    return HttpResponseRedirect('/goals')


@login_required
def savings(request):
    user = get_user(request)
    form = SavingsForm()
    expenses = get_savings(user.data.id)
    payload = {'user': user, 'form': form, 'rows': expenses}
    return render(request, 'savings.html', payload)


@login_required
def load_older_savings(request):
    user = get_user(request)
    start = int(request.GET.get('start'))
    end = int(request.GET.get('end'))
    savings = get_savings(user.data.id, start, end)
    return JsonResponse(dict_savings(savings))


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
            create_saving(payload) if payload['id'] == 0 else edit_saving(payload)
    
    return HttpResponseRedirect('/savings')


@login_required
def destroy_saving(request):
    user = get_user_object(request)
    id = int(request.GET.get('id'))
    payload = {'user': user, 'id': id}
    remove_saving(payload)
    return HttpResponseRedirect('/savings')
