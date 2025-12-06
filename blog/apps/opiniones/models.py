from django.db import models

# Create your models here.
class Opinion(models.Model):
    usuario = models.ForeignKey