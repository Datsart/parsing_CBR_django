from django.contrib import admin
from .models import CbrPars
# Register your models here.

class CbrParsAdmin(admin.ModelAdmin):
    list_display = ('name', 'charcode', 'value')

admin.site.register(CbrPars, CbrParsAdmin)