from productos.models import indumentaria , bicicletas
from django import forms  



""" class IndumentariaForm (forms.Form):
    cod_indumentaria=forms.IntegerField ()
    tipo=forms.CharField(max_length=100) 
    genero=forms.CharField(max_length=100)
    nombre=forms.CharField(max_length=100)
    stock=forms.IntegerField ()
    precio=forms.FloatField () 
    imagen=forms.ImageField () """

class IndumentariaForm (forms.ModelForm):
    class Meta:
        model = indumentaria
        fields=['cod_indumentaria','tipo','genero','nombre','stock','precio','imagen']

""" class BicicletaForm (forms.Form):
    tipo=forms.CharField(max_length=50)
    nombre=forms.CharField(max_length=60) 
    rodado=forms.IntegerField ()
    marca=forms.CharField(max_length=50)
    precio=forms.FloatField ()  """
class BicicletaForm (forms.ModelForm):
    class Meta:
        model =bicicletas
        fields=['tipo','nombre','rodado','marca','precio','descuento','imagen']