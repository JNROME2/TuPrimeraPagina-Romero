from django.urls import path
from tienda.views import inicio, sucursales, productos, clientes

urlpatterns = [
    path("inicio", inicio, name= "inicio"),
    path("sucursales", sucursales, name= "sucursales"),
    path("productos", productos, name= "productos"),
    path("clientes", clientes, name= "clientes"), 
]