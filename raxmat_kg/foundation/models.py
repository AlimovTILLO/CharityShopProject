# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
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
