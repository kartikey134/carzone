from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.

def home(request):
    teams = Team.objects.all()
    featuredCars = Car.objects.order_by('-createdDate').filter(isFeatured=True)
    allCars = Car.objects.order_by('-createdDate')
    # searchFields = Car.objects.values('model', 'city', 'year', 'bodyStyle')
    modelSearch = Car.objects.values_list('model', flat=True).distinct()
    citySearch = Car.objects.values_list('city', flat=True).distinct()
    yearSearch = Car.objects.values_list('year', flat=True).distinct()
    bodyStyleSearch = Car.objects.values_list('bodyStyle', flat=True).distinct()
    data = {
        'teams': teams,
        'featuredCars': featuredCars,
        'allCars': allCars,
        # 'searchFields': searchFields,
        'modelSearch': modelSearch,
        'citySearch': citySearch,
        'yearSearch': yearSearch,
        'bodyStyleSearch': bodyStyleSearch,
    }
    return render(request, 'pages/home.html', data)

def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')
