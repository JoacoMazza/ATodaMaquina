from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from . import views

app_name = "producto"

urlpatterns = [
    path('', home, name='home'),
    #path('crearproducto/', FormularioProductoViews.index, name='crearproducto'),
    #path('guardarproducto/', FormularioProductoViews.proscesarform, name='guardarproducto'),
    path("producto/list/", views.Productolist.as_view(), name="producto_list"),
    path("producto/create/", views.Productocreate.as_view(), name="producto_create"),
    path("producto/detail/<int:pk>", views.Productodetail.as_view(), name="producto_detail"),
    path("producto/update/<int:pk>", views.Productoupdate.as_view(), name="producto_update"),
    path("producto/delete/<int:pk>", views.Productodelete.as_view(), name="producto_delete"),
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
