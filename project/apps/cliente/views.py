from datetime import date
from django.views.generic import DeleteView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required

from .forms import ClienteForm
from . import models

# Create your views here.
from .models import Cliente, Sexo

@staff_member_required
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
    
#Delete
class Clientedelete(DeleteView):
    model = models.Cliente
    success_url = reverse_lazy('cliente:home')