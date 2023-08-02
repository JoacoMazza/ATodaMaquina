from datetime import date

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path

from .forms import ClienteForm

# Create your views here.
from .models import Cliente, Sexo


def home(request):
    clientes_registros = Cliente.objects.all()
    contexto = {"clientes": clientes_registros}
    return render(request, "cliente/index.html", contexto)



class FormularioClienteViews(HttpRequest):

    def index(request):
        cliente = ClienteForm()
        return render(request, 'cliente/formulario.html', {'form': cliente})
    
    def proscesarform(request):
        cliente = ClienteForm(request.POST)
        if cliente.is_valid():
            cliente.save()
            cliente = ClienteForm()
            
        return render(request, 'cliente/formulario.html', {'form': cliente, 'mensaje': 'OK'})