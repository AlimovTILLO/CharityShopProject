# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-17 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ('-creation_date',), 'verbose_name': '\u041a\u043e\u0440\u0437\u0438\u043d\u0430', 'verbose_name_plural': '\u041a\u043e\u0440\u0437\u0438\u043d\u044b'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('cart',), 'verbose_name': '\u0422\u043e\u0432\u0430\u0440', 'verbose_name_plural': '\u0422\u043e\u0432\u0430\u0440\u044b'},
        ),
        migrations.AlterField(
            model_name='cart',
            name='checked_out',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd1\x80\xd0\xb5\xd0\xbd\xd0\xbe'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='creation_date',
            field=models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x81\xd0\xbe\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='item',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Cart', verbose_name=b'\xd0\x9a\xd0\xbe\xd1\x80\xd0\xb7\xd0\xb8\xd0\xbd\xd0\xb0'),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.PositiveIntegerField(verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe'),
        ),
    ]
