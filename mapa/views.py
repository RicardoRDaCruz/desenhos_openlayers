# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder

from .models import *

import json
import unicodedata


# Create your views here.

@login_required
def index(request):    
    return render(request, 'index.html')

@csrf_exempt
def dados_elementos(request):
    if request.is_ajax():
        request_data = request.POST

        dados_parsed = request_data.keys()[0].split(',"DIVISOR",')
        nome = eval(str(dados_parsed[0][1:]))        
        geometria = str(dados_parsed[1])        
        fill = str(dados_parsed[2])        
        stroke = str(dados_parsed[3])        
        font = str(dados_parsed[4])        
        type = str(dados_parsed[5])        
        raio = str(dados_parsed[6])
        centro = str(dados_parsed[7])
        function = eval(str(dados_parsed[8])[:3])
                

        novo_elemento = Elemento.objects.create(nome=nome,user=request.user,geometria=geometria,fill=fill,stroke=stroke,type=type,font=font,raio=raio, centro=centro,function=function)
        novo_elemento.save()
    
        return JsonResponse({'teste': 'deu certo'})

def get_elementos(request):

    elementos = Elemento.objects.all()
    
    elementos_json = serialize('json', elementos, cls=DjangoJSONEncoder)

    return JsonResponse(elementos_json, safe=False)