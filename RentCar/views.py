from django.shortcuts import render, get_object_or_404
from .models import Rent, Driver


# Create your views here.
def driver_chouse(request):
    drivers = Driver.objects.all()
    return render(request, 'html/DriverCard.html', {'drivers': drivers})
def rent_list(request):
    rents = Rent.objects.all()
    return render(request, 'html/list.html', {'rents': rents})
