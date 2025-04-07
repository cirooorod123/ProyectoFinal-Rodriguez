from django.db import models



class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nombre
    

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True, blank=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self) -> str:
        if self.categoria:
            return f"{self.categoria} - {self.nombre}"
        else:
            return self.nombre

    class Meta:
        unique_together = ("categoria", "nombre")
        



