from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('password/', views.password_change, name='password_change'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
]
