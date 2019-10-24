from betterforms.multiform import MultiModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = [
            'name',
            'phone',
            'email',
            'entry_date',
            'market_stall',
            'Rol',
        ]
        labels = {
            'name':'',
            'phone':'',
            'email': '',
            'entry_date':'',
            'market_stall':'Puesto',
            'Rol':'Rol',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre Completo'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Ingresa el telefono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Ingresa el correo'}),
            'entry_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder':'Ingresa la Fecha de Ingreso'}),
            'market_stall': forms.Select(attrs={'class': 'form-control'}),
            'Rol': forms.Select(attrs={'class': 'form-control'}),
        }

class UserForm(UserCreationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresa el Usuario'}))
    password1= forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Ingresa la Contraseña'}))
    password2= forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirma la contraseña'}))
    class meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2'
        ]


class UserStaffForm(MultiModelForm):
    form_classes = {
        'user': UserForm,
        'staff': StaffForm
    }