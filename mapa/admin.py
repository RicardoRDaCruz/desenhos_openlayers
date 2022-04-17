# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *

from django.contrib import admin


@admin.register(Elemento)
class ElementoAdmin(admin.ModelAdmin):
	list_display = ('nome', 'data', 'user')

