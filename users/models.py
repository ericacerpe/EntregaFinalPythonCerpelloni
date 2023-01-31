from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profie')
    telefono = models.CharField(max_length=25,null=True,blank=True)
    fecha_nacimiento=models.DateField(null=True,blank=True)
    foto_perfil= models.ImageField(upload_to='perfil_imagenes',null=True,blank=True)

