from django.contrib import admin
from .models import Water, Energy, WaterStats, EnergyStats

# Register your models here.

class WaterData(admin.ModelAdmin):
  list_display = ['id', 'dispname', 'location', 'instalh', 'totall', 'collectdate']

class EnergyData(admin.ModelAdmin):
  list_display = ['id', 'dispname', 'location', 'minwh', 'totalwh', 'collectdate']

class WaterStatsData(admin.ModelAdmin):
  list_display = ['id', 'dispname', 'wMean', 'wMedian', 'wSTD', 'wCV', 'wMax', 'wMin', 'wFQ', 'wTQ']

class EnergyStatsData(admin.ModelAdmin):
  list_display = ['id', 'dispname', 'eMean', 'eMedian', 'eSTD', 'eCV', 'eMax', 'eMin', 'eFQ', 'eTQ']

admin.site.register(Water, WaterData)
admin.site.register(Energy, EnergyData)
admin.site.register(WaterStats, WaterStatsData)
admin.site.register(EnergyStats, EnergyStatsData)