from django import forms


class ExpenseForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Serviço'}))
    type = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Tipo'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': '01/01/2021'}))
    value = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'R$ 00,00'}))
    recurring = forms.BooleanField(label='Mensal')