from django.db import models
from Clients.models import *
from Staff.models import *

# Create your models here.

class Jobs(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name='cliente')
    number_folio = models.CharField(max_length=100, verbose_name='Numero de Folio')
    description = models.TextField(max_length=500, verbose_name='Descripción')
    time = models.TimeField(verbose_name='Tiempo aproximado')
    date_start = models.DateTimeField(verbose_name='Fecha de inicio')
    date_end = models.DateTimeField(verbose_name='Fecha de termino')
    scheduled_date = models.DateTimeField(verbose_name='Fecha programada')
    staff = models.ManyToManyField(Staff, on_delete=models.CASCADE, verbose_name='Personal')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Trabajo'
        verbose_name_plural = 'Trabajos'
        ordering = ['created_on']

    def __str__ (self):
        return self.number_folio