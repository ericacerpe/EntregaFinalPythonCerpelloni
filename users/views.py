

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from users.form import registerform, userupdateform
from django.contrib.auth.models import User


def login_view(request):

    if request.method == 'GET':
        form = AuthenticationForm()
        context ={
            'form':form
        }
        return render (request, 'Users/login.html', context=context)
    elif request.method =='POST':
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate (username=username, password=password)
            print (user)
            if user is not None:
                login(request,user)
                context={
                    'message':f'{username} - Se ha regisntrado con exito'
                }
                return render(request, 'index.html', context=context)

    form = AuthenticationForm()
    context ={
            'form':form,
            'errors':'Ususario o contraseña invalida'
        }        
    return render (request, 'Users/login.html', context=context)


def register(request):
    if  request.method == 'GET':
        form =registerform()
        context ={
            'form': form
        }
        return render (request, 'Users/register.html', context=context)
    elif request.method =='POST':
         form =registerform(request.POST)
         if form.is_valid():
                form.save()
                return redirect('login')    
         context ={
            'errors':form.errors,
            'form':registerform()
        }           
         return render (request, 'Users/register.html', context=context)    

@login_required
def update_user(request):
    user = request.user
    if  request.method == 'GET':
        form =userupdateform(initial ={
            'username':user.username,
            'firt_name':user.first_name,
            'last_name':user.last_name    
        })
        context ={
            'form': form
        }
        return render (request, 'Users/update_user.html', context=context)
    elif request.method =='POST':
         form =userupdateform(request.POST)
         if form.is_valid():
                user.username=form.cleaned_data.get('username')
                user.firt_name=form.cleaned_data.get('firt_name')
                user.last_name=form.cleaned_data.get('last_name')
                user.save()
                return redirect('index')    
         context ={
            'errors':form.errors,
            'form':userupdateform()
        }           
         return render (request, 'Users/update_user.html', context=context)        