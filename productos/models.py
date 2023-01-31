from django.db import models

# Create your models here.
class indumentaria(models.Model):
    cod_indumentaria=models.IntegerField (null=False, default=0)
    tipo=models.CharField(max_length=100,null=True) 
    genero=models.CharField(max_length=100,null=True)
    nombre=models.CharField(max_length=100,null=True)
    stock=models.IntegerField (null=False,default=0)
    precio=models.FloatField (null=False,default=0)
    imagen=models.ImageField (upload_to='producto_image',null=True, blank=True)


class bicicletas(models.Model):
    tipo=models.CharField(max_length=50,null=False)
    nombre=models.CharField(max_length=60,null=False)
    rodado=models.IntegerField(null=False,default=0)
    marca=models.CharField(max_length=50,null=True)
    precio=models.FloatField (null=False,default=0)

