# -*- coding: utf-8 -*-
from django.db import models


class SmisObj(models.Model):
    class Meta:
        db_table = "smisobj"
        verbose_name = 'СМИС объект'
        verbose_name_plural = 'СМИС объекты'

    """
    description
    """
    # smiskontragent_id = models.PositiveSmallIntegerField()
    smisobj_name = models.TextField(verbose_name='название объекта')
    smisobj_address = models.TextField(verbose_name='адрес объекта', blank=True, null=True)
    smisobj_category = models.TextField(verbose_name='категория объекта', blank=True, null=True)
    # smis_datecreate = models.DateTimeField(verbose_name='дата создания ТУ', blank=True, null=True)


    # def __unicode__(self):
    # def __str__(self):
    #     return self.smisobj_name


