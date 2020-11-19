from django.shortcuts import render, get_object_or_404
from .models import Rent, Driver, Vehicle, SpecialEquipment


# Create your views here.
def driver_chouse(request):
    drivers = Driver.objects.all()
    return render(request, 'html/DriverCard.html', {'drivers': drivers})

def spezeqv_choose(request):
    special_equipment = SpecialEquipment.objects.all()
    return render(request, 'html/SpezeqvCard.html', {'special_equipment': special_equipment})


def rent_list(request):
    rents = Rent.objects.all()
    return render(request, 'html/list.html', {'rents': rents})


def vehicle_spec(request):
    vehicles = Vehicle.spec_objects.all()
    first = Vehicle.spec_objects.first()
    return render(request, 'html/VehiclesCard.html', {'vehicles': vehicles, 'first': first})


def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'html/VehiclesCard.html', {'vehicles': vehicles})
