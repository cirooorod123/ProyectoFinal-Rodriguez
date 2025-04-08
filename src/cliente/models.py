from django.db import models
 

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15, blank=True, null=True)
    nacimiento = models.DateField()
    barrio = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Create your models here.
