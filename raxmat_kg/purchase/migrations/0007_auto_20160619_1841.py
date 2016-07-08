# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-19 12:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('purchase', '0006_auto_20160619_1839'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercheckout',
            name='user',
        ),
        migrations.AddField(
            model_name='usercheckout',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]