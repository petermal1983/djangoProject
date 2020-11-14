from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rent', views.rent_list, name='rent_list'),
    path('driver', views.driver_chouse, name='driver_list')

]
