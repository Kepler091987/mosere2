from betterforms.multiform import MultiModelForm
from django import forms
from .models import *

class ClientsForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = [
            'name',
            'first_name',
            'last_name',
        ]
        labels = {
            'name': '',
            'first_name': '',
            'last_name': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el nombre del cliente'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el apellido paterno del cliente'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el apellido materno del cliente'}),
        }

class PhonesForm(forms.ModelForm):
    class Meta:
        model = Phones
        fields = [
            'phone',
        ]
        labels = {
            'phone': '',
        }
        widgets = {
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el telefono del cliente'}),
        }

class EmailsForm(forms.ModelForm):
    class Meta:
        model = Emails
        fields = [
            'email',
        ]
        labels = {
            'email': '',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el correo del cliente'}),
        }

class CustomersAddressForm(forms.ModelForm):
    class Meta:
        model = customersAddress
        exclude = (' ',)
        fields = [
            'street',
            'number',
            'suburb',
            'city',
            'state',
            'code_postal'
        ]
        labels = {
            'street': 'Dirección:',
            'number': '',
            'suburb': '',
            'city': '',
            'state': '',
            'code_postal': ''
        }
        widgets = {
            'street': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Calle'}),
            'number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Numero'}),
            'suburb': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Colonia'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estado'}),
            'code_postal': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Codigo Postal'})
        }


class FiscalDataForm(forms.ModelForm):
    class Meta:
        model = fiscalData
        fields = [
            'client',
            'rfc',
            'address',
            'state',
            'code_postal',
            'phone',
            'email',
        ]
        labels = {
            'client': 'Cliente',
            'rfc': 'RFC',
            'address': 'Dirección',
            'state': 'Estado',
            'code_postal': 'Codigo Postal',
            'phone': 'Telefono',
            'email': 'Correo',
        }
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'rfc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el RFC'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa la dirección'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el estado'}),
            'code_postal': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el codigo postal'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el numero telefonico'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el correo'}),
        }

class ClientPhoneEmailCustomersAddressForm(MultiModelForm):
    form_classes = {
        'client': ClientsForm,
        'phone': PhonesForm,
        'email': EmailsForm,
        'customersAddress': CustomersAddressForm
    }