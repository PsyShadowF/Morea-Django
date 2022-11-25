from django.db import models

# Create your models here.

class MoteType(models.IntegerChoices):
    null = 0, 'NullMote'
    water = 1, 'WMote'
    energy = 2, 'EMote'
    gas_BM = 3, 'GMote-BM'

class Motes(models.Model):
    name = models.CharField(max_length=255)
    type = models.IntegerField(default=MoteType.null, choices=MoteType.choices)
    sector = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=255, null=False)


class Data(models.Model):
    mote = models.ForeignKey(Motes, on_delete=models.CASCADE, default=0)
    min_lh = models.FloatField(default=0) #Litros/Hora no último minuto
    total_l = models.FloatField(default=0) #Listros totais
    min_wh = models.FloatField(default=0) #Watt/Hora no último minuto
    total_wh = models.FloatField(default=0) #Total de Watts consumidos
    min_ppm = models.FloatField(default=0) #Partes por milhão no último minuto
    collect_date = models.DateTimeField() #Data de coleta


#class WaterStats(models.Model):
#    mote_id = models.ForeignKey(Motes, on_delete=models.CASCADE, default=0)
#    wMean = models.FloatField()
#    wMedian = models.FloatField()
#    wSTD = models.FloatField()
#    wCV = models.FloatField()
#    wMax = models.FloatField()
#    wMin = models.FloatField()
#    wFQ = models.FloatField()
#    wTQ = models.FloatField()


#class EnergyStats(models.Model):
#    mote_id = models.ForeignKey(Motes, on_delete=models.CASCADE, default=0)
#    eMean = models.FloatField()
#    eMedian = models.FloatField()
#    eSTD = models.FloatField()
#    eCV = models.FloatField()
#    eMax = models.FloatField()
#    eMin = models.FloatField()
#    eFQ = models.FloatField()
#    eTQ = models.FloatField()
