from django.contrib import admin
from .models import CategoriaProd, Fundacion, Producto, Contacto

# Register your models here.

admin.site.register(CategoriaProd)
admin.site.register(Producto)
admin.site.register(Contacto)
admin.site.register(Fundacion)


