
from django.db import models

class Unit(models.Model):
    
    code_dec = models.CharField(
        max_length=4,
        default='',
        blank=False,
        unique=True,
        verbose_name='Код числовой'
    )
    name = models.CharField(
        max_length=100,
        default='',
        blank=False,
        verbose_name='Наименование'
    )
    notation_national = models.CharField(
        max_length=30,
        default='',
        blank=True,
        verbose_name='Условное обозначение (национальное)'
    )
    notation_international = models.CharField(
        max_length=30,
        default='',
        blank=True,
        verbose_name='Условное обозначение (международное)'
    )
    code_national = models.CharField(
        max_length=30,
        default='',
        blank=True,
        verbose_name='Код бквенный (национальный)'
    )
    code_international = models.CharField(
        max_length=30,
        default='',
        blank=True,
        verbose_name='Код бквенный (международный)'
    )
    repr = models.CharField(
        max_length=256,
        default='',
        blank=True,
        verbose_name='Единица измерения'
    )

    def save(self, *args, **kwargs):
        if self.notation_national:
            new_repr = f'{self.name} ({self.notation_national})'
        elif self.code_national:
            new_repr = f'{self.name} ({self.code_national})'
        elif self.notation_international:
            new_repr = f'{self.name} ({self.notation_international})'
        elif self.code_international:
            new_repr = f'{self.name} ({self.code_international})'
        else:
            new_repr = self.name
        if self.repr != new_repr:
            self.repr = new_repr
        super().save(*args, **kwargs)

    def __str__(self):
        return self.repr

    def __repr__(self):
        return self.repr

    class Meta:
        indexes = [
            models.Index(fields=['code_dec']),
            models.Index(fields=['notation_national'])
        ]
        ordering = ['id']
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерений'

