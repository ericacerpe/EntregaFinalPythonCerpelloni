from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User
from users.models import UserProfile
from django import forms

class registerform(UserCreationForm):
    first_name = forms.CharField(max_length=100,required=True)
    last_name = forms.CharField(max_length=100,required=True)
    class Meta:
        model = User
        fields =['username','first_name','last_name','email','password1','password2']

class userupdateform(forms.ModelForm):
    username = forms.CharField(max_length=100,required=True)
    first_name = forms.CharField(max_length=100,required=True)
    last_name = forms.CharField(max_length=100,required=True)
    class Meta:
        model = User
        fields =['username','first_name','last_name']

class userprofilefom(forms.ModelForm):
    class Meta:
        model= UserProfile
        fields =['telefono','fecha_nacimiento','foto_perfil']



