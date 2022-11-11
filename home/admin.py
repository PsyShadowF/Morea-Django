from django.contrib import admin
from .models import Motes, Water, Energy, WaterStats, EnergyStats

# Register your models here.


class MotesData(admin.ModelAdmin):
    list_display = ['name', 'sector', 'location']


class WaterData(admin.ModelAdmin):
    list_display = ['instalh', 'totall', 'collectdate']


class EnergyData(admin.ModelAdmin):
    list_display = ['minwh', 'totalwh', 'collectdate']


class WaterStatsData(admin.ModelAdmin):
    list_display = ['wMean', 'wMedian',
                    'wSTD', 'wCV', 'wMax', 'wMin', 'wFQ', 'wTQ']


class EnergyStatsData(admin.ModelAdmin):
    list_display = ['eMean', 'eMedian',
                    'eSTD', 'eCV', 'eMax', 'eMin', 'eFQ', 'eTQ']


admin.site.register(Motes, MotesData)
admin.site.register(Water, WaterData)
admin.site.register(Energy, EnergyData)
admin.site.register(WaterStats, WaterStatsData)
admin.site.register(EnergyStats, EnergyStatsData)
