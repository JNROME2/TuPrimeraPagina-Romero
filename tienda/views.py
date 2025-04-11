from django.shortcuts import render

def sucursales (request):
    return render(request, "tienda/sucursales.html")

def productos (request):
    return render(request, "tienda/productos.html")

def clientes (request):
    return render(request, "tienda/clientes.html")
