from django import forms  
class IndumentariaForm (forms.Form):
    cod_indumentaria=forms.IntegerField ()
    tipo=forms.CharField(max_length=100) 
    genero=forms.CharField(max_length=100)
    nombre=forms.CharField(max_length=100)
    stock=forms.IntegerField ()
    precio=forms.FloatField () 

class BicicletaForm (forms.Form):
    tipo=forms.CharField(max_length=50)
    nombre=forms.CharField(max_length=60) 
    rodado=forms.IntegerField ()
    marca=forms.CharField(max_length=50)
    precio=forms.FloatField () 