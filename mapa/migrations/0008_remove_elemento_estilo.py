# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-04-15 16:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapa', '0007_auto_20220414_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elemento',
            name='estilo',
        ),
    ]
