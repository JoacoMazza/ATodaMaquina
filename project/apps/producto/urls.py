from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from . import views
from django.contrib.auth.decorators import login_required



app_name = "producto"

urlpatterns = [
    path('', home, name='home'),
    path("producto/list/", views.Productolist.as_view(), name="producto_list"),
    path("producto/create/", views.Productocreate.as_view(), name="producto_create"),
    path("producto/detail/<int:pk>", views.Productodetail.as_view(), name="producto_detail"),
    path("producto/update/<int:pk>", views.Productoupdate.as_view(), name="producto_update"),
    path("producto/delete/<int:pk>", views.Productodelete.as_view(), name="producto_delete"),
    #url(r'^workers/$', login_required( views.RootWorkerView.as_view())),
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
