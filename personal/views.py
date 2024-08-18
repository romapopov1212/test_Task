from django.shortcuts import render, redirect
from personal.forms import AddForm
from .models import Car
# Create your views here.

def home_screen_view(request):
    cars = Car.objects.all()
    return render(request, "home.html", {'cars' : cars})

def add_screen_view(request):
    if request.POST:
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            
        return redirect(home_screen_view)
    
    return render(request, "add.html", {'form' : AddForm})


