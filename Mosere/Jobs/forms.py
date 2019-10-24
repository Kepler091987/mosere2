from django import forms
from .models import *

class JobsForm(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = [
            'client',
            'number_folio',
            'description',
            'time',
            'date_start',
            'date_end',
            'scheduled_date',
            'staff',
        ]
        labels = {
            'client': 'Cliente',
            'number_folio': 'Numero de Folio',
            'description': 'Descripción',
            'time': 'Tiempo estimado',
            'date_start': 'fecha de inicio',
            'date_end': 'fecha de terminado',
            'scheduled_date': 'fecha de programado',
            'staff': 'Personal asignado',
        }
        widgets = {
            'client': forms.Select(attrs={'class': 'form-control'}),
            'number_folio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el numero de folio'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingresa la descripción'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa el tiempo estimado'}),
            'date_start': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa fecha de inicio'}),
            'date_end': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa fecha de terminado'}),
            'scheduled_date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa fecha de programado'}),
            'staff': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Selecciona el personal asignado'}),
        }
