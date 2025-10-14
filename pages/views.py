from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Post, Libro
from .forms import PostForm, LibroForm

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'pages/post_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(subtitle__icontains=q) | Q(content__icontains=q))
        return qs

    @classmethod
    def as_form_view(cls):
        def view(request, *args, **kwargs):
            self = cls()
            self.request = request
            context = {'posts': self.get_queryset()}
            return render(request, 'pages/post_list.html', context)
        return view

class PostDetailView(DetailView):
    model = Post
    template_name = 'pages/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'pages/post_form.html'
    success_url = reverse_lazy('pages:post_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        messages.success(self.request, 'Post creado.')
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'pages/post_form.html'

    def get_success_url(self):
        messages.success(self.request, 'Post actualizado.')
        return self.object.get_absolute_url()

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'pages/post_confirm_delete.html'
    success_url = reverse_lazy('pages:post_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Post eliminado.')
        return super().delete(request, *args, **kwargs)

def libro_list(request):
    q = request.GET.get('q')
    if q:
        libros = Libro.objects.filter(Q(titulo__icontains=q) | Q(autor__icontains=q) | Q(descripcion__icontains=q))
    else:
        libros = Libro.objects.all()
    return render(request, 'pages/libro_list.html', {'libros': libros})

def libro_detail(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'pages/libro_detail.html', {'libro': libro})

@login_required
def libro_create(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro creado.')
            return redirect('pages:libro_list')
    else:
        form = LibroForm()
    return render(request, 'pages/libro_form.html', {'form': form})

@login_required
def libro_update(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro actualizado.')
            return redirect('pages:libro_detail', pk=libro.pk)
    else:
        form = LibroForm(instance=libro)
    return render(request, 'pages/libro_form.html', {'form': form, 'libro': libro})

@login_required
def libro_delete(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        messages.success(request, 'Libro eliminado.')
        return redirect('pages:libro_list')
    return render(request, 'pages/libro_confirm_delete.html', {'libro': libro})
