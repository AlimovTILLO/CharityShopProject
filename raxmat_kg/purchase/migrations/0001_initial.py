# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-13 05:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_sales_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('purchase_pin', models.TextField(default=b'2835d')),
                ('purchase_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.Item')),
                ('purchase_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'purchase',
                'verbose_name': '\u041f\u043e\u043a\u0443\u043f\u043a\u0430',
                'verbose_name_plural': '\u041f\u043e\u043a\u0443\u043f\u043a\u0438',
            },
        ),
    ]