from django.contrib import admin
from .models import Motes, Data

# Register your models here.


class MotesData(admin.ModelAdmin):
    list_display = ['name', 'type', 'sector', 'location']

class DataData(admin.ModelAdmin):
    list_display = ['mote', 'min_lh', 'totall', 'min_wh', 'totalwh', 'min_ppm', 'collectdate']


admin.site.register(Motes, MotesData)
admin.site.register(Data, DataData)
