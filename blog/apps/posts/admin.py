

from django.contrib import admin
from apps.posts.models import Categoria, Post
from .models import Region
from .models import Pais

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Post)
admin.site.register(Region)
admin.site.register(Pais)
