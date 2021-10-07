from django.shortcuts import render
from django.http.response import JsonResponse
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from app.userHelper import get_user, get_user_object
from .expensesHelper import create_expense, edit_expense, destroy_expense, get_expenses, dict_expenses
from .recurringHelper import create_recurring, edit_recurring, destroy_recurring, get_recurring, dict_recurring
from .goalsHelper import create_goal, edit_goal, destroy_goal, get_goals, dict_goals

from .forms import ExpenseForm, RecurringForm, GoalsForm


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


def destroy_expense(request):
    user = get_user_object(request)
    id = int(request.GET.get('id'))
    payload = {'user': user, 'id': id}
    destroy_expense(payload)
    return HttpResponseRedirect('/expenses')


@login_required
def recurring(request):
    user = get_user(request)
    form = RecurringForm()
    payload = {'user': user, 'form': form}
    return render(request, 'recurring-paymentes.html', payload)


@login_required
def load_recurring(request):
    user = get_user(request)
    recurring = get_recurring(user.data.id)
    return JsonResponse(dict_recurring(recurring))


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


def destroy_recurring(request):
    user = get_user_object(request)
    id = int(request.GET.get('id'))
    payload = {'user': user, 'id': id}
    destroy_recurring(payload)
    return HttpResponseRedirect('/recurring-payments')


@login_required
def goals(request):
    user = get_user(request)
    form = GoalsForm()
    payload = {'user': user, 'form': form}
    return render(request, 'goals.html', payload)


@login_required
def load_goals(request):
    user = get_user(request)
    goals = get_goals(user.data.id)
    return JsonResponse(dict_goals(goals))


def update_goal(request):
    user = get_user_object(request)

    if request.method == 'POST':
        form = GoalsForm(request.POST)

        if form.is_valid():
            payload = {
                'id': int(form.cleaned_data['id']),
                'user': user,
                'date': form.cleaned_data['date'],
                'savings': form.cleaned_data['savings'],
                'expenses': form.cleaned_data['expenses'],
            }
            create_goal(payload) if payload['id'] == 0 else edit_goal(payload)
    
    return HttpResponseRedirect('/goals')


def destroy_goal(request):
    user = get_user_object(request)
    id = int(request.GET.get('id'))
    payload = {'user': user, 'id': id}
    destroy_goal(payload)
    return HttpResponseRedirect('/goals')
