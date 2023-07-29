from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = ['fecha_actualizacion']
        fields = ('nombre', 'precio', 'descripcion', 'imagen')