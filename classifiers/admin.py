
from django.contrib import admin
from .models import Currency
from .models import Unit

class CurrencyAdmin(admin.ModelAdmin):
    fields = ['name', ('code_dec', 'code_str')]
    list_display = ['code_dec', 'code_str', 'name']
    search_fields = ['code_str', 'code_dec', 'name']
    ordering = ['name']

class UnitAdmin(admin.ModelAdmin):
    fields = [('name', 'code_dec'), ('notation_national', 'notation_international'), ('code_national', 'code_international')]
    list_display = ['code_dec', 'name', 'notation_national', 'notation_international', 'code_national', 'code_international']
    search_fields = ['code_dec', 'notation_national', 'code_national', 'name']
    ordering = ['id']

admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Unit, UnitAdmin)
