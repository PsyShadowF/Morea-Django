import numpy
from .models import Motes, Data, Stats
import pandas as pd
import matplotlib.pyplot as plt

# testing

def calcWaterStats():
    wMotes = Motes.objects.values_list('id').filter(type=1)

    for mote in wMotes:
        wMotesData = list(Data.objects.values_list('min_lh').filter(mote=mote))
        wMean = numpy.mean(wMotesData)
        wMedian = numpy.median(wMotesData)
        wSTD = numpy.std(wMotesData)
        wCV = wSTD / wMean
        wMax = numpy.amax(wMotesData)
        wMin = numpy.amin(wMotesData)
        wFQ = numpy.quantile(wMotesData, 0.25)
        wTQ = numpy.quantile(wMotesData, 0.75)
        stats = Stats(id=mote[0], mote=Motes.objects.get(id=mote[0]), mean=wMean, median=wMedian, std=wSTD, cv=wCV, max=wMax, min=wMin, fq=wFQ, tq=wTQ)
        stats.save()

dataList = {}
wMotes = Motes.objects.values_list('id').filter(type=1)
biggestList = 0
qnt = 0

for mote in wMotes:
    tempDataList = []
    wMotesData = list(Data.objects.values_list('min_lh').filter(mote=mote))
    for data in wMotesData:
        tempDataList.append(data[0])
    listSize = len(tempDataList)
    if listSize > biggestList:
        biggestList = listSize

for mote in wMotes:
    qnt += 1
    tempDataList = []
    wMotesData = list(Data.objects.values_list('min_lh').filter(mote=mote))
    for data in wMotesData:
        tempDataList.append(data[0])
    while len(tempDataList) < biggestList:
        tempDataList.append(None)
    dataList.update({'wMote' + str(qnt): tempDataList})

print(dataList)

names = list(dataList.keys())
values = list(dataList.values())

dataTest = pd.DataFrame(dataList)
dataTest.head()

dataTest.plot(ylabel='L/H', title='Direct vs Tele Sales')

#plt.bar(range(len(dataList)), values, tick_label=names)
plt.show()

deb = 0

'''# Water
wMoteDispsData = list(Water.objects.values_list('dispname'))
wMoteDisps = list(dict.fromkeys(wMoteDispsData))

wMotesValues = {}
for item in range(len(wMoteDisps) + 1):
    if (item > 0):
        wMoteGenericValues = []
        wMoteName = 'WMote' + str(item)
        wMoteGenericData = list(Water.objects.filter(
            dispname=wMoteName).values_list('instalh'))
        for data in range(len(wMoteGenericData)):
            wTempMoteData = wMoteGenericData[data]
            wMoteGenericValues.append(wTempMoteData[0])
        wMotesValues['WMote' + str(item)] = wMoteGenericValues

for item in range(len(wMotesValues) + 1):
    if (item > 0):
        wMoteN = 'WMote' + str(item)
        wMean = numpy.mean(wMotesValues[wMoteN])
        wMedian = numpy.median(wMotesValues[wMoteN])
        wSTD = numpy.std(wMotesValues[wMoteN])
        wCV = wSTD / wMean
        wMax = numpy.amax(wMotesValues[wMoteN])
        wMin = numpy.amin(wMotesValues[wMoteN])
        wFQ = numpy.quantile(wMotesValues[wMoteN], 0.25)
        wTQ = numpy.quantile(wMotesValues[wMoteN], 0.75)

        stats = WaterStats(pk=item, dispname=wMoteN, wMean=wMean, wMedian=wMedian,
                           wSTD=wSTD, wCV=wCV, wMax=wMax, wMin=wMin, wFQ=wFQ, wTQ=wTQ)
        stats.save()

# Energy
eMoteDispsData = list(Energy.objects.values_list('dispname'))
eMoteDisps = list(dict.fromkeys(eMoteDispsData))

eMotesValues = {}
for item in range(len(eMoteDisps) + 1):
    if (item > 0):
        eMoteGenericValues = []
        eMoteName = 'EMote' + str(item)
        eMoteGenericData = list(Energy.objects.filter(
            dispname=eMoteName).values_list('minwh'))
        for data in range(len(eMoteGenericData)):
            eTempMoteData = eMoteGenericData[data]
            eMoteGenericValues.append(eTempMoteData[0])
        eMotesValues['EMote' + str(item)] = eMoteGenericValues

for item in range(len(eMotesValues) + 1):
    if (item > 0):
        eMoteN = 'EMote' + str(item)
        eMean = numpy.mean(eMotesValues[eMoteN])
        eMedian = numpy.median(eMotesValues[eMoteN])
        eSTD = numpy.std(eMotesValues[eMoteN])
        eCV = eSTD / eMean
        eMax = numpy.amax(eMotesValues[eMoteN])
        eMin = numpy.amin(eMotesValues[eMoteN])
        eFQ = numpy.quantile(eMotesValues[eMoteN], 0.25)
        eTQ = numpy.quantile(eMotesValues[eMoteN], 0.75)

        stats = EnergyStats(pk=item, dispname=eMoteN, eMean=eMean, eMedian=eMedian,
                            eSTD=eSTD, eCV=eCV, eMax=eMax, eMin=eMin, eFQ=eFQ, eTQ=eTQ)
        stats.save()'''