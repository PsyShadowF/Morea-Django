from django.shortcuts import render, HttpResponseRedirect
from .models import Water, Energy, WaterStats, EnergyStats

# Create your views here.


def homeEmpty(request):
    return HttpResponseRedirect('home/')


def home(request):
    return render(request, 'home.html')


def dados(request):
    waterData = Water.objects.all()
    energyData = Energy.objects.all()

    return render(request, 'dados.html', {'waterData': waterData, 'energyData': energyData})


def dashboard(request):
    waterStatsData = WaterStats.objects.all()
    energyStatsData = EnergyStats.objects.all()

    return render(request, 'dashboard.html', {'waterStatsData': waterStatsData, 'energyStatsData': energyStatsData})


def about(request):

    return render(request, 'about.html')
