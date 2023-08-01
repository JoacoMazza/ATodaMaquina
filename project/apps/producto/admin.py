from django.contrib import admin
from . import models

admin.site.site_title = 'Productos'

@admin.register(models.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'precio',
        'descripcion',
        'fecha_actualizacion',
        'imagen' 
        )
    list_display_links = ('nombre',)
    search_fields = ('nombre',)
    ordering = (
        'precio',
        'nombre'
    )
    list_filter = ('nombre',)
    date_hierarchy = 'fecha_actualizacion'
