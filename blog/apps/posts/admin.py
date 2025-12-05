

from django.contrib import admin
from apps.posts.models import Categoria, Post


# Register your models here.

admin.site.register(Categoria)
admin.site.register(Post)