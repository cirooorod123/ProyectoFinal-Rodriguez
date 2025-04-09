from django.db import models


        





class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nombre

    

class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    precio_original = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    estrellas = models.PositiveIntegerField(default=0)  # de 0 a 5
    mostrar_estrellas = models.BooleanField(default=False)
    en_oferta = models.BooleanField(default=False)
    link = models.URLField(default="#")  

    def __str__(self) -> str:
        if self.categoria:
            return f"{self.categoria} - {self.nombre}"
        else:
            return self.nombre
        
    class Meta:
        unique_together = ("categoria", "nombre")

    @property
    def imagen_url(self):
        if self.imagen:
            return self.imagen.url
        return 'https://via.placeholder.com/450x300?text=Sin+Imagen'


