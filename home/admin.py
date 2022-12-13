from django.contrib import admin
from .models import Motes, Data, Stats

# Register your models here.


class MotesData(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'sector', 'location']


class DataData(admin.ModelAdmin):
    list_display = ['id', 'mote', 'min_lh', 'total_l', 'min_wh', 'total_wh', 'min_ppm', 'collect_date']

class StatsData(admin.ModelAdmin):
    list_display = ['id', 'mote', 'mean', 'median', 'std', 'cv', 'max', 'min', 'fq', 'tq']

admin.site.register(Motes, MotesData)
admin.site.register(Data, DataData)
admin.site.register(Stats, StatsData)