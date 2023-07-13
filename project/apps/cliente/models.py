from django.db import models

# Create your models here.
class Sexo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True)
    sexo_id = models.ForeignKey(Sexo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
