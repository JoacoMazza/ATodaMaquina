from django.db import models
from django.utils import timezone

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=250, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(default=timezone.now, editable=False, verbose_name='fecha de actualizacion')
    imagen = models.ImageField(upload_to='productos', blank=True, null=True)

    def __str__(self):
        return self.nombre