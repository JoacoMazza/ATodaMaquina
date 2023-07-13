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
    # return render(request, "index.html", {"clientes": clientes_registros})
    return render(request, "cliente/index.html", contexto)


def crear_clientes(request):
    from datetime import date

    p1 = Sexo(nombre="Hombre")
    p2 = Sexo(nombre="Mujer")
    p3 = Sexo(nombre="Prefiero no Mencionarlo")

    p1.save()
    p2.save()
    p3.save()

    c1 = Cliente(nombre="Almendra", apellido="Ruiseñor",
                 nacimiento=date(2015, 1, 1), sexo_id=p1)
    c2 = Cliente(nombre="Giordana", apellido="Tapello",
                 nacimiento=date(2005, 2, 2), sexo_id=p2)
    c3 = Cliente(nombre="Macarena", apellido="Lito",
                 nacimiento=date(1990, 1, 1), sexo_id=p3)
    c4 = Cliente(nombre="Jhiordana", apellido="Perez",
                 nacimiento=date(2005, 1, 1), sexo_id=None)

    c1.save()
    c2.save()
    c3.save()
    c4.save()
    return redirect("cliente:home")

def busqueda(request: HttpRequest) -> HttpResponse:
    # Búsqueda por nombre que contenga "dana"
    cliente_nombre = Cliente.objects.filter(nombre__contains="dana")

    # Nacimientos  mayores a 2000
    cliente_nacimiento = Cliente.objects.filter(
        nacimiento__gt=date(2000, 1, 1))

    # País de origen vacío
    cliente_pais = Cliente.objects.filter(Sexo_id=None)

    contexto = {
        "clientes_nombre": cliente_nombre,
        "clientes_nacimiento": cliente_nacimiento,
        "clientes_pais": cliente_pais
    }
    return render(request, "cliente/search.html", contexto)

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