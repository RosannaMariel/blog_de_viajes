
from django.urls import path
from .views import acerca

app_name = 'acerca'

urlpatterns = [
    path('', acerca, name='acerca'),
]
