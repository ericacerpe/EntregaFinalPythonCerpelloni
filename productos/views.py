from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from productos.models import indumentaria
from productos.models import bicicletas
from productos.forms import IndumentariaForm
from productos.forms import BicicletaForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView,DeleteView,UpdateView

""" def crea_indumentaria(request):
    if request.method=='GET':
        context ={
            'form': IndumentariaForm()
        }

        return render (request,'Productos/create_indumentaria.html',context=context)
    elif request.method=='POST':
        form = IndumentariaForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            indumentaria = IndumentariaForm.save(commit=False)
            indumentaria.cod_indumentaria=form.cleaned_data.get('cod_indumentaria')
            indumentaria.tipo=form.cleaned_data.get('tipo')
            indumentaria.genero=form.cleaned_data.get('genero')
            indumentaria.nombre=form.cleaned_data.get('nombre')
            indumentaria.stock=form.cleaned_data.get('stock')
            indumentaria. precio=form.cleaned_data.get('precio')
            indumentaria.imagen=form.cleaned_data.get('imagen')
            indumentaria.save() 
            return redirect('lista_indumentaria')
          
                
    context={
                'errors':form.errors,
                'form':IndumentariaForm ()       

                }
    return render (request,'Productos/create_indumentaria.html',context=context)
                   
         
 """
class IndumentariaCreateView(CreateView):
    model= indumentaria
    template_name='Productos/create_indumentaria.html'
    fields='__all__'
    success_url='../lista_indumentaria'

def lista_indumentaria(request):
    print (request.GET)
    if 'search' in request.GET:
        search = request.GET['search']
        indumentarias = indumentaria.objects.filter(nombre__contains=search)
    else:
        indumentarias = indumentaria.objects.all()
    context={
        'indumentarias':indumentarias,
        }
    return render (request, 'Productos/lista_indumentaria.html', context=context)

class BicicetasCreateView(CreateView):
    model= bicicletas
    template_name='Productos/create_bicicleta.html'
    fields='__all__'
    success_url='../lista_bicicleta'


def crea_bicicletas(request):
    if request.method=='GET':
        context ={
            'form': BicicletaForm()
        }

        return render (request,'Productos/create_bicicleta.html',context=context)
    elif request.method=='POST':
        form = BicicletaForm(request.POST)
        if form.is_valid():
            bicicletas.objects.create(
                tipo=form.cleaned_data['tipo'],
                nombre=form.cleaned_data['nombre'], 
                rodado=form.cleaned_data['rodado'],
                marca=form.cleaned_data['marca'],
                precio=form.cleaned_data['precio'], 
                )
            context={
                'message': 'La bicicleta ha sido creada'

                }
            return render (request,'Productos/create_bicicleta.html',context=context)
        else:
            context ={
                'form_errors': form.errors,
                'form':BicicletaForm()
            }
            return render (request,'Productos/create_bicicleta.html',context=context)   
   
def lista_bicicleta(request):
    
    if 'search' in request.GET:
        search = request.GET['search']
        bicicletas1 = bicicletas.objects.filter(nombre__contains=search)
    else:
        bicicletas1 = bicicletas.objects.all()
    context={
        'bicicletas':bicicletas1,
        }
    return render (request, 'Productos/lista_bicicletas.html', context=context)
    
def index(request):
    return render (request, 'index.html', context={})   
class IndumentariaUpdateView(UpdateView):
    model=indumentaria
    template_name='Productos/update_indumentaria.html' 
    success_url='../lista_indumentaria' 
    fields='__all__' 

class IndumentariaDeleteView(DeleteView):
    model=indumentaria
    template_name='Productos/delete_indumentaria.html' 
    success_url='../lista_indumentaria'  

class BicicletaUpdateView(UpdateView):
    model=bicicletas
    template_name='Productos/update_bicicletas.html' 
    success_url='../lista_bicicleta' 
    fields='__all__' 

class BicicletaDeleteView(DeleteView):
    model=    model=bicicletas
    template_name='Productos/delete_bicicletas.html' 
    success_url='../lista_bicicleta'  