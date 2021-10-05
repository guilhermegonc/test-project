from django import forms


class ExpenseForm(forms.Form):
    choices = [
        ('Moradia', 'Moradia'),('Mercado', 'Mercado'),('Alimentação', 'Alimentação'),
        ('Transporte', 'Transporte'),('Saúde', 'Saúde'),('Entretenimento', 'Entretenimento'),
        ('Educação', 'Educação'),('Outros', 'Outros'),('Manutenção', 'Manutenção'),
        ('Compras +1000', 'Compras +1000'),('Férias', 'Férias'),
    ]
    id = forms.IntegerField(widget=forms.HiddenInput())
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Serviço'}))
    type = forms.ChoiceField(required=False, choices=choices)
    date = forms.DateField(widget=forms.DateInput(attrs={'placeholder': '2021-01-01'}))
    value = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'R$ 00,00'}))
    recurring = forms.BooleanField(label='Mensal', required=False)