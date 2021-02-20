from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from .models import Rent, Driver, Vehicle, SpecialEquipment
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .forms import RegistrationForm
from django.contrib.auth.models import User


# Create your views here.
def main_view(request):
    return render(request, 'html/index.html')


def driver_chouse(request):
    drivers = Driver.objects.all()
    return render(request, 'html/DriverCard.html', {'drivers': drivers})


def about(request):
    return render(request, 'html/about.html')


def spezeqv_choose(request):
    special_equipment = SpecialEquipment.objects.all()
    return render(request, 'html/SpezeqvCard.html', {'special_equipment': special_equipment})


def rent_list(request):
    rents = Rent.objects.all()
    return render(request, 'html/list.html', {'rents': rents})


def vehicle_list(request):
    vehicles = Vehicle.spec_objects.all()
    first = Vehicle.spec_objects.first()
    return render(request, 'html/VehiclesCard.html', {'vehicles': vehicles, 'first': first})


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.password(form.cleaned_data['password'])
            user.save()
            return render(request, '')
    else:
        form = RegistrationForm()
        return render(request, 'html/signup.html', {'form': form})


def logined(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("")
    else:
        return HttpResponseRedirect("")


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.customeruser.age = form.cleaned_data.get('age')
            user.customeruser.adress = form.cleaned_data.get('adress')
            user.customeruser.phone_num = form.cleaned_data.get('phone_num')
            user.customeruser.license_num = form.cleaned_data.get('license_num')
            user.customeruser.citizenship = form.cleaned_data.get('citizenship')
            user.customeruser.save()
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            return redirect("http://127.0.0.1:8000")
        else:
            return HttpResponse(form.errors.as_json())

    else:
        form = RegistrationForm()
        return render(request, "html/register.html", {'form': form})
