from django.shortcuts import render, redirect
from .forms import AddForm
from .models import Car
from .filters import CarFilter
# Create your views here.

def home_screen_view(request):
    cars = Car.objects.all()
    
    myFilter = CarFilter(request.GET, queryset=cars)
    
    cars = myFilter.qs
    return render(request, "home.html", {'cars' : cars, 'myFilter' : myFilter})

def add_screen_view(request):
    if request.POST:
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            
        return redirect(home_screen_view)
    
    return render(request, "add.html", {'form' : AddForm})


