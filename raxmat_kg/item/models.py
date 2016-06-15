# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# from django.db.models.signals import post_save
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
    item_category_main = models.ForeignKey(MainCategory, on_delete=models.CASCADE)

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


# class ItemQuerySet(models.query.QuerySet):
#    def item_active(self):
#        return self.filter(item_active=True)


class ItemManager(models.Manager):
    # def get_queryset(self):
    #    return ItemQuerySet(self.model, using=self._db)

    # def all(self, *args, **kwargs):
    #    return self.get_queryset().item_active()
    def all(self):
        return self.get_queryset().item_active()


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
    item_date = models.DateTimeField(default=timezone.now)
    item_likes = models.IntegerField(default=0)
    item_foundation = models.ForeignKey(Foundation, on_delete=models.CASCADE)
    item_charity = models.ForeignKey(Charity, on_delete=models.CASCADE)
    item_category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    item_active = models.BooleanField(default=True)
    item_quantity = models.IntegerField(default=1)


class Comments(models.Model):
    class Meta:
        db_table = "comments"
        verbose_name = "Коммент"
        verbose_name_plural = "Комментарии"

    comments_date = models.DateTimeField(default=timezone.now)
    comments_text = models.TextField(verbose_name="Текст коментария")
    comments_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    comments_from = models.ForeignKey(User, on_delete=models.CASCADE)

# class Variation(models.Model):
#    variation_item_name = models.ForeignKey(Item)
#    variation_item_title = models.CharField(max_length=120)
#    variation_item_price = models.DecimalField(max_digits=18, decimal_places=2)
#   variation_item_sale_price = models.DecimalField(max_digits=18, decimal_places=2, null=True, blank=True)
#    variation_item_active = models.BooleanField(default=True)
#    variation_item_inventory = models.IntegerField(null=True, blank=True)

#    def __unicode__(self):
#        return self.variation_item_title

#    def get_price(self):
#        if self.variation_item_sale_price is not None:
#            return self.variation_item_sale_price
#        else:
#            return self.variation_item_price


# def item_post_saved_receiver(sender, instance, created, *args, **kwargs):
#    variation_item_name = instance
#    variations = variation_item_name.variation_set.all()
#    if variations.count() == 0:
#        new_var = Variation()
#        new_var.variation_item_name = variation_item_name
#        new_var.variation_item_title = "Default"
#        new_var.variation_item_price = variation_item_name.variation_item_price
#        new_var.save()


# post_save.connect(item_post_saved_receiver, sender=Item)
