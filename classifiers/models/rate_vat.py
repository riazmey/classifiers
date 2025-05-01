
from django.db import models

class RateVAT(models.Model):

    class Meta:
        
        indexes = [
            models.Index(fields=['code_str']),
            models.Index(fields=['rate']),
            models.Index(fields=['repr'])]
        
        ordering = ['rate']
        verbose_name = 'Ставка НДС'
        verbose_name_plural = 'Ставки НДС'

    code_str = models.CharField(
        max_length = 20,
        default = '',
        blank = False,
        unique = True,
        verbose_name = 'Код (строковый)')

    rate = models.IntegerField(
        default = 0,
        blank = True,
        verbose_name = 'Ставка')

    repr = models.CharField(
        max_length = 255,
        default = '',
        blank = False,
        verbose_name = 'Ставки НДС')

    def __str__(self):
        return self.repr

    def __repr__(self):
        return self.repr
