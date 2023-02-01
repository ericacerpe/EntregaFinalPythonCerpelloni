from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    telefono = models.CharField(max_length=25,null=True,blank=True)
    fecha_nacimiento=models.DateField(null=True,blank=True)
    foto_perfil= models.ImageField(upload_to='fotos_perfil',null=True,blank=True)

def __str__(self):
    return f"{self.user} - {self.foto_perfil}"
