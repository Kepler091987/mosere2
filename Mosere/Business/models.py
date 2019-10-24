from django.db import models
from Clients.models import *

# Create your models here.
class Business(models.Model):
    client = models.OneToOneField(Clients, on_delete=models.CASCADE, verbose_name='Cliente')
    business_name = models.CharField(max_length=100, verbose_name='Razón Social')
    RFC = models.CharField(max_length=100, verbose_name='rfc')
    address = models.CharField(max_length=100, verbose_name='Dirección')
    state = models.CharField(max_length=100, verbose_name='Estado')
    code_postal = models.IntegerField(verbose_name='Codigo Postal')
    phone = models.BigIntegerField(verbose_name='Telefono')
    email = models.EmailField(max_length=70, blank=True, verbose_name='Correo')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['created_on']

    def __str__ (self):
        return self.business_name
