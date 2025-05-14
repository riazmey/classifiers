
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save


class CargoHazard(models.Model):

    class Meta:
        indexes = [models.Index(fields=['code_str'])]
        ordering = ['code_str']
        verbose_name = 'Класс опасности груза'
        verbose_name_plural = 'Классификатор опасных грузов. ГОСТ Р 57478—2017'

    code_str = models.CharField(
        max_length = 10,
        default = '',
        blank = False,
        unique = True,
        verbose_name = 'Код (строковый)')

    name = models.CharField(
        max_length = 255,
        default = '',
        blank = False,
        unique = True,
        verbose_name = 'Наименование')

    repr = models.CharField(
        max_length = 300,
        default = '',
        blank = False,
        verbose_name = 'Класс опасности груза')

    def __str__(self):
        return self.repr

    def __repr__(self):
        return self.repr

@receiver(pre_save, sender=CargoHazard)
def update_repr(sender, instance: CargoHazard, **kwargs):
    new_repr = f'{instance.code_str} ({instance.name})'
    if instance.repr != new_repr:
        instance.repr = new_repr
