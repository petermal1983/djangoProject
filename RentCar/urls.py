from  django.contrib import admindocs
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.main_view),
    url(r'^index/$', views.main_view),
    path('grappelli/', include('grappelli.urls')),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('rent', views.rent_list, name='rent_list'),
    path('driver', views.driver_chouse, name='driver_list'),
    path('vehicle', views.vehicle_list, name='vehicle_list'),
    path('spezeqv', views.spezeqv_choose, name='spezeqv_list'),
    #path('signup', views.signup, name='signup'),
    path('register', views.register, name='register'),
    path('about', views.about, name='about')
]

