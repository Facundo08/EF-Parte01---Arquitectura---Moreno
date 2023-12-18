from django.db import models


class Docente(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    fecha_nacimiento = models.DateField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido_paterno} {self.apellido_materno}'