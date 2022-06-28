from django.urls import path 
from .views import eliminar_prod, index,nosotros, tienda, contacto, donaciones, administrador,agregar_prod,modificar_prod,lista_personas, agregar_fundacion, admin_fund,modificar_fundacion,eliminar_fundacion 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index,name="index"),
    path('nosotros', nosotros,name="nosotros"),
    path('tienda', tienda,name="tienda"),
    path('contacto', contacto,name="contacto"),
    path('donaciones', donaciones,name="donaciones"),
    path('administrador', administrador,name="administrador"),
    path('agregar_prod', agregar_prod,name="agregar_prod"),
    path('modificar_prod', modificar_prod,name="modificar_prod"),
    path('eliminar_prod', eliminar_prod,name="eliminar_prod"),
    path('lista_personas', lista_personas,name="lista_personas"),
    path('agregar_fundacion', agregar_fundacion,name="agregar_fundacion"),
    path('admin_fund',admin_fund,name="admin_fund"),
    path('modificar_fundacion',modificar_fundacion,name="modificar_fundacion"),
    path('eliminar_fundacion',eliminar_fundacion ,name="eliminar_fundacion "),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)