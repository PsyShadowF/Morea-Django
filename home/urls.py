from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeEmpty, name='homeEmpty'),
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dados/', views.dados, name='dados'),
    path('sobre/', views.about, name='sobre'),
]
