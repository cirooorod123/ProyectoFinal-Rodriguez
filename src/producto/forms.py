from django import forms

from . import models


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        fields = "__all__"


class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = "__all__"

