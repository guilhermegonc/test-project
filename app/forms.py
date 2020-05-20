from django import forms

class BasicForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Nome'}))
    email = forms.EmailField(label='email', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
