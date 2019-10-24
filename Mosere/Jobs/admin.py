from django.contrib import admin
from Jobs.models import *

# Register your models here.
class JobsAdmin(admin.ModelAdmin):
    list_display = ('client', 'number_folio', 'description', 'time', 'date_start', 'date_end', 'scheduled_date', 'staff')

admin.site.register(Jobs, JobsAdmin)