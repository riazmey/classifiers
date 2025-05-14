
from django.db import models


class LegalType(models.Model):

    class Meta:

        indexes = [
            models.Index(fields=['code_str']),
            models.Index(fields=['name'])]

        ordering = ['code_str']
        verbose_name = 'Организационно-правовая форма'
        verbose_name_plural = 'Общероссийский классификатор организационно-правовых форм (ОКОПФ)'

    code_str = models.CharField(
        max_length = 8,
        default = '',
        blank = False,
        unique = True,
        verbose_name = 'Код (строковый)')

    name = models.CharField(
        max_length = 256,
        default = '',
        blank = True,
        verbose_name = 'Наименование')

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
