from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def cars(request):

    cars = Car.objects.order_by('-createdDate')
    paginator = Paginator(cars, 2)
    page = request.GET.get('page')
    pagedCars = paginator.get_page(page)

    modelSearch = Car.objects.values_list('model', flat=True).distinct()
    citySearch = Car.objects.values_list('city', flat=True).distinct()
    yearSearch = Car.objects.values_list('year', flat=True).distinct()
    bodyStyleSearch = Car.objects.values_list('bodyStyle', flat=True).distinct()

    data = {
        'cars': pagedCars,
        'modelSearch': modelSearch,
        'citySearch': citySearch,
        'yearSearch': yearSearch,
        'bodyStyleSearch': bodyStyleSearch,
    }

    return render(request, 'cars/cars.html', data)

def carDetail(request, id):

    singleCar = get_object_or_404(Car, pk=id)

    data = {
        'singleCar': singleCar,
    }

    return render(request, 'cars/carDetail.html', data)

def search(request):

    cars = Car.objects.order_by('createdDate')

    modelSearch = Car.objects.values_list('model', flat=True).distinct()
    citySearch = Car.objects.values_list('city', flat=True).distinct()
    yearSearch = Car.objects.values_list('year', flat=True).distinct()
    bodyStyleSearch = Car.objects.values_list('bodyStyle', flat=True).distinct()
    transmissionSearch = Car.objects.values_list('transmission', flat=True).distinct()

    # filtering car data acc to Search
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'bodyStyle' in request.GET:
        bodyStyle = request.GET['bodyStyle']
        if bodyStyle:
            cars = cars.filter(bodyStyle__iexact=bodyStyle)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            cars = cars.filter(transmission__iexact=transmission)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'cars': cars,
        'modelSearch': modelSearch,
        'citySearch': citySearch,
        'yearSearch': yearSearch,
        'bodyStyleSearch': bodyStyleSearch,
        'transmissionSearch': transmissionSearch,
    }

    return render(request, 'cars/search.html', data)
