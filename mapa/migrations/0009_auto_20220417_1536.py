# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-04-17 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapa', '0008_remove_elemento_estilo'),
    ]

    operations = [
        migrations.AddField(
            model_name='elemento',
            name='centro',
            field=models.CharField(default='', max_length=100000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='elemento',
            name='raio',
            field=models.CharField(default='', max_length=100000),
            preserve_default=False,
        ),
    ]