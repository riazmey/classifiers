
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save

from .enum_unit_type import EnumUnitType
from .enum_unit_area_using import EnumUnitAreaUsing


class Unit(models.Model):
    
    class Meta:

        indexes = [
            models.Index(fields=['code_dec']),
            models.Index(fields=['type']),
            models.Index(fields=['area_using']),
            models.Index(fields=['type', 'area_using']),
            models.Index(fields=['notation_national']),
            models.Index(fields=['notation_international'])]
        
        ordering = ['id']
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Общероссийский классификатор единиц измерения (ОКЕИ)'

    code_dec = models.CharField(
        max_length = 4,
        default = '',
        blank = False,
        unique = True,
        verbose_name = 'Код числовой')

    name = models.CharField(
        max_length = 100,
        default = '',
        blank = False,
        verbose_name = 'Наименование')

    type = models.ForeignKey(
        EnumUnitType,
        on_delete = models.PROTECT,
        blank = False,
        verbose_name = 'Тип измерения')

    area_using = models.ForeignKey(
        EnumUnitAreaUsing,
        on_delete = models.PROTECT,
        blank = False,
        verbose_name = 'Регион использования')

    notation_national = models.CharField(
        max_length = 30,
        default = '',
        blank = True,
        verbose_name = 'Условное обозначение (национальное)')

    notation_international = models.CharField(
        max_length = 30,
        default = '',
        blank = True,
        verbose_name = 'Условное обозначение (международное)')

    code_national = models.CharField(
        max_length = 30,
        default = '',
        blank = True,
        verbose_name = 'Код буквенный (национальный)')

    code_international = models.CharField(
        max_length = 30,
        default = '',
        blank = True,
        verbose_name = 'Код буквенный (международный)')

    repr = models.CharField(
        max_length = 256,
        default = '',
        blank = True,
        verbose_name = 'Единица измерения')

    def __str__(self):
        return self.repr

    def __repr__(self):
        return self.repr

@receiver(pre_save, sender=Unit)
def update_repr(sender, instance: Unit, **kwargs):
    if instance.notation_national:
        new_repr = f'{instance.name} ({instance.notation_national})'
    elif instance.code_national:
        new_repr = f'{instance.name} ({instance.code_national})'
    elif instance.notation_international:
        new_repr = f'{instance.name} ({instance.notation_international})'
    elif instance.code_international:
        new_repr = f'{instance.name} ({instance.code_international})'
    else:
        new_repr = instance.name
    if instance.repr != new_repr:
        instance.repr = new_repr
