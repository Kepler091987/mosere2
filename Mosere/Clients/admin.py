from django.contrib import admin
from .models import *

# Register your models here.
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'first_name', 'last_name')

admin.site.register(Clients, ClientsAdmin)
admin.site.register(fiscalData)
admin.site.register(customersAddress)
