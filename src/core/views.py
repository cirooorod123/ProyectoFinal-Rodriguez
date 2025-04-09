
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import LoginForm, RegisterForm
from producto.models import Producto




def index(request):
    query = request.GET.get('q')  
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        productos = Producto.objects.all()
    return render(request, 'core/index.html', {
        'productos': productos,
        'query': query,  # esto es útil si querés mostrar el término buscado
    })

def about(request):
    return render(request, "core/about.html")


class MiLoginView(LoginView):
    template_name = "core/login.html"
    authentication_form = LoginForm
    next_page = reverse_lazy("core:index")

    def form_valid(self, form):
        usuario = form.get_user()
        messages.success(self.request, f"Inicio de sesión exitoso. ¡Bienvenido {usuario.username}!")
        return super().form_valid(form)


class MiRegisterView(CreateView):
    form_class = RegisterForm
    template_name = "core/register.html"
    success_url = reverse_lazy("core:login")

    def form_valid(self, form):
        messages.success(self.request, "Registro exitoso. Ahora puedes iniciar sesión")
        return super().form_valid(form)


