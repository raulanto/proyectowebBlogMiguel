from django.contrib import admin
from .models.post import Post,Categoria
# Register your models here.

admin.site.register(Post)
admin.site.register(Categoria)