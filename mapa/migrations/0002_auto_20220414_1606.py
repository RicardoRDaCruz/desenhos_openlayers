# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-04-14 16:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mapa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='elemento',
            name='data',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='elemento',
            name='user',
            field=models.ForeignKey(default=1998, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
