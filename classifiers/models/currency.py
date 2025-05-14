
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save


class Currency(models.Model):
    
    class Meta:
        indexes = [
            models.Index(fields=['code_dec']),
            models.Index(fields=['code_str'])
        ]
        ordering = ['code_str']
        verbose_name = 'Валюта'
        verbose_name_plural = 'Общероссийский классификатор валют (ОКВ)'

    code_dec = models.CharField(
        max_length = 3,
        default = '',
        blank = False,
        unique = True,
        verbose_name = 'Код (числовой)')
    
    code_str = models.CharField(
        max_length = 3,
        default = '',
        blank = False,
        unique = True,
        verbose_name = 'Код (строковый)')
    
    name = models.CharField(
        max_length = 50,
        default = '',
        blank = False,
        verbose_name = 'Имя')
    
    repr = models.CharField(
        max_length = 256,
        default = '',
        blank = True,
        verbose_name = 'Валюта')

    def __str__(self):
        return self.repr

    def __repr__(self):
        return self.repr

@receiver(pre_save, sender=Currency)
def update_repr(sender, instance: Currency, **kwargs):
    new_repr = f'{instance.code_str} ({instance.name})'
    if instance.repr != new_repr:
        instance.repr = new_repr
