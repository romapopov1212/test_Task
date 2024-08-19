from django.shortcuts import render, redirect
from .forms import AddForm
from .models import Car
from .filters import CarFilter
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.core.exceptions import ValidationError


def home_screen_view(request):
    cars = Car.objects.all()
    myFilter = CarFilter(request.GET, queryset=cars)
    cars = myFilter.qs
    context = {'cars': cars, 'myFilter': myFilter}
    return render(request, "home.html", context)

def add_screen_view(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            try:
               
                form.save()
                return redirect(home_screen_view)
            except ValidationError as e:
                
                form.add_error(None, e)

    else:
        form = AddForm()

    context = {'form': form}
    return render(request, "add.html", context)

def pageNotFound(request, exception):
    response = HttpResponseNotFound('<h1>Client error</h1>')
    response.status_code = 404
    return response
