
from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=255)  # Título de la publicación
    content = models.TextField()  # Contenido de la publicación
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Autor de la publicación
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)  # Fecha de última actualización
    published_at = models.DateTimeField(null=True, blank=True)  # Fecha de publicación
    is_published = models.BooleanField(default=False)  # Estado de publicación
    categories = models.ManyToManyField(Categoria, blank=True)  # Categorías relacionadas
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)  # Archivo adjunto

    def __str__(self):
        return self.title
