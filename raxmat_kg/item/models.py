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

    main_category_name = models.CharField(max_length=50, verbose_name="Главная категория")


class ItemCategory(models.Model):
    def __unicode__(self):
        return self.item_category_name

    class Meta:
        db_table = "item_category"
        verbose_name = "Категория товара"
        verbose_name_plural = "Категории товаров"

    item_category_name = models.CharField(max_length=50, verbose_name="Категория")
    item_category_main = models.ForeignKey(MainCategory, on_delete=models.CASCADE, verbose_name="Главная категория")

    def __unicode__(self):
        return self.item_category_name


class Charity(models.Model):
    def __unicode__(self):
        return self.charity_percent

    class Meta:
        db_table = "charity"
        verbose_name = "Процент благотворителности"
        verbose_name_plural = "Проценты благотворителностей"

    charity_percent = models.CharField(max_length=3, verbose_name="Процент для благотворителности")


class ItemManager(models.Manager):
    def all(self):
        return self.get_queryset().item_active()


class Item(models.Model):
    def __unicode__(self):
        return self.item_title

    class Meta:
        db_table = 'item'
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    item_title = models.CharField(max_length=200, verbose_name="Названия")
    item_image = models.FileField(null=True, blank=True, verbose_name="Изображение")
    item_description = models.TextField(verbose_name="Описание товара")
    item_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name="Цена")
    item_date = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    item_likes = models.IntegerField(default=0, verbose_name="Рейтинг товара")
    item_foundation = models.ForeignKey(Foundation, on_delete=models.CASCADE, verbose_name="Выбирите Фонд")
    item_charity = models.ForeignKey(Charity, on_delete=models.CASCADE, verbose_name="Процент для благотворителностей")
    item_category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, verbose_name="Выбирите категорию")
    item_active = models.BooleanField(default=True, verbose_name="Активный")
    item_quantity = models.IntegerField(default=1, verbose_name="Количество")


class Comments(models.Model):
    class Meta:
        db_table = "comments"
        verbose_name = "Коммент"
        verbose_name_plural = "Комментарии"

    comments_date = models.DateTimeField(default=timezone.now)
    comments_text = models.TextField(verbose_name="Текст коментария")
    comments_item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name="Комментарий товара")
    comments_from = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь комментария")
