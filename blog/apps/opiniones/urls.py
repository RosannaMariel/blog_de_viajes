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

from apps.opiniones.views import EliminarOpinion, ModificarOpinion, agregar_opinion, listar_opiniones

app_name = "apps.opiniones"

urlpatterns = [
    path("agregar_opinion/", agregar_opinion, name="agregar_opinion"),
    path("opiniones/", listar_opiniones, name="opiniones"),
    path("modificar_opinion/<int:pk>", ModificarOpinion.as_view(), name="modificar_opinion"),
    path("eliminar_opinion/<int:pk>", EliminarOpinion.as_view(), name="eliminar_opinion")
]
