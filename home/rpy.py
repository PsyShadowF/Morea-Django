import os
from statistics import mean
os.environ["R_HOME"] = r"C:\Program Files\R\R-4.2.1" # change as needed
import rpy2.robjects as robjects
import rpy2.robjects.packages as rpackages
from rpy2.robjects.vectors import StrVector
from .models import Water, Energy, WaterStats, EnergyStats
import numpy

#Water
wMoteDispsData = list(Water.objects.values_list('dispname'))
wMoteDisps = list(dict.fromkeys(wMoteDispsData))

wMotesValues = {}
for item in range(len(wMoteDisps) + 1):
  if(item > 0):
    wMoteGenericValues = []
    wMoteName = 'WMote' + str(item)
    wMoteGenericData = list(Water.objects.filter(dispname=wMoteName).values_list('instalh'))
    for data in range(len(wMoteGenericData)): 
      wTempMoteData = wMoteGenericData[data]
      wMoteGenericValues.append(wTempMoteData[0])
    wMotesValues['WMote' + str(item)] = wMoteGenericValues

for item in range(len(wMotesValues) + 1):
  if(item > 0):
    wMoteN = 'WMote' + str(item)
    wMean = numpy.mean(wMotesValues[wMoteN])
    wMedian = numpy.median(wMotesValues[wMoteN])
    wSTD = numpy.std(wMotesValues[wMoteN])
    wCV = wSTD / wMean
    wMax = numpy.amax(wMotesValues[wMoteN])
    wMin = numpy.amin(wMotesValues[wMoteN])
    wFQ = numpy.quantile(wMotesValues[wMoteN], 0.25)
    wTQ = numpy.quantile(wMotesValues[wMoteN], 0.75)

    stats = WaterStats(pk=item, dispname=wMoteN, wMean=wMean, wMedian=wMedian, wSTD=wSTD, wCV=wCV, wMax=wMax, wMin=wMin, wFQ=wFQ, wTQ=wTQ)
    stats.save()

#Energy
eMoteDispsData = list(Energy.objects.values_list('dispname'))
eMoteDisps = list(dict.fromkeys(eMoteDispsData))

eMotesValues = {}
for item in range(len(eMoteDisps) + 1):
  if(item > 0):
    eMoteGenericValues = []
    eMoteName = 'EMote' + str(item)
    eMoteGenericData = list(Energy.objects.filter(dispname=eMoteName).values_list('minwh'))
    for data in range(len(eMoteGenericData)): 
      eTempMoteData = eMoteGenericData[data]
      eMoteGenericValues.append(eTempMoteData[0])
    eMotesValues['EMote' + str(item)] = eMoteGenericValues

for item in range(len(eMotesValues) + 1):
  if(item > 0):
    eMoteN = 'EMote' + str(item)
    eMean = numpy.mean(eMotesValues[eMoteN])
    eMedian = numpy.median(eMotesValues[eMoteN])
    eSTD = numpy.std(eMotesValues[eMoteN])
    eCV = eSTD / eMean
    eMax = numpy.amax(eMotesValues[eMoteN])
    eMin = numpy.amin(eMotesValues[eMoteN])
    eFQ = numpy.quantile(eMotesValues[eMoteN], 0.25)
    eTQ = numpy.quantile(eMotesValues[eMoteN], 0.75)

    stats = EnergyStats(pk=item, dispname=eMoteN, eMean=eMean, eMedian=eMedian, eSTD=eSTD, eCV=eCV, eMax=eMax, eMin=eMin, eFQ=eFQ, eTQ=eTQ)
    stats.save()






#RPy Programming
base = rpackages.importr('base')
utils = rpackages.importr('utils')

#Choose CRAN
utils.chooseCRANmirror(ind=1)

packages = ('ggplot2')

#Install R packages.
packagesToInstall = [x for x in packages if not rpackages.isinstalled(x)]
if len(packagesToInstall) > 0:
    utils.install_packages(StrVector(packagesToInstall))