from django.urls import path
from tienda.views import sucursales

urlpatterns = [
    path("sucursales", sucursales, name= "sucursales")
]