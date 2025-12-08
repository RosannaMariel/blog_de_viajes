"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from .views import AgregarCategoria, AgregarPost, ActualizarPost, EliminarPost, ListarPost

app_name = "apps.posts"

urlpatterns = [
    path("agregar_categoria/", AgregarCategoria.as_view(), name='agregar_categoria'),
    path("agregar_post/", AgregarPost.as_view(), name="agregar_post"),
    path("actualizar_post/<int:pk>", ActualizarPost.as_view() , name="actualizar_post" ),
    path("eliminar_post/<int:pk>", EliminarPost.as_view(), name="eliminar post"),
    path("listar_posts/", ListarPost.as_view(), name="listar_posts"),
    path("listar_por_categoria/<str:categoria>", ListarPost.listar_post_por_categoria, name="listar_por_categoria"),
    path("ordenar_por", ListarPost.ordenar_por , name="ordenar_por"),
]
