from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from ECycling.models import cliente, personalizacion
from ECycling.forms import ClienteForm 



def crea_clientes(request):
    if request.method=='GET':
        context ={
            'form': ClienteForm()
        }

        return render (request,'Clientes/create_clientes.html',context=context)
    elif request.method=='POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente.objects.create(
                cod_cliente=form.cleaned_data['cod_cliente'],
                nombre=form.cleaned_data['nombre'],
                apellido=form.cleaned_data['apellido'],
                direccion=form.cleaned_data['direccion'],
                localidad=form.cleaned_data['localidad'],
                cp=form.cleaned_data['cp'],
                telefono=form.cleaned_data['telefono'],
                email=form.cleaned_data['email'],
                )
            context={
                'message': 'El Clientes ha sido creado'

                }
            return render (request,'Clientes/create_clientes.html',context=context)
        else:
            context ={
                'form_errors': form.errors,
                'form':ClienteForm()
            }
            return render (request,'Clientes/create_clientes.html',context=context) 

class ClientesCreateView(CreateView):
    model= cliente
    template_name='Clientes/create_clientes.html'
    fields='__all__'
    success_url='../lista_clientes'

def actualiza_clientes(request, pk):
    cliente1 = cliente.objects.get(id=pk)
    
    if request.method=='GET':
        context ={
            'form': ClienteForm(
                initial={
                    'cod_cliente':cliente1.cod_cliente,
                    'nombre':cliente1.nombre,
                    'apellido':cliente1.apellido,
                    'direccion':cliente1.direccion,
                    'localidad':cliente1.localidad,
                    'cp':cliente1.cp,
                    'telefono':cliente1.telefono,
                    'email':cliente1.email,

                }
            )
        }

        return render (request,'Clientes/update_clientes.html',context=context)
    elif request.method=='POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            
                cliente1.cod_cliente=form.cleaned_data['cod_cliente']
                cliente1.nombre=form.cleaned_data['nombre']
                cliente1.apellido=form.cleaned_data['apellido']
                cliente1.direccion=form.cleaned_data['direccion']
                cliente1.localidad=form.cleaned_data['localidad']
                cliente1.cp=form.cleaned_data['cp']
                cliente1.telefono=form.cleaned_data['telefono']
                cliente1.email=form.cleaned_data['email']
                cliente1.save()
                context={
                'message': 'El Clientes ha sido actualizado'

                }
                return render (request,'Clientes/update_clientes.html',context=context)
        else:
            context ={
                'form_errors': form.errors,
                'form':ClienteForm()
            }
            return render (request,'Clientes/update_clientes.html',context=context)

def muestra_nosotros(request):
    return render (request, 'about_me.html', context={})  

def index(request):
    personalizaciones = personalizacion.objects.all()
    context={
            'personalizaciones':personalizaciones
        }
    print (context)    
    return render (request, 'index.html', context=context)   

def lista_clientes(request):
    print (request.GET)
    if 'search' in request.GET:
        search = request.GET['search']
        clientes = cliente.objects.filter(nombre__contains=search)
    else:
        clientes = cliente.objects.all()
    context={
        'clientes':clientes,
        }
    return render (request, 'Clientes/lista_clientes.html', context=context)


class ClienteListView(LoginRequiredMixin,ListView):
    model = cliente
    template_name= 'Clientes/lista_clientes.html'
  
  
class ClienteDeleteView(DeleteView):
    model=cliente
    template_name='Clientes/delete_clientes.html' 
    success_url='../lista_clientes'   

class ClienteUpdateView(UpdateView):
    model=cliente
    template_name='Clientes/update_clientes.html' 
    success_url='../lista_clientes' 
    fields='__all__' 














