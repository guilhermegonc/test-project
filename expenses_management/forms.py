from django import forms
from django.conf import settings

import datetime


choices = [
    ('Moradia', 'Moradia'),('Mercado', 'Mercado'),('Alimentação', 'Alimentação'),
    ('Transporte', 'Transporte'),('Saúde', 'Saúde'),('Entretenimento', 'Entretenimento'),
    ('Educação', 'Educação'),('Outros', 'Outros'),('Manutenção', 'Manutenção'),
    ('Compras grandes', 'Compras grandes'),('Férias', 'Férias'),('Pet', 'Pet')
]

saving_choices = [
    ('Reserva','Reserva'),('Casa','Casa'),('Carro','Carro'),
    ('Previdência','Previdência'),('Longo Prazo','Longo Prazo'),
    ('Viagem','Viagem')
]

months = [
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio',
    'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
    'Novembro', 'Dezembro'
]

month_choices = [(f'{datetime.datetime.now().year}-{ind+1:02d}-01',\
    f'{m} - {datetime.datetime.now().year}',) for ind, m in enumerate(months)]

class ExpenseForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    value = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'R$ 00,00'}))
    type = forms.ChoiceField(required=False, choices=choices)
    date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': '15/10/2021'}), input_formats=settings.DATE_INPUT_FORMATS)
    name = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nome (Opcional)'}))
    recurring = forms.BooleanField(widget=forms.HiddenInput(), required=False)


class RecurringForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    type = forms.ChoiceField(required=False, choices=choices)
    value = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'R$ 00,00'}))
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Serviço'}))
    active = forms.BooleanField(label='Ativo', required=False)


class SavingsForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    value = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'R$ 00,00'}))
    objective = forms.ChoiceField(choices=saving_choices)
    date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': '15/01/2021'}), input_formats=settings.DATE_INPUT_FORMATS)
    name = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nome do Fundo ou Broker'}))


class GoalsForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    date = forms.ChoiceField(choices=month_choices)
    savings = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'A guardar R$ 00,00'}))
    expenses = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'A gastar R$ 00,00'}))