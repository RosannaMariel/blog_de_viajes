# Vistas basadas en clase

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"


# Vistas basadas en funciones
# from django.shortcuts import render    

# def index(request):
#     return render(request, "index.html")