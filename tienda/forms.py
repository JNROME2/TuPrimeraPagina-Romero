from django.forms import ModelForm

from tienda.models import TiendaSucursales, TiendaClientes, TiendaProductos, TiendaInicio

class TiendaSucursalesForm(ModelForm):
     class Meta:
        model = TiendaSucursales
        fields =["localidad","telefono"]

class TiendaClientesForm(ModelForm):
     class Meta: 
        model = TiendaClientes
        fields =["nombre","email","telefono"]

class TiendaProductosForm(ModelForm):
     class Meta:
        model = TiendaProductos
        fields =["nombre","codigo"]

class TiendaInicioForm(ModelForm):
      class Meta:
        model = TiendaInicio
        fields =["nombre"]
