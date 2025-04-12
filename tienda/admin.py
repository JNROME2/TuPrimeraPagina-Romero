from django.contrib import admin

from tienda.models import TiendaSucursales, TiendaClientes, TiendaProductos

admin.site.register(TiendaSucursales)
admin.site.register(TiendaClientes)
admin.site.register(TiendaProductos)
