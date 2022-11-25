from django.contrib import admin
from .models import Motes, Data

# Register your models here.


class MotesData(admin.ModelAdmin):
    list_display = ['id', 'name', 'type', 'sector', 'location']


class DataData(admin.ModelAdmin):
    list_display = ['id', 'mote', 'min_lh', 'total_l', 'min_wh', 'total_wh', 'min_ppm', 'collect_date']


admin.site.register(Motes, MotesData)
admin.site.register(Data, DataData)