from django.urls import path

from .views import *

app_name = "cliente"

urlpatterns = [
    path("", home, name="home"),
    path('registrarformulario/', FormularioClienteViews.index, name='registrarFormulario'),
    path('guardarformulario/', FormularioClienteViews.proscesarform, name='guardarformulario'),
]

