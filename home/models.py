from django.db import models

# Create your models here.


class Motes(models.Model):
    name = models.CharField(max_length=255)
    sector = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=255, null=False)


class Water(models.Model):
    mote_id = models.ForeignKey(Motes, on_delete=models.CASCADE, default=0)
    instalh = models.FloatField()
    totall = models.FloatField()
    collectdate = models.DateTimeField()


class Energy(models.Model):
    mote_id = models.ForeignKey(Motes, on_delete=models.CASCADE, default=0)
    minwh = models.FloatField()
    totalwh = models.FloatField()
    collectdate = models.DateTimeField()


class WaterStats(models.Model):
    mote_id = models.ForeignKey(Motes, on_delete=models.CASCADE, default=0)
    wMean = models.FloatField()
    wMedian = models.FloatField()
    wSTD = models.FloatField()
    wCV = models.FloatField()
    wMax = models.FloatField()
    wMin = models.FloatField()
    wFQ = models.FloatField()
    wTQ = models.FloatField()


class EnergyStats(models.Model):
    mote_id = models.ForeignKey(Motes, on_delete=models.CASCADE, default=0)
    eMean = models.FloatField()
    eMedian = models.FloatField()
    eSTD = models.FloatField()
    eCV = models.FloatField()
    eMax = models.FloatField()
    eMin = models.FloatField()
    eFQ = models.FloatField()
    eTQ = models.FloatField()
