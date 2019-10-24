from django.db import models

# Create your models here.
class Clients(models.Model):
    name = models.CharField(max_length=40, verbose_name='Nombre')
    first_name = models.CharField(max_length=40, verbose_name='Apellido Paterno')
    last_name = models.CharField(max_length=40, verbose_name='Apellido Materno')
    created_on = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['created_on']

    def __str__ (self):
        chain = self.name + " " + self.first_name + " " + self.last_name
        return chain


class Phones(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, null=True, verbose_name='Cliente')
    phone = models.BigIntegerField(verbose_name='Telefono')
    created_on = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = 'Telefono'
        verbose_name_plural = 'Telefonos'
        ordering = ['created_on']

    def __str__(self):
        return self.phone


class Emails(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, null=True, verbose_name='Cliente')
    email = models.EmailField(verbose_name='Email')
    created_on = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = 'Correo'
        verbose_name_plural = 'Correos'
        ordering = ['created_on']

    def __str__(self):
        return self.email

class customersAddress(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, null=True, verbose_name='Cliente')
    street = models.CharField(max_length=250, verbose_name='Calle')
    number = models.IntegerField(verbose_name='Numero')
    suburb = models.CharField(max_length=50, verbose_name='Colonia')
    city = models.CharField(max_length=50, verbose_name='Ciudad')
    state = models.CharField(max_length=50, verbose_name='Estado')
    code_postal = models.IntegerField(verbose_name='Codigo Postal')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Direccion de Cliente'
        verbose_name_plural = 'Direcciones de Clientes'
        ordering = ['created_on']

    def __str__ (self):
        return self.street

class fiscalData(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, null=True, verbose_name='Cliente')
    rfc = models.CharField(max_length=40)
    address = models.CharField(max_length=100, verbose_name='Dirección')
    state = models.CharField(max_length=40, verbose_name='Estado')
    code_postal = models.IntegerField(verbose_name='Codigo Postal')
    phone = models.BigIntegerField(verbose_name='Telefono')
    email = models.EmailField(max_length=70, blank=True, verbose_name='Correo')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Datos fiscales'
        verbose_name_plural = 'Datos Fiscales'
        ordering = ['created_on']

    def __str__(self):
        return self.rfc

