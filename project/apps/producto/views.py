from typing import Any
from .models import Producto
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
    productos_registros = Producto.objects.all()
    contexto = {"productos": productos_registros}
    return render(request, "producto/index.html", contexto)

#Producto


#List
class Productolist(LoginRequiredMixin, ListView):
    model = models.Producto
    login_url = '../../../login'
    redirect_field_name = 'redirect_to'

    def get_queryset(self) -> QuerySet[Any]:
        if self.request.GET.get("consulta"):
            consulta = self.request.GET.get("consulta")
            object_list = models.Producto.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Producto.objects.all()
        return object_list

#Create
class Productocreate(LoginRequiredMixin, CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy('producto:producto_list')
    login_url = '../../../login'
    redirect_field_name = 'redirect_to'

#Detail
class Productodetail(LoginRequiredMixin, DetailView):
    model = models.Producto
    login_url = '../../../login'
    redirect_field_name = 'redirect_to'

#Update
class Productoupdate(LoginRequiredMixin, UpdateView):
    model = models.Producto
    login_url = '../../../login'
    redirect_field_name = 'redirect_to'
    form_class = forms.ProductoForm
    success_url = reverse_lazy('producto:producto_list')

#Delete
class Productodelete(LoginRequiredMixin, DeleteView):
    model = models.Producto
    login_url = '../../../login'
    redirect_field_name = 'redirect_to'
    success_url = reverse_lazy('producto:producto_list')
