from urllib import request
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Fundacion, Producto
from .serializers import FundacionSerializer, ProductoSerializers

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_productos(request):
    """
    GET = lista todos los productos
    POST = Agrega registro
    """
    
    if request.method == 'GET':
        Producto = Producto.objects.all()
        serializer = ProductoSerializers(Producto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def lista_fundacion(request):
    """
    GET = lista todos los productos
    POST = Agrega registro
    """
    
    if request.method == 'GET':
        Fundacion = Fundacion.objects.all()
        serializer = FundacionSerializer(Producto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FundacionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)