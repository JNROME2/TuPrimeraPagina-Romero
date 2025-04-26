from django.urls import path
from tienda.views import (inicio, 
                          sucursales, 
                          productos, 
                          clientes, 
                          about,
                          home,
                          TiendaCreateView, 
                          TiendaListView, 
                          TiendaDetailView, 
                          TiendaUpdateView,
                          TiendaDeleteView
)

app_name = 'tienda' 

urlpatterns = [
    path("", home, name= "home" ),
    path("tienda/inicio", inicio, name= "inicio"),
    path("tienda/sucursales", sucursales, name= "sucursales"),
    path("tienda/productos", productos, name= "productos"),
    path("tienda/clientes", clientes, name= "clientes"), 
    path("tienda/about", about, name= "about"), 
    path('tienda/cbv/alta-producto/', TiendaCreateView.as_view(), name='cbv-alta-producto'),
    path("tienda/cbv/lista-producto/", TiendaListView.as_view(), name="cbv-lista-producto"),
    path("tienda/cbv/producto/<int:pk>", TiendaDetailView.as_view(), name="cbv-producto-detail"),
    path("tienda/cbv/producto/<int:pk>/update/>", TiendaUpdateView.as_view(), name="cbv-producto-update"),
    path("tienda/cbv/producto/<int:pk>/delete/>", TiendaDeleteView.as_view(), name="cbv-producto-delete"),
    ]