"""fundao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static
import mapa.views as mapa_views

urlpatterns = [
  	url(r'^$', RedirectView.as_view(url='/mapa/')),
    url(r'^admin/', admin.site.urls,),
    url(r'^mapa/', mapa_views.index, name="index",),
    url(r'^dados_elementos/$', mapa_views.dados_elementos, name="dados_elementos",),
    url(r'^get_elementos/$', mapa_views.get_elementos, name="get_elementos",),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)