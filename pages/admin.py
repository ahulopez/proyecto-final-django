from django.contrib import admin
from .models import Post, Libro

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','subtitle','created_at','code','author')
    search_fields = ('title','subtitle','content','code','author__username')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','anio','creado')
    search_fields = ('titulo','autor')
