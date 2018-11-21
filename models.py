from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Persona(models.Model):
    username = models.CharField(max_length=200, verbose_name="Username")
    password = models.CharField(max_length=200, verbose_name="password")
    tipo = models.CharField(max_length=200, verbose_name="tipo")
    email = models.EmailField()

    
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    #link = models.URLField(verbose_name="Dirección Web", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "anuncios"
        verbose_name_plural = "anuncios"
        ordering = ('title',)

    def __str__(self):
        return self.title