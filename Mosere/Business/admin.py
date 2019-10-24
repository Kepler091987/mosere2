from django.contrib import admin
from .models import Business

# Register your models here.
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('client', 'business_name', 'RFC', 'address', 'state', 'code_postal', 'phone', 'email', 'created_on')

admin.site.register(Business, BusinessAdmin)