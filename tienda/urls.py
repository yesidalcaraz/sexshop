"""tienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from comercio import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.contrib.auth.decorators import login_required
from usuario.views import Login,logoutUsuario,RegistroUsuario
from comercio.views import Consultar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrar/',RegistroUsuario.as_view(),name='registrar'),
    path('accouts/login/',Login.as_view(),name='login'),
    path('logout/',login_required(logoutUsuario),name='logout'),

    path('comercio/', include(('comercio.urls', 'comercio'))),
    path('buscar/',views.busqueda, name = 'buscar'),
    path('',Consultar.as_view(), name = 'inicio'),
]
