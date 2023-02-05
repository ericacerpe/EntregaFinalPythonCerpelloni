from django.db import models

# Create your models here.
class cliente(models.Model):
    cod_cliente=models.IntegerField (null=False, default=0)
    nombre=models.CharField(max_length=100,null=True)
    apellido=models.CharField (max_length=100,null=True)
    direccion=models.CharField(max_length=100,null=True)
    localidad=models.CharField(max_length=100,null=True)
    cp=models.IntegerField(null=True)
    telefono=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)

class personalizacion(models.Model):
    titulo=models.CharField(max_length=100,null=True)
    imagen_portada=models.ImageField  (upload_to='imagen_portada',null=True, blank=True)
   