from django.shortcuts import render

# Create your views here.

def home_screen_view(request):
    
    return render(request, "home.html")

def add_screen_view(request):
    return render(request, "add.html")