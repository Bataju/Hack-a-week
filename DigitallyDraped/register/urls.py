#created by us to link urls between the main project and other apps like this
from django.urls import path
from . import views #importing views.py

urlpatterns = [
    path('', views.index, name="index"),
]#default path in this app is linked to views.index