from rest_framework import serializers
from core.models import Producto
from core.models import Fundacion

class ProductoSerializers (serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['codProducto','nombreProducto', 'descripcion','stock', 'precio','categoria', 'imagenProd']

class FundacionSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Fundacion
        fields = ['nomFundacion', 'nomFundacion', 'descFundacion' , 'dirFundacion ', 'telFundacion', 'mailFundacion','imgFundacion' ]
                