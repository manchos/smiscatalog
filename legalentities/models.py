# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class LegalEntities(models.Model):
    class Meta:
        db_table = "legalenti"
        verbose_name = 'Юридическое лицо'
        verbose_name_plural = 'Юридические лица'

    legalenti_name = models.TextField(verbose_name='название юр. лица')
    legalenti_address = models.TextField(verbose_name='адрес юр. лица', blank=True, null=True)
    # организационно правовая форма
    legalenti_opf = models.TextField(verbose_name='категория объекта', blank=True, null=True)
