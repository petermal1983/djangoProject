from django.contrib import admin
from django.urls import path, include
from djangoProject.views import hello

urlpatterns = [
    path('admin/', admin.site.urls)
]
