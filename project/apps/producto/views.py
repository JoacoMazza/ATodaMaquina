from typing import Any

from django.contrib.auth.decorators import login_required

#! importaciones para login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from . import forms, models

def home(request):
    return render(request, "producto/index.html")


#class FormularioProductoViews(HttpRequest):

    def index(request):
        producto = ProductoForm()
        return render(request, 'producto/crear_producto.html', {'form': producto})
    
    def proscesarform(request):
        producto = ProductoForm(request.POST)
        if producto.is_valid():
            producto.save()
            producto = ProductoForm()
            
        return render(request, 'producto/crear_producto.html', {'form': producto, 'mensaje': 'OK'})


#Producto
#List
class Productolist(ListView):
    model = models.Producto

#Create
class Productocreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy('producto:producto_list')

#Detail
class Productodetail(DetailView):
    model = models.Producto

#Update
class Productoupdate(UpdateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy('producto:producto_list')

#Delete
class Productodelete(DeleteView):
    model = models.Producto
    success_url = reverse_lazy('producto:producto_list')
