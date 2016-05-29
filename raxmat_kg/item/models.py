# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from foundation.models import Foundation


class MainCategory(models.Model):
    class Meta:
        db_table = "main_category"

    main_category_name = models.CharField(max_length=50)


class ItemCategory(models.Model):
    class Meta:
        db_table = "item_category"

    item_category_name = models.CharField(max_length=50)
    item_category_main_id = models.ForeignKey(MainCategory, on_delete=models.SET_NULL, blank=True, null=True)


class Item(models.Model):
    class Meta:
        db_table = 'item'

    item_title = models.CharField(max_length=200)
    item_image = models.FileField(null=True, blank=True)
    item_description = models.TextField()
    item_price = models.IntegerField(default=0)
    item_foundation_id = models.ForeignKey(Foundation, on_delete=models.SET_NULL, blank=True, null=True)
    item_charity = models.IntegerField(default=0)
    item_date = models.DateTimeField()
    item_likes = models.IntegerField(default=0)
    item_category_id = models.ForeignKey(ItemCategory, on_delete=models.SET_NULL, blank=True, null=True)


class Comments(models.Model):
    class Meta:
        db_table = "comments"

    comments_date = models.DateTimeField()
    comments_text = models.TextField(verbose_name="Текст коментария")
    comments_item = models.ForeignKey(Item, on_delete=models.SET_NULL, blank=True, null=True)
    comments_from = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
