from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'mainapp/home.html')

def about(request):
    return render(request, 'mainapp/about.html')

@login_required
def dashboard_protegido(request):
    return render(request, 'mainapp/dashboard.html')
