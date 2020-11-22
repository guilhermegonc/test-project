from django import forms

class MicrcontrollerCreate(forms.Form):
    token = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Seu Token aqui'}))

class DevicesControl(forms.Form):
    device_id = forms.IntegerField(widget=forms.HiddenInput())
    pin = forms.CharField(max_length=31, required=False)
    name = forms.CharField(max_length=255, required=False)
    active = forms.BooleanField(label="Mostrar na página inicial", required=False)
