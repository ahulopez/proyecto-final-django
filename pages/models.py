from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    content = RichTextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pages:post_detail', args=[str(self.pk)])

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    portada = models.ImageField(upload_to='libros/', blank=True, null=True)
    anio = models.IntegerField()
    creado = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
