from django import forms
from .models import *

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = [
            'client',
            'business_name',
            'RFC',
            'address',
            'state',
            'code_postal',
            'phone',
            'email',
        ]
        labels = {
            'client': 'Cliente',
            'business_name': 'Razon Social',
            'RFC': 'RFC',
            'address': 'Dirección',
            'state': 'Estado',
            'code_postal': 'Codigo Postal',
            'phone': 'Telefono',
            'email': 'Correo',
        }
        widgets = {
            'client': forms.Select(attrs={'class':'form-control'}),
            'business_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingresa la razón Social'}),
            'RFC': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingresa el RFC'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingresa la dirección'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ingresa el estado'}),
            'code_postal': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Ingresa el codigo postal'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Ingresa el numero telefonico'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Ingresa el correo'}),
        }