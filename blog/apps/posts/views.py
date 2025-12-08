from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from apps.posts.models import Categoria, Post

# Create your views here.

# ----- Categoria -----
class AgregarCategoria(CreateView):
    model = Categoria
    fields = ["nombre"]
    template_name = "posts/agregar_categoria.html"
    success_url = reverse_lazy("index")

# ----- Posts -----
class AgregarPost(CreateView):
    model = Post
    fields = ['titulo', 'categoria', 'descripcion', 'imagen']
    template_name = "posts/agregar_post.html"
    success_url = reverse_lazy("index")

class ActualizarPost(UpdateView):
    model = Post
    fields = ['titulo', 'categoria', 'descripcion', 'imagen']
    template_name = "posts/agregar_post.html"
    success_url = reverse_lazy("index")

class EliminarPost(DeleteView):
    model = Post
    template_name = "posts/confirma_eliminar.html"
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
        query = self.request.GET('buscador')
        queryset = super().get_queryset()

       
        if query:
            queryset = queryset.filter(titulo_icontaihs = query )

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
        orden = request.GET.get('orden','')

        if orden == "fecha":
            posts = Post.objects.order_by('fecha_agregado')
        elif orden == "titulo":
            posts = Post.objects.order_by('titulo')
        else:
            posts = Post.objects.all()

        context ={
            "posts" : posts
        }
        template_name = "posts/listar_posts.html"

        return render(request, template_name, context)
    
    