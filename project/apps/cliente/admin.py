from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Cliente, Sexo

admin.site.register(Cliente)
admin.site.register(Sexo)
