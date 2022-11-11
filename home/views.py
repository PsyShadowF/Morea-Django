from django.shortcuts import render, HttpResponseRedirect
from .models import Water
from statistics import *

# Create your views here.


def homeEmpty(request):
    return HttpResponseRedirect('home/')


def home(request):
    return render(request, 'home.html')


def dados(request):

    data = Water.objects.all()

    print(data)

    return render(request, 'dados.html', {'data': data})


def dashboard(request):

    return render(request, 'dashboard.html')


def about(request):

    return render(request, 'about.html')
