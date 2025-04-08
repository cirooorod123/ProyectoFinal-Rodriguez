from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Cliente)

@admin.register(models.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "email", "telefono")
    search_fields = ("nombre", "apellido")
    list_filter = ("barrio",)
    ordering = ("apellido", "nombre")
    date_hierarchy = "nacimiento"
