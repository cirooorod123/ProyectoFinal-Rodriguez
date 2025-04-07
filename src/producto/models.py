from django.db import models



class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nombre
# Create your models here.
