from django import forms

class JoinAccount(forms.Form):
    token = forms.CharField(
        max_length=255, 
        widget=forms.TextInput(attrs={'placeholder': 'Token da Conta'})
        )

class CreateMicrocontroller(forms.Form):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Dê um apelido para o seu assistente!'})
    )
    token = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Token do Controle'})
    )

class UpdateMicrocontroller(forms.Form):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'Dê um apelido para o seu assistente!'})
    )

class DevicesControl(forms.Form):
    CHOICES_PIN = [('D0', 'D0'), ('D1', 'D1'), ('D2', 'D2'), ('D3', 'D3')]
    pin = forms.ChoiceField(required=False, widget=forms.Select, choices=CHOICES_PIN)
    name = forms.CharField(max_length=255, required=False)
    active = forms.BooleanField(label="Mostrar na página inicial", required=False)
    device = forms.IntegerField(widget=forms.HiddenInput())
