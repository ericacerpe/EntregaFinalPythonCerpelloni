from django import forms    

class ClienteForm (forms.Form):
    cod_cliente=forms.IntegerField (required=True)
    nombre=forms.CharField(max_length=100)
    apellido=forms.CharField (max_length=100,)
    direccion=forms.CharField(max_length=100)
    localidad=forms.CharField(max_length=100)
    cp=forms.IntegerField()
    telefono=forms.CharField(max_length=100)
    email=forms.CharField(max_length=100)

