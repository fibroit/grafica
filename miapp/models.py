from django.db import models

class Venta(models.Model):
    fecha = models.DateField()
    cantidad = models.IntegerField()
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre} - {self.fecha}"
