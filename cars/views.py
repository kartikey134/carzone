from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def cars(request):
    cars = Car.objects.order_by('-createdDate')
    paginator = Paginator(cars, 2)
    page = request.GET.get('page')
    pagedCars = paginator.get_page(page)
    data = {
        'cars': pagedCars,
    }
    return render(request, 'cars/cars.html', data)

def carDetail(request, id):
    singleCar = get_object_or_404(Car, pk=id)
    data = {
        'singleCar': singleCar,
    }
    return render(request, 'cars/carDetail.html', data)
