from xml.etree.ElementInclude import include
from django.urls import path
from .views import lista_productos

urlpatterns = [
    path('lista_productos', lista_productos, name="lista_productos"),
    #path('', include('core.urls')),
    #path('api/', include('rest_producto.urls')),
]


