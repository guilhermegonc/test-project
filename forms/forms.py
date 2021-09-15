from django import forms

class BasicForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Seu nome aqui'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'email@mail.com'}))
    random_big_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '1111 1111 1111 1111'}))
    phone = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '+00 (00) 3333 3333'}))
    cell_phone = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': '+00 (00) 9999 9999'}))
    twitter = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Twitter'}))
    facebook = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Facebook'}))
    linkedin = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Linkedin'}))
    website = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Site'}))
    company = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Empresa'}))
    role = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Cargo'}))
    state = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Estado'}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Cidade'}))
    communication_consent = forms.BooleanField()
