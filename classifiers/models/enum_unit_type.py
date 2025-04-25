
from django.db import models

class EnumUnitType(models.Model):

    class Meta:
        indexes = [
            models.Index(fields=['code_str'])
        ]
        ordering = ['code_str']
        verbose_name = 'Тип единицы измерения'
        verbose_name_plural = 'Типы единицы измерений'

    code_str = models.CharField(
        max_length=20,
        default='',
        blank=False,
        unique=True,
        verbose_name='Код (строковый)'
    )

    repr = models.CharField(
        max_length=255,
        default='',
        blank=False,
        verbose_name='Тип единицы измерения'
    )

    def __str__(self):
        return self.repr

    def __repr__(self):
        return self.repr
