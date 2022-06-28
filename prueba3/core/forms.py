from pyexpat import model

from django import forms
from django.forms import ModelForm
from .models import Fundacion, Producto
from .models import Contacto

class ProductoForm(ModelForm):
    imagenProd = forms.ImageField(required=False)

    class Meta: 
        model = Producto
        fields = ['codProducto','nombreProducto', 'descripcion','stock', 'precio', 'categoria','imagenProd' ]


class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        #fields = ['codFormu','nombreF','apellidoF',' mailF','phoneF',' direccionF','regionF','comunaF']
        fields = "__all__"

class FundacionForm(ModelForm):
    imgFundacion = forms.ImageField(required=False)

    class Meta:
        model = Fundacion
        #fields ['nomFundacion', 'nomFundacion', 'descFundacion' , 'dirFundacion ', 'telFundacion', 'mailFundacion',','imgFundacion' ]
        fields = "__all__"