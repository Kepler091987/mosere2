from django.contrib import admin
from .models import Staff

# Register your models here.
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'email', 'entry_date', 'market_stall', 'Rol', 'created_on')

admin.site.register(Staff, StaffAdmin)