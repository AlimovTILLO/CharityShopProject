# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class FoundationCategory(models.Model):
    def __unicode__(self):
        return self.foundation_category_name

    class Meta:
        db_table = "foundation_category"
        verbose_name = "Категория фонда"
        verbose_name_plural = "Категории Фондов"

    foundation_category_name = models.CharField(max_length=50)


class Foundation(models.Model):
    def __unicode__(self):
        return self.foundation_name

    class Meta:
        db_table = "foundation"
        verbose_name = "Фонд"
        verbose_name_plural = "Фонды"

    foundation_name = models.CharField(max_length=200)
    foundation_description = models.TextField()
    foundation_logo = models.FileField(null=True, blank=True)
    foundation_status = models.CharField(max_length=50, null=True)
    foundation_category = models.ForeignKey(FoundationCategory, on_delete=models.SET_NULL, blank=True, null=True)
    foundation_url = models.URLField(verbose_name="Ссылка", null=True)
