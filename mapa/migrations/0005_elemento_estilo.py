# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-04-14 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapa', '0004_auto_20220414_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='elemento',
            name='estilo',
            field=models.CharField(default='', max_length=5000),
            preserve_default=False,
        ),
    ]
