from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from apps.posts.models import Categoria, Post, Region, Pais
from apps.opiniones.models import Opinion
from apps.opiniones.forms import OpinionForm


# Create your views here.

# ----- Region -----
class AgregarRegion(CreateView):
    model = Region
    fields = ["nombre"]
    template_name = "posts/agregar_region.html"
    success_url = reverse_lazy("index")

# ----- Pais ------
class AgregarPais(CreateView):
    model = Pais
    fields = ["nombre"]
    template_name = "posts/agregar_pais.html"
    success_url = reverse_lazy("index")
# ----- Categoria -----
class AgregarCategoria(CreateView):
    model = Categoria
    fields = ["nombre"]
    template_name = "posts/agregar_categoria.html"
    success_url = reverse_lazy("index")

# ----- Posts -----
class AgregarPost(CreateView):
    model = Post
    fields = ['region', 'pais', 'categoria','titulo','descripcion', 'imagen']
    template_name = "posts/agregar_post.html"
    success_url = reverse_lazy("index")

class ActualizarPost(UpdateView):
    model = Post
    fields = ['region', 'pais', 'categoria','titulo','descripcion', 'imagen']
    template_name = "posts/agregar_post.html"
    success_url = reverse_lazy("index")

class EliminarPost(DeleteView):
    model = Post
    template_name = "genericos/confirma_eliminar.html"
    success_url = reverse_lazy("index")

class ListarPost(ListView):
    model = Post
    template_name = "posts/listar_posts.html"
    context_object_name = "posts"
    paginate_by = 3

    def get_context_data(self):
        context = super().get_context_data()
        categorias = Categoria.objects.all()
        context["categorias"] = categorias
        return context
    
    def get_queryset(self):
        query = self.request.GET.get('buscador')
        queryset = super().get_queryset()

       
        if query:
            queryset = queryset.filter(titulo__icontains = query )

        return queryset.order_by('titulo')
      
def listar_post_por_categoria(request, categoria):
    categoria_filtrada = Categoria.objects.filter(nombre = categoria)
    posts = Post.objects.filter(categoria = categoria_filtrada[0].id ).order_by('fecha_agregado')
    categorias = Categoria.objects.all()
    template_name = "posts/listar_posts.html"
    context = {
        'posts' : posts,
        'categorias' : categorias
    }
    return render(request, template_name, context)

def ordenar_por(request):
    orden = request.GET.get('orden','fecha_asc') # Default to fecha_asc

    if orden == "fecha_asc":
        posts = Post.objects.order_by('fecha_agregado')
    elif orden == "fecha_desc":
        posts = Post.objects.order_by('-fecha_agregado')
    elif orden == "titulo_asc":
        posts = Post.objects.order_by('titulo')
    elif orden == "titulo_desc":
        posts = Post.objects.order_by('-titulo')
    else:
        posts = Post.objects.all()

    context ={
        "posts" : posts,
        "orden_actual": orden
    }
    template_name = "posts/listar_posts.html"

    return render(request, template_name, context)

def leer_post(request, id):
    post = Post.objects.get(id = id)
    opiniones = Opinion.objects.filter(post = id)
    form = OpinionForm(request.POST)

    if form.is_valid():
        if request.user.is_authenticated:
            aux = form.save(commit=False)
            aux.post = post
            aux.usuario = request.user
            aux.save()
            form = OpinionForm()
        else:
            return redirect("apps.usuarios:iniciar_sesion")
    template_name = "posts/posts.html"
    context = {
        "post" : post,
        "form" : form,
        "opiniones" : opiniones
    }
    return render(request, template_name, context)
