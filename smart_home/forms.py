from django import forms

class DeviceForm(forms.Form):
    CHOICES = [
        ('', 'Selecionar'),
        ('D1', 'Tomada 1'),
        ('D2', 'Tomada 2'),
        ('D3', 'Tomada 3'),
        ('D4', 'Tomada 4')
    ]
    pin = forms.CharField(widget=forms.Select(choices=CHOICES))
