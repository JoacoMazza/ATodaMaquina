from django.urls import path
from . import views
from .views import *

app_name = "cliente"

urlpatterns = [
    path("", home, name="home"),
    path('registrarformulario/', FormularioClienteViews.index, name='registrarFormulario'),
    path('guardarformulario/', FormularioClienteViews.proscesarform, name='guardarformulario'),
    path("cliente/delete/<int:pk>", views.Clientedelete.as_view(), name="cliente_delete"),
]

