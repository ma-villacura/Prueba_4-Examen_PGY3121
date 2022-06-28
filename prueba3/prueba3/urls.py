"""prueba3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from xml.etree.ElementInclude import include
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from core.views import index, nosotros, tienda, contacto, donaciones, administrador, agregar_prod, modificar_prod, eliminar_prod,lista_personas,agregar_fundacion, admin_fund,modificar_fundacion,eliminar_fundacion 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('index.html', index, name="index"),
    path('nosotros.html', nosotros,name="nosotros"),
    path('tienda.html', tienda,name="tienda"),
    path('contacto.html', contacto,name="contacto"),
    path('donaciones.html', donaciones,name="donaciones"),
    path('administrador.html', administrador,name="administrador"),
    path('agregar_prod.html', agregar_prod,name="agregar_prod"),
    path('modificar_prod/<id>', modificar_prod,name="modificar_prod"),
    path('eliminar_prod/<id>', eliminar_prod,name="eliminar_prod"),
    path('api/',include('rest_producto.urls')),
    path('lista_personas', lista_personas, name='lista_personas'),
    path('agregar_fundacion',agregar_fundacion,name="agregar_fundacion"),
    path('admin_fund',admin_fund,name="admin_fund"),
    path('modificar_fundacion/<id>',modificar_fundacion,name="modificar_fundacion"),
    path('eliminar_fundacion /<id>',eliminar_fundacion ,name="eliminar_fundacion "),
]

