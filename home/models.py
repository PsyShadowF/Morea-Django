from django.db import models

# Create your models here.

class Water(models.Model):
  id = models.AutoField(primary_key=True)
  dispname = models.CharField(default="", max_length=255)
  location = models.CharField(default="", max_length=255)
  instalh = models.FloatField()
  totall = models.FloatField()
  collectdate = models.DateTimeField()

class Energy(models.Model):
  id = models.AutoField(primary_key=True)
  dispname = models.CharField(default="", max_length=255)
  location = models.CharField(default="", max_length=255)
  minwh = models.FloatField()
  totalwh = models.FloatField()
  collectdate = models.DateTimeField()

class WaterStats(models.Model):
  id = models.AutoField(primary_key=True)
  dispname = models.CharField(default="", max_length=255)
  wMean = models.FloatField()
  wMedian = models.FloatField()
  wSTD = models.FloatField()
  wCV = models.FloatField()
  wMax = models.FloatField()
  wMin = models.FloatField()
  wFQ = models.FloatField()
  wTQ = models.FloatField()

class EnergyStats(models.Model):
  id = models.AutoField(primary_key=True)
  dispname = models.CharField(default="", max_length=255)
  eMean = models.FloatField()
  eMedian = models.FloatField()
  eSTD = models.FloatField()
  eCV = models.FloatField()
  eMax = models.FloatField()
  eMin = models.FloatField()
  eFQ = models.FloatField()
  eTQ = models.FloatField()