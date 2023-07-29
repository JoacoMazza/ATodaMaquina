from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import ProductoForm
from .models import Producto
def home(request):
    productos_registros = Producto.objects.all()
    contexto = {"productos": productos_registros}
    return render(request, "producto/index.html", contexto)


class FormularioProductoViews(HttpRequest):

    def index(request):
        producto = ProductoForm()
        return render(request, 'producto/crear_producto.html', {'form': producto})
    
    def proscesarform(request):
        producto = ProductoForm(request.POST)
        if producto.is_valid():
            producto.save()
            producto = ProductoForm()
            
        return render(request, 'producto/crear_producto.html', {'form': producto, 'mensaje': 'OK'})

def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('producto/index.html')
    else:
        form = ProductoForm()
    return render(request, 'producto/crear_producto.html', {'form': form})
