from django.shortcuts import render
from tienda.models import TiendaClientes, TiendaProductos, TiendaSucursales
from tienda.forms import TiendaClientesForm, TiendaProductosForm, TiendaSucursalesForm,TiendaInicioForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

def sucursales (request):
    if request.method == "GET":        
        contexto = {"formulario": TiendaSucursalesForm()}
        return render(request, "tienda/sucursales.html", context=contexto)
    else:

        formulario = TiendaSucursalesForm(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            modelo_sucursales = TiendaSucursales(
                localidad= datos["localidad"],
                telefono= datos["telefono"],
            )
            modelo_sucursales.save()  
            return redirect ("sucursales")

    

def productos (request):
    if request.method == "GET":
        contexto = {"formulario": TiendaProductosForm()}
        return render(request, "tienda/productos.html", context=contexto)
    else:
        
        formulario = TiendaProductosForm(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            modelo_productos = TiendaProductos(
                nombre= datos["nombre"],
                codigo= datos["codigo"],
            )
            modelo_productos.save()  
            return redirect ("productos")



def clientes (request):
    if request.method == "GET":
        
        contexto = {"formulario": TiendaClientesForm()}
        return render(request, "tienda/clientes.html", context=contexto)
    else:
       

        formulario = TiendaClientesForm(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            modelo_clientes = TiendaClientes(
                nombre=datos["nombre"],
                email= datos["email"],
                telefono= datos["telefono"],
            )
            modelo_clientes.save()  
            return redirect ("clientes")
        
def inicio (request):
    if request.method == "GET":
        contexto = {"formulario": TiendaInicioForm()}
        return render(request, "tienda/inicio.html", context=contexto)
    else:
        formulario = TiendaInicioForm(request.POST)
        
        if formulario.is_valid():
            nombre = formulario.cleaned_data["nombre"]
            
            productos = TiendaProductos.objects.filter(nombre__icontains=nombre)
            
            contexto={
                "productos": productos,
            }
 
            return render(request, "tienda/detail.html", context=contexto)
        
        contexto = {"formulario": TiendaInicioForm()}
        return render(request, "tienda/inicio.html", context=contexto)
    
def about(request):
    return render(request, "tienda/about.html") 

def home(request):
    return render(request,"tienda/home.html")
        
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from django.urls import reverse_lazy

class TiendaCreateView(LoginRequiredMixin, CreateView):
    model= TiendaProductos
    fields= ["nombre","codigo"]
    template_name= "tienda/cbv/alta-producto.html"
    success_url= reverse_lazy ("tienda:cbv-lista-producto")

class TiendaListView(LoginRequiredMixin,ListView):
    model= TiendaProductos
    template_name="tienda/cbv/lista-producto.html"
    context_object_name=("productos")

class TiendaDetailView(LoginRequiredMixin,DetailView):
    model= TiendaProductos
    template_name="tienda/cbv/producto-detail.html"
    context_object_name = 'producto'
   
class TiendaUpdateView(LoginRequiredMixin, UpdateView):
    model= TiendaProductos
    fields=["nombre","codigo"]
    template_name="tienda/cbv/producto-update.html"
    success_url= reverse_lazy ("tienda:cbv-lista-producto")

class TiendaDeleteView(LoginRequiredMixin,DeleteView):
    model= TiendaProductos
    template_name="tienda/cbv/producto-delete.html"
    success_url= reverse_lazy ("tienda:cbv-lista-producto")

               
            



