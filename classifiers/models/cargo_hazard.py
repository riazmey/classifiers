
from django.db import models

class CargoHazard(models.Model):

    class Meta:
        indexes = [
            models.Index(fields=['code_str'])
        ]
        ordering = ['code_str']
        verbose_name = 'Класс опасности груза'
        verbose_name_plural = 'Классы опасности грузов'

    code_str = models.CharField(
        max_length=10,
        default='',
        blank=False,
        unique=True,
        verbose_name='Код'
    )

    name = models.CharField(
        max_length=255,
        default='',
        blank=False,
        unique=True,
        verbose_name='Наименование'
    )

    repr = models.CharField(
        max_length=300,
        default='',
        blank=False,
        verbose_name='Класс опасности груза'
    )

    def __str__(self):
        return self.repr

    def __repr__(self):
        return self.repr

    def save(self, *args, **kwargs):
        new_repr = f'Класс №{self.code_str}. {self.name}    '
        if self.repr != new_repr:
            self.repr = new_repr
        super().save(*args, **kwargs)