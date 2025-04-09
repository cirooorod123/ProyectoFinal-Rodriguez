from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from . import models, forms
from .models import Producto


#def index(request):
#    return render(request, "producto/index.html")


def categoria_list(request):
    busqueda = request.GET.get("busqueda")
    if busqueda:
        queryset = models.Categoria.objects.filter(nombre__icontains=busqueda)
    else:
        queryset = models.Categoria.objects.all()
    context = {"object_list": queryset}
    return render(request, "producto/categoria_list.html", context)


def categoria_create(request):
    if request.method == "GET":
        form = forms.CategoriaForm()
    if request.method == "POST":
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto:categoria_list")
    return render(request, "producto/categoria_form.html", {"form": form})


def categoria_update(request, pk: int):
    query = models.Categoria.objects.get(id=pk)
    if request.method == "GET":
        form = forms.CategoriaForm(instance=query)
    if request.method == "POST":
        form = forms.CategoriaForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("producto:categoria_list")
    return render(request, "producto/categoria_form.html", {"form": form})


def categoria_delete(request, pk: int):
    query = models.Categoria.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("producto:categoria_list")
    return render(request, "producto/categoria_confirm_delete.html", {"object": query})


class ProductoListView(ListView):
    model = models.Producto

    def get_queryset(self):
        busqueda = self.request.GET.get("busqueda")
        if busqueda:
            queryset = models.Producto.objects.filter(nombre__icontains=busqueda)
        else:
            queryset = models.Producto.objects.all()
        return queryset


class ProductoCreateView(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")


class ProductoUpdateView(UpdateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")


class ProductoDetailView(DetailView):
    model = models.Producto


class ProductoDeleteView(DeleteView):
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")




def index(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, 'core/detalle.html', {'producto': producto})
