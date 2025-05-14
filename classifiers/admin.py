
from django.contrib import admin

from classifiers.models import (
    Currency,
    Unit,
    RateVAT,
    CargoHazard,
    LegalType)


class CurrencyAdmin(admin.ModelAdmin):
    
    fields = [
        'name',
        ('code_dec', 'code_str')]
    
    list_display = [
        'code_dec',
        'code_str',
        'name']

    search_fields = [
        'code_str',
        'code_dec', 'name']
    
    ordering = ['name']

class UnitAdmin(admin.ModelAdmin):
    
    fields = [
        ('name', 'code_dec'),
        ('type', 'area_using'),
        ('notation_national', 'notation_international'),
        ('code_national', 'code_international')]
    
    list_display = [
        'code_dec',
        'name',
        'type',
        'area_using',
        'notation_national',
        'notation_international',
        'code_national',
        'code_international']
    
    search_fields = [
        'code_dec',
        'notation_national',
        'code_national',
        'name']
    
    ordering = [
        'area_using',
        'type',
        'code_dec']

class RateVATAdmin(admin.ModelAdmin):

    fields = [
        'repr',
        'code_str',
        'rate']
    
    list_display = [
        'code_str',
        'repr',
        'rate']
    
    search_fields = [
        'rate',
        'repr']
    
    ordering = ['rate']

class CargoHazardAdmin(admin.ModelAdmin):
    
    fields = [
        'code_str',
        'name']
    
    list_display = [
        'code_str',
        'name']
    
    search_fields = [
        'code_str',
        'name']
    
    ordering = ['code_str']

class LegalTypeAdmin(admin.ModelAdmin):
    
    fields = [
        'code_str',
        'name']
    
    list_display = [
        'code_str',
        'name']
    
    search_fields = [
        'code_str',
        'name']
    
    ordering = ['code_str']


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(RateVAT, RateVATAdmin)
admin.site.register(CargoHazard, CargoHazardAdmin)
admin.site.register(LegalType, LegalTypeAdmin)
