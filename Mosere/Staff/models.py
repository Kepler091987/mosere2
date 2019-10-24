from django.db import models
from django.contrib.auth.models import User

# Create your models here.
ROLES = {
    ('ING', 'Ingeniero'),
    ('INS', 'Instalador'),
    ('ADM', 'Administrador'),
        }

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuario')
    name = models.CharField(max_length=100, verbose_name='Nombre Completo')
    phone = models.BigIntegerField(verbose_name='Telefono')
    email = models.EmailField(verbose_name='Correo')
    entry_date = models.DateField(verbose_name='Fecha de ingreso')
    market_stall = models.CharField(max_length=3, choices=ROLES, verbose_name='Puesto')
    Rol = models.CharField(max_length=3, choices=ROLES, verbose_name='Rol')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personal'
        ordering = ['created_on']

    def __str__ (self):
        return self.name