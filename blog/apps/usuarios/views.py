from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from apps.usuarios.models import Usuario
from apps.usuarios.forms import RegistroUsuarioForm
# Create your views here.
class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = RegistroUsuarioForm
    template_name = "usuarios/registrar.html"
    success_url = reverse_lazy('index')