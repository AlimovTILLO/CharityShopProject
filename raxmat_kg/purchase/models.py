# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
import uuid
from item.models import Item
from django.contrib.auth.models import User
from django.db import models


class Purchase(models.Model):
    def __unicode__(self):
        return self.purchase_pin

    class Meta:
        db_table = "purchase"
        verbose_name = "Покупка"
        verbose_name_plural = "Покупки"

    purchase_user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchase_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    purchase_sales_date = models.DateTimeField(default=timezone.now)
    purchase_pin = models.TextField(default=uuid.uuid4().hex[:5])


class Account(models.Model):
    def __unicode__(self):
        return self.account_id

    class Meta:
        db_table = "account"
        verbose_name = "account"
        verbose_name_plural = "accounts"

    account_user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_data = models.CharField(max_length=50)


class Transaction(models.Model):
    def __unicode__(self):
        return self.transaction_id

    class Meta:
        db_table = "transaction"
        verbose_name = "transaction"
        verbose_name_plural = "transactions"

    transaction_from_account = models.ForeignKey(Account, on_delete=models.CASCADE)
#    transaction_to_account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(default=timezone.now)
    transaction_status = models.TextField(default=None)
