from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.
def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.all()
    search_fields = Car.objects.values('model', 'city', 'year', 'body_style')
    model_fields = Car.objects.values_list('model', flat=True).distinct()
    city_fields = Car.objects.values_list('city', flat=True).distinct()
    year_fields = Car.objects.values_list('year', flat=True).distinct()
    body_style_fields = Car.objects.values_list('body_style', flat=True).distinct()
    data = {
        'teams': teams,
        'featured_cars' : featured_cars,
        'all_cars': all_cars,
        'search_fields': search_fields,
        'model_fields': model_fields,
        'city_fields': city_fields,
        'year_fields': year_fields,
        'body_style_fields': body_style_fields

    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

# def cars(request):
#     return render(request, 'pages/cars.html')

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')