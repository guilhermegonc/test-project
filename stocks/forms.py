from django import forms

class StockForm(forms.Form):
    code = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Código'}))
    unit_price = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'R$ 00,00'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Cotas'}))
    action = forms.CharField(max_length=8, widget=forms.HiddenInput())
