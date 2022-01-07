from django import forms
from django.conf import settings

import datetime


choices = [
    ('Alimentação', 'Alimentação'),
    ('Compras grandes', 'Compras grandes'),
    ('Educação', 'Educação'),
    ('Entretenimento', 'Entretenimento'),
    ('Férias', 'Férias'),
    ('Manutenção', 'Manutenção'),
    ('Mercado', 'Mercado'),
    ('Moradia', 'Moradia'),
    ('Pet', 'Pet'),
    ('Saúde', 'Saúde'),
    ('Transporte', 'Transporte'),
    ('Vestuário', 'Vestuário'),
    ('Outros', 'Outros'),
]

saving_choices = [
    ('Casa','Casa'),
    ('Carro','Carro'),
    ('Longo Prazo','Longo Prazo'),
    ('Previdência','Previdência'),
    ('Reserva','Reserva'),
    ('Viagem','Viagem'),
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
    value = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'R$ 00,00'}))
    type = forms.ChoiceField(required=False, choices=choices)
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
    month_date = forms.ChoiceField(choices=month_choices)
    savings = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'A guardar R$ 00,00'}))
    expenses = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'A gastar R$ 00,00'}))
