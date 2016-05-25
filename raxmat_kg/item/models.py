# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Item(models.Model):
    class Meta:
        db_table = 'item'

    item_title = models.CharField(max_length=200)
    item_image = models.ImageField()
    item_text = models.TextField()
    item_date = models.DateTimeField()
    item_likes = models.IntegerField(default=0)

class Comments(models.Model):
    class Meta():
     db_table = "comments"

    comments_date = models.DateTimeField()
    comments_text = models.TextField(verbose_name="Текст коментария")
    comments_item = models.ForeignKey(Item)
    comments_from = models.ForeignKey(User)

