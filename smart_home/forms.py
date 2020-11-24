from django import forms

class JoinAccount(forms.Form):
    token = forms.CharField(
        max_length=255, 
        widget=forms.TextInput(attrs={'placeholder': 'Token da Conta'})
        )

class MicrocontrollerCreate(forms.Form):
    token = forms.CharField(
        max_length=255, 
        widget=forms.TextInput(attrs={'placeholder': 'Seu Token aqui'})
        )

class DevicesControl(forms.Form):
    device_id = forms.IntegerField(widget=forms.HiddenInput())
    CHOICES = (('D0', 'D0'),('D1', 'D1'),('D2', 'D2'),('D3', 'D3'))
    pin = forms.ChoiceField(required=False, widget=forms.Select, choices=CHOICES)
    name = forms.CharField(max_length=255, required=False)
    active = forms.BooleanField(label="Mostrar na página inicial", required=False)
