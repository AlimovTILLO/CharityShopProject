# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-27 10:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0007_auto_20160527_0506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='item_text',
            new_name='item_description',
        ),
    ]