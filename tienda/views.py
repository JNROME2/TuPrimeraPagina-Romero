from django.shortcuts import render
from tienda.models import TiendaClientes, TiendaProductos, TiendaSucursales
from tienda.forms import TiendaClientesForm, TiendaProductosForm, TiendaSucursalesForm,TiendaInicioForm
from django.shortcuts import redirect

def sucursales (request):
    if request.method == "GET":
        print ("metodo fue GET")
        contexto = {"formulario": TiendaSucursalesForm()}
        return render(request, "tienda/sucursales.html", context=contexto)
    else:
        print("el metodo es POST")
        print(request.POST)

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
        print ("metodo fue GET")
        contexto = {"formulario": TiendaProductosForm()}
        return render(request, "tienda/productos.html", context=contexto)
    else:
        print("el metodo es POST")
        print(request.POST)

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
        print ("metodo fue GET")
        contexto = {"formulario": TiendaClientesForm()}
        return render(request, "tienda/clientes.html", context=contexto)
    else:
        print("el metodo es POST")
        print(request.POST)

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
        

               
            



