from distutils.command.upload import upload
from doctest import register_optionflag
from pyexpat import model
from django.db import models
from asyncio.windows_events import NULL
from distutils.command.upload import upload
from tkinter.tix import INCREASING


# Create your models here.


class CategoriaProd(models.Model):
    idCategoria = models.AutoField(primary_key=True, verbose_name='Id de Categoria Proucto')
    nombreCategoria = models.CharField(max_length=50,verbose_name='Nombre de la categoria')

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    codProducto = models.AutoField(primary_key=True, verbose_name='Codigo Producto')
    nombreProducto = models.CharField(max_length=50, verbose_name="Nombre producto")
    descripcion = models.CharField(max_length=50, verbose_name="Descripccion Producto")
    stock = models.IntegerField(verbose_name="Cantidad Disponible")
    precio = models.IntegerField( verbose_name="Precio Producto")
    imagenProd = models.ImageField(upload_to='media/img/', null=True, blank=True)
    categoria = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)

    def __int__(self):
        return self.codProducto



class Contacto(models.Model):
    codFormu = models.AutoField(primary_key=True, verbose_name='Codigo Formulario')
    nombreF = models.CharField(max_length=50, verbose_name="Nombre ")
    apellidoF = models.CharField(max_length=50, verbose_name="Apellido")
    mailF = models.EmailField(verbose_name="Correo")
    phoneF = models.IntegerField( verbose_name="Teléfono")
    direccionF = models.CharField(max_length=250, null=True, blank=True, verbose_name="Dirección")
    regionF = models.CharField(max_length=250, verbose_name='Región de Cliente')
    comunaF = models.CharField(max_length=250, verbose_name='Comuna')

      
    
def __str__(self):
        return self.nombreF

class Fundacion(models.Model):
    codFundacion = models.AutoField(primary_key=True, verbose_name="Codigo Fundacion")
    nomFundacion = models.CharField(max_length=50,verbose_name="Nombre Fundacion")
    descFundacion = models.CharField(max_length=200, verbose_name="Descripcion Fundacion")
    dirFundacion = models.CharField(max_length=50,verbose_name="Direccion Fundacion")
    telFundacion = models.IntegerField(verbose_name="Telefono Contacto")
    mailFundacion = models.EmailField(verbose_name="Correo")
    imgFundacion = models.ImageField(upload_to='media/img/', null=True, blank=True)

    def __int__(self):
        return self.codFundacion
    
    