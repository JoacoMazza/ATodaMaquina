from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

app_name = "producto"

urlpatterns = [
    path('', home, name='home'),
    path('crearproducto/', FormularioProductoViews.index, name='crearproducto'),
    path('guardarproducto/', FormularioProductoViews.proscesarform, name='guardarproducto'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
