from django.db import models

from apps.usuarios.models import Usuario
from apps.posts.models import Post

# Create your models here.
class Opinion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    texto = models.TextField(verbose_name="Opinion")
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto
    
    class Meta:
        ordering = ["-fecha",]
