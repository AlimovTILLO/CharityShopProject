# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from foundation.models import Foundation


class MainCategory(models.Model):
    def __unicode__(self):
        return self.main_category_name

    class Meta:
        db_table = "main_category"
        verbose_name = "Главная категория"
        verbose_name_plural = "Главные категории"

    main_category_name = models.CharField(max_length=50)


class ItemCategory(models.Model):
    def __unicode__(self):
        return self.item_category_name

    class Meta:
        db_table = "item_category"
        verbose_name = "Категория товара"
        verbose_name_plural = "Категории товаров"

    item_category_name = models.CharField(max_length=50)
    item_category_main = models.ForeignKey(MainCategory, on_delete=models.SET_NULL, blank=True, null=True)


class Charity(models.Model):
    def __unicode__(self):
        return self.charity_percent

    class Meta:
        db_table = "charity"
        verbose_name = "Процент благотворителности"
        verbose_name_plural = "Проценты благотворителностей"

    charity_percent = models.CharField(max_length=3, verbose_name="Процент для благотворителности")


class Item(models.Model):
    def __unicode__(self):
        return self.item_title

    class Meta:
        db_table = 'item'
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    item_title = models.CharField(max_length=200, verbose_name="Названия товара")
    item_image = models.FileField(null=True, blank=True)
    item_description = models.TextField()
    item_price = models.DecimalField(max_digits=18, decimal_places=2)
    item_date = models.DateTimeField()
    item_likes = models.IntegerField(default=0)
    item_foundation = models.ForeignKey(Foundation, on_delete=models.SET_NULL, blank=True, null=True)
    item_charity = models.ForeignKey(Charity, blank=True, null=True)
    item_category = models.ForeignKey(ItemCategory, on_delete=models.SET_NULL, blank=True, null=True)


class Comments(models.Model):
    class Meta:
        db_table = "comments"
        verbose_name = "Коммент"
        verbose_name_plural = "Комментарии"

    comments_date = models.DateTimeField(default=timezone.now)
    comments_text = models.TextField(verbose_name="Текст коментария")
    comments_item = models.ForeignKey(Item, on_delete=models.SET_NULL, blank=True, null=True)
    comments_from = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
