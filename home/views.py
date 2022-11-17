from django.shortcuts import render, HttpResponseRedirect
from .models import Motes
from statistics import *

# Create your views here.


def homeEmpty(request):
    return HttpResponseRedirect('home/')


def home(request):
    return render(request, 'home.html')


def dados(request):

    return render(request, 'dados.html')


def dashboard(request):

    return render(request, 'dashboard.html')


def about(request):

    return render(request, 'about.html')


def debbug(request):
    dict = {
        '1': [
            'Wmote01',
            'bebedouro'
        ],
        '2': [
            'Wmote02',
            'bebedouro'
        ]
    }

    #WaterData = Water.objects.select_related('mote')

    #print(WaterData.query)
    #print(WaterData[0])

    return render(request, 'debbug.html')
