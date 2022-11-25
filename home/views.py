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
    waterCounter = 0

    for data in waterData:
        wData = int(data[0])
        waterCounter += 1
        relatedWaterData = Data.objects.filter(mote=wData).select_related('mote')
        waterDataContext.update({'WMote' + str(waterCounter): relatedWaterData})

    #Get Energy Motes Values
    energyData = Motes.objects.values_list('id').filter(type=2)
    energyDataContext = {}
    energyCounter = 0

    for data in energyData:
        eData = int(data[0])
        energyCounter += 1
        relatedEnergyData = Data.objects.filter(mote=eData).select_related('mote')
        energyDataContext.update({'EMote' + str(energyCounter): relatedEnergyData})

    #Get Energy Motes Values
    gas_BMData = Motes.objects.values_list('id').filter(type=3)
    gas_BMDataContext = {}
    gas_BMCounter = 0

    for data in gas_BMData:
        g_BMData = int(data[0])
        gas_BMCounter += 1
        relatedGas_BMData = Data.objects.filter(mote=g_BMData).select_related('mote')
        gas_BMDataContext.update({'GMote-BM' + str(energyCounter): relatedGas_BMData})
  
    return render(request, 'dados.html', {'water': waterDataContext, 'energy': energyDataContext, 'gas_BM': gas_BMDataContext})


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
