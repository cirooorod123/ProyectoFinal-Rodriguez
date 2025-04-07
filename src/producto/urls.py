from django.urls import path

from . import views

app_name = "producto"

urlpatterns = [
    path("", views.index, name="index"),
    path("categoria/list/", views.categoria_list, name="categoria_list"),
    path("categoria/create/", views.categoria_create, name="categoria_create"),
    path("categoria/update/<int:pk>", views.categoria_update, name="categoria_update"),
    path("categoria/delete/<int:pk>", views.categoria_delete, name="categoria_delete"),
]

urlpatterns += [
    path("producto/list/", views.ProductoListView.as_view(), name="producto_list"),
    path("producto/create/", views.ProductoCreateView.as_view(), name="producto_create"),
    path("producto/update/<int:pk>", views.ProductoUpdateView.as_view(), name="producto_update"),
    path("producto/detail/<int:pk>", views.ProductoDetailView.as_view(), name="producto_detail"),
    path("producto/delete/<int:pk>", views.ProductoDeleteView.as_view(), name="producto_delete"),
]