from django import forms

class BasicForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Seu nome aqui'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'email@mail.com'}))
    random_big_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '1111 1111 1111 1111'}))
