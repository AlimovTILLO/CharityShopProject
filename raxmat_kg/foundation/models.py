from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Foundation(models.Model):
    class Meta:
        db_table = "foundation"

    foundation_name = models.CharField(max_length=200)
    foundation_description = models.TextField()
    foundation_logo = models.FileField(null=True, blank=True)
