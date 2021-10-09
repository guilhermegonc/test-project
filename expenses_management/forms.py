from django import forms


choices = [
    ('Moradia', 'Moradia'),('Mercado', 'Mercado'),('Alimentação', 'Alimentação'),
    ('Transporte', 'Transporte'),('Saúde', 'Saúde'),('Entretenimento', 'Entretenimento'),
    ('Educação', 'Educação'),('Outros', 'Outros'),('Manutenção', 'Manutenção'),
    ('Compras +1000', 'Compras +1000'),('Férias', 'Férias'),
]

saving_choices = [
    ('Reserva','Reserva'),('Carro/Casa','Carro/Casa'),
    ('Previdência','Previdência'),('Longo Prazo','Longo Prazo')
]


class ExpenseForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    value = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'R$ 00,00'}))
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Serviço'}))
    type = forms.ChoiceField(required=False, choices=choices)
    date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': '2021-01-01'}))
    recurring = forms.BooleanField(widget=forms.HiddenInput(), required=False)


class RecurringForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Serviço'}))
    type = forms.ChoiceField(required=False, choices=choices)
    value = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'R$ 00,00'}))
    active = forms.BooleanField(label='Ativo', required=False)


class SavingsForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Serviço'}))
    objective = forms.ChoiceField(choices=saving_choices)
    value = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'R$ 00,00'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': '2021-01-01'}))


class GoalsForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': '2021-01-01'}))
    savings = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Economias R$ 00,00'}))
    expenses = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'Despesas R$ 00,00'}))