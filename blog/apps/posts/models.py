from django.db import models


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=45)

    def __str__(self):
        return self.nombre
    


class Post(models.Model):
    titulo = models.CharField(max_length=100, null= False)
    descripcion = models.TextField()
    imagen = models.ImageField(null=True, blank=True, upload_to='posts',default='posts/posts_default.png')
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    fecha_agregado=models.DateTimeField(auto_now_add=True)
    deleted = False

    def __str__(self):
        return self.titulo