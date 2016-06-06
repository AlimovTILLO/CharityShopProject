# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-31 08:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0014_auto_20160530_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charity_percent', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'charity',
                'verbose_name': '\u041f\u0440\u043e\u0446\u0435\u043d\u0442 \u0431\u043b\u0430\u0433\u043e\u0442\u0432\u043e\u0440\u0438\u0442\u0435\u043b\u043d\u043e\u0441\u0442\u0438',
                'verbose_name_plural': '\u041f\u0440\u043e\u0446\u0435\u043d\u0442\u044b \u0431\u043b\u0430\u0433\u043e\u0442\u0432\u043e\u0440\u0438\u0442\u0435\u043b\u043d\u043e\u0441\u0442\u0435\u0439',
            },
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442', 'verbose_name_plural': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': '\u0422\u043e\u0432\u0430\u0440', 'verbose_name_plural': '\u0422\u043e\u0432\u0430\u0440\u044b'},
        ),
        migrations.AlterModelOptions(
            name='itemcategory',
            options={'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0442\u043e\u0432\u0430\u0440\u0430', 'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438 \u0442\u043e\u0432\u0430\u0440\u043e\u0432'},
        ),
        migrations.AlterModelOptions(
            name='maincategory',
            options={'verbose_name': '\u0413\u043b\u0430\u0432\u043d\u0430\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f', 'verbose_name_plural': '\u0413\u043b\u0430\u0432\u043d\u044b\u0435 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'},
        ),
        migrations.RemoveField(
            model_name='item',
            name='item_charity',
        ),
        migrations.AddField(
            model_name='item',
            name='item_charity_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='item.Charity'),
        ),
    ]