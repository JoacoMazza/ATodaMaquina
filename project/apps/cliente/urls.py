from django.urls import path

from .views import *

app_name = "cliente"

urlpatterns = [
    path("", home, name="home"),
    path('crear_clientes/', crear_clientes, name="crear_clientes"),
    path('busqueda/', busqueda, name="busqueda"),
    path('registrarformulario/', FormularioClienteViews.index, name='registrarFormulario'),
    path('guardarformulario/', FormularioClienteViews.proscesarform, name='guardarformulario'),
]

