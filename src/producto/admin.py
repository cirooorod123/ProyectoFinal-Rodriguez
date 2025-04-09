from django.contrib import admin
from .models import Categoria, Producto

admin.site.register(Categoria)





@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "en_oferta", "mostrar_estrellas")
    search_fields = ("nombre",)
    list_filter = ("en_oferta", "mostrar_estrellas")


# Register your models here.
