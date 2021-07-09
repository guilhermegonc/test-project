from django import forms

class StockForm(forms.Form):
    code = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Código'}))
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Cotas'}))
    unit_price = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'R$ 00,00'}))
