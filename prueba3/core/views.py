from core.forms import ProductoForm 
from core.forms import FundacionForm
from core.forms import UsuarioForm
from .models import Producto, Contacto , Fundacion, Usuario
from django.shortcuts import render, redirect  
from distutils.command.upload import upload
from asyncio.windows_events import NULL
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import ContactoForm

# Create your views here.

# Vistas Secciones 
def index(request):
    return render(request, 'core/inicio.html')

def inicio(request):
    return render(request, 'core/index.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def login(request):
    return render(request, 'core/login.html')
    

def tienda(request):
    
    Productos = Producto.objects.all()

    data={
        'productos':Productos
    }

    return render(request, 'core/tienda.html', data)

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "formulario enviado"
        else:
            data["form"] = formulario

    return render(request, 'core/contacto.html', data)

def donaciones(request):
    fundaciones = Fundacion.objects.all()

    data={
        'fundaciones':fundaciones
    }



    return render(request, 'core/donaciones.html', data)

def registrarse(request):
    context = { 
        'form': UsuarioForm()
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            context["mensaje"]= "Usuario creado exitosamente"
        else:
            context["form"] = formulario 

    return render(request, 'core/registrarse.html', context)

#VISTAS DE ADMINISTRADOR PRODUCTOS  

def administrador(request):
    productos = Producto.objects.all()
    #producto.imagenProd = request.FILE.get('txtImagen')
    fundaciones = Fundacion.objects.all()
    

    datos = {
        'productos' : productos
            }
    return render(request, 'core/administrador.html', datos )


#VISTAS PRODUCTO

def agregar_prod(request):
    productoForm = ProductoForm( )
    datos = {
        'form' : productoForm
    }

    if request.method == 'POST':
        
        formulario = ProductoForm(request.POST, request.FILES)

        if formulario.is_valid:
            
            formulario.save()

            datos['mensaje'] = "El producto ha sido agregado correctamente!"
        
            return render(request, "core/agregar_prod.html", datos)

    return render(request, "core/agregar_prod.html", datos)



def modificar_prod(request, id):
    producto = Producto.objects.get(codProducto = id)

    datos = {
        'form':ProductoForm(instance= producto )
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto)

        if formulario.is_valid:
             formulario.save()
             datos['mensaje'] = 'Producto Modificado Correctamente'
    
    return render(request, 'core/modificar_prod.html', datos)

def eliminar_prod(request, id):
    producto = Producto.objects.get(codProducto = id)

    producto.delete()

    return redirect(to=administrador)


#VISTA LISTA DE PERSONAS QUE COMPLETAN EL FORMULARIO
def lista_personas(request):
    contacto = Contacto.objects.all()
    contexto = {'contactos': contacto}
    return render(request, 'core/lista_personas.html', contexto)


###     VISTA DE FUNDACION   ####

def admin_fund(request):
    fundaciones = Fundacion.objects.all()
    #producto.imagenProd = request.FILE.get('txtImagen')
    
    data = {
        'fundaciones' : fundaciones
            }
    return render(request, 'core/admin_fund.html', data)

def agregar_fundacion(request):
    fundacionForm = FundacionForm( )
    data = {
        'form' : fundacionForm
    }

    if request.method == 'POST':
        
        formulario = FundacionForm(request.POST, request.FILES)
        if formulario.is_valid:
            formulario.save()
            data['mensaje'] = "La fundaci??n ha sido agregado correctamente!"
        
            return render(request, "core/agregar_fundacion.html", data)

    return render(request, "core/agregar_fundacion.html", data)


def modificar_fundacion(request, id):
    fundacion = Fundacion.objects.get(codFundacion = id)

    data = {
        'form':FundacionForm(instance= fundacion )
    }

    if request.method == 'POST':
        formulario = FundacionForm(request.POST, request.FILES ,instance=fundacion)

        if formulario.is_valid:
             formulario.save()
             data['mensaje'] = 'Fundacion Modificada Correctamente'
    
    return render(request, 'core/modificar_fundacion.html', data)

def eliminar_fundacion(request, id):
    fundacion = Fundacion.objects.get(codFundacion = id)

    fundacion.delete()

    return redirect(to=admin_fund)