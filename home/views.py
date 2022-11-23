from django.shortcuts import render, HttpResponseRedirect
from .models import Motes, Data
from statistics import *

# Create your views here.


def homeEmpty(request):
    return HttpResponseRedirect('home/')


def home(request):
    return render(request, 'home.html')


def dados(request):

    #Get Water Motes Values
    waterData = Motes.objects.values_list('id').filter(type=1)
    waterDataContext = {}

    counter = 0

    for wdata in waterData:
        wdatat = int(wdata[0])
        counter += 1
        tempData = Data.objects.filter(mote=wdatat).select_related('mote')
        waterDataContext.update({'WMote' + str(counter): tempData})
    
    return render(request, 'dados.html', {'water': waterDataContext})


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
