from django.urls import path
from tienda.views import sucursales, productos, clientes

urlpatterns = [
    path("sucursales", sucursales, name= "sucursales"),
    path("productos", productos, name= "productos"),
    path("clientes", clientes, name= "clientes"),
]