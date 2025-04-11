from django.shortcuts import render

def sucursales (request):
    return render(request, "tienda/sucursales.html")
