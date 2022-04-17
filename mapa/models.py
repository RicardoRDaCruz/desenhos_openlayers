# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

import json

class Elemento(models.Model):
    nome = models.CharField(max_length=512)
    user = models.ForeignKey(User)
    geometria = models.CharField(max_length=100000)
    data = models.DateField(auto_now_add=True, blank=True, null=True)
    fill = models.CharField(max_length=100)
    stroke = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    font = models.CharField(max_length=100000)
    raio = models.CharField(max_length=100000)
    centro = models.CharField(max_length=100000)
    function = models.CharField(max_length=100)

    def set_geoemtria(self, x):
        self.geometria = json.dumps(x)

    def get_geometria(self):
        return json.loads(self.geometria)

    def set_estilo(self, x):
        self.estilo = json.dumps(x)

    def get_estilo(self):
        return json.loads(self.estilo)