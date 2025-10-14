from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('posts/', views.PostListView.as_form_view(), name='post_list'),
    path('posts/create/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    path('libros/', views.libro_list, name='libro_list'),
    path('libros/create/', views.libro_create, name='libro_create'),
    path('libros/<int:pk>/', views.libro_detail, name='libro_detail'),
    path('libros/<int:pk>/edit/', views.libro_update, name='libro_update'),
    path('libros/<int:pk>/delete/', views.libro_delete, name='libro_delete'),
]
