from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
