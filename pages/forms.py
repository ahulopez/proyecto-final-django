from django import forms
from .models import Post, Libro

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','subtitle','content','image','code']

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo','autor','descripcion','portada','anio']
