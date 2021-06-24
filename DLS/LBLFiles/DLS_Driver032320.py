#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:20:30 2019

@author: rebeccarapflbl
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import glob
import os
import pandas as pd
#import datetime
import DLSFunctionLibrary as DFL

# =============================================================================
# FILE DETAILS
# =============================================================================
Path0 = '/Users/rebeccarapflbl/Desktop/ExperimentalData/DLS/Alina/'
#FOLDER = os.getcwd()
#print FOLDER #prints the folder where the python code lives
DATARUN = "test"
DATA_SUBFOLDER = "/"+DATARUN+"/" #where does the data live?
#DATA_SUBFOLDER = "/Test/"
#FILE_EXTENSION ='*.ASC'

os.chdir(Path0+DATA_SUBFOLDER)
print os.getcwd() #prints where you are pulling data from
#FILES = sorted(glob.glob(FILE_EXTENSION))
#FILE_PREFIX = FILES[0][:-8]
#print FILES

NUM_FILES = len(FILES)
print NUM_FILES #how many files are we dealing with
NUM_AVG = 5
R2FILT = 0.5

#LineLocationsDict = {"DATE_LINE": 2,
#                     "TIME_LINE": 3,
#                     "HEADER_LENGTH":23, #remaining lines in header (so full header is 3+HEADER_LENGTH)
#                     "CORRELATION_LENGTH": 190,#207,#215,#190, #number of lines/datapoints in correlation function data
#                     "SPACE_BETWEEN": 3, #lines between correlation function data and scatter intensity data
#                     "COUNTS_LENGTH" : 254}

# =============================================================================
# 
# =============================================================================

modelParamsDict = DFL.initializeExponentialModelParams();

# =============================================================================
# READ IN ALL FILES 
# =============================================================================


##RawNormCorr = 0
#[AllTimes, AllScatter, AllNormCorr, AllDecayTime] = DFL.ReadAllFiles(FILES,LineLocationsDict)
#ScatterTime = pd.DataFrame()
#
#ScatterTime[FILE_PREFIX+'AllTimes']=AllTimes
#ScatterTime[FILE_PREFIX+'AllScatter']=AllScatter
##AllTimesNames =np.zeros(len(AllTimes))
##for entry in range(len(AllTimes)-1):
##AllTimesNames[entry] = str(int(AllTimes[entry]))
#
#AllTimesNames = ["%.0f" % number for number in AllTimes]
##print AllTimesNames
#    
#
#DecayTimeIndex = AllDecayTime[0]
#AllNormCorr = np.transpose(AllNormCorr)
#
#RawNormCorr = pd.DataFrame(index = DecayTimeIndex, columns = AllTimesNames, dtype = 'float64')
#RawNormCorr.index.name = FILE_PREFIX+'DecayTime'
#RawNormCorr.columns.name = FILE_PREFIX+'PhotoTime'
#
#for i in range(NUM_FILES):
#    RawNormCorr.iloc[:,i] = AllNormCorr[:,i]
#    
#RawNormCorr = RawNormCorr.add_prefix(FILE_PREFIX+"PhotoTime")
##print RawNormCorr
#RawNormCorr.to_csv(FILE_PREFIX+"_RawNormCorr.csv")
#ScatterTime.to_csv(FILE_PREFIX+"_RawScatter.csv")
# =============================================================================

# =============================================================================
Radii = np.zeros(NUM_FILES)
RadiiVariance = np.zeros(NUM_FILES)
RadStdDev = np.zeros(NUM_FILES)

AvgCorr = np.zeros(LineLocationsDict.get('CORRELATION_LENGTH'))
AvgRadii = np.zeros((NUM_FILES/NUM_AVG))
AvgRadStdDev = np.zeros((NUM_FILES/NUM_AVG))
AvgTimes = np.zeros((NUM_FILES/NUM_AVG))

R2 =[]
AvgR2 = []

counter = 0
index = 0

#testarray = np.array([[0, 1, 2, 3],[4,5,6,7],[8, 9, 10, 11]])
#
#aa = testarray[0:2,:]
#print aa

for i in range(NUM_FILES/NUM_AVG):
    #print i
    modelParamsDict["DecayTime"] = AllDecayTime[index]
    Radius, RadVar = curve_fit(DFL.ExponentialModel, modelParamsDict, AllNormCorr[index], maxfev = 100000)

    
    AvgCorr = np.zeros(LineLocationsDict.get('CORRELATION_LENGTH'))
    while counter < NUM_AVG:
        AvgCorr = AvgCorr + AllNormCorr[(index)]
        index += 1
        counter += 1
        #print AvgCorr
    counter = 0

    
    

    #Radius, RadVar = curve_fit(DFL.ExponentialModel, DecayTime, NormCorr, maxfev = 100000)
    
    
    if (i+1)%NUM_AVG == 0:
        #print i
        AvgCorr = np.true_divide(AvgCorr, NUM_AVG)
        
        AvgTime = np.true_divide(sum(AllTimes[(i-NUM_AVG+1):i+1]), NUM_AVG)
        #print AllTimes[(i-NUM_AVG+1):i+1]
        AvgTimes[i/NUM_AVG] = AvgTime
        #print AvgCorr
        AvgRadius, AvgRadVar = curve_fit(DFL.ExponentialModel, modelParamsDict, AvgCorr, maxfev = 100000)
#        if AvgRadius > 500:
#            AvgRadius = 0
        AvgRadii[i/NUM_AVG] = AvgRadius
        AvgRadStdDev[i/NUM_AVG] = np.sqrt(np.diag(AvgRadVar))
        
        AvgR0 = np.sum((DFL.ExponentialModel(modelParamsDict, AvgRadii[i/NUM_AVG]) - AvgCorr)**2)
        AvgR1 = np.sum((AvgCorr - np.mean(AvgCorr))**2)
        AvgR2 = np.append(AvgR2, 1 - (AvgR0/AvgR1)) 
        
        if AvgR2[i/NUM_AVG] < R2FILT:
            AvgRadii[i/NUM_AVG] = 0
            AvgRadStdDev[i/NUM_AVG] = 0
#        if AvgRadii[i/NUM_AVG]>200:
#            AvgRadii[i/NUM_AVG] = 0
#            AvgRadStdDev[i/NUM_AVG] = 0
        
        AvgCorr = np.zeros(LineLocationsDict.get("CORRELATION_LENGTH"))
        #print AvgRadius
        counter = 0

    #Radius, RadVar = curve_fit(ExponentialModel, DecayTime, NormCorr, maxfev = 100000)
#    if Radius > 500:
#        Radius = 0

    
    Radii[i] = Radius
    RadiiVariance[i] = RadVar
    RadStdDev[i] = np.sqrt(np.diag(RadVar))
    
    #R**2 goodness of fit paramter
    R0 = np.sum((DFL.ExponentialModel(modelParamsDict, Radii[i]) - AllNormCorr)**2)
    R1 = np.sum((AllNormCorr - np.mean(AllNormCorr))**2)
    R2 = np.append(R2, 1 - (R0/R1)) 
    
#    if R2[i] < 0.7:
#        #print 'hi'
#        Radii[i] = 0
    

plt.plot(np.log10(AllDecayTime), AllNormCorr)
plt.show()
plt.close()
# =============================================================================
# Save and plot analyzed data
# =============================================================================



#RF.DLSPlot(AllTimes/3600, Radii,['Time (hours)', 'Radius (nm)'],'SizeNoAvg')
DFL.DLSPlot(AvgTimes/3600, AvgRadii,['Time (hours)', 'Radius (nm)'],'SizeAvgCorrFiltpt5'+str(NUM_AVG))

#RF.DLSSaveData(AllTimes/3600, Radii,'SizeNoAvgFilt',FILE_PREFIX,R2, RadStdDev)
#DFL.DLSSaveData(AvgTimes/3600, AvgRadii,'SizeFiltpt5AvgCorr'+str(NUM_AVG),FILE_PREFIX, AvgR2,AvgRadStdDev)
#RF.DLSSaveData(AvgTimes/3600, AvgR2,'R2AvgCorr50',FILE_PREFIX)
#RF.DLSSaveData(AvgTimes/3600, AvgRadStdDev,'StdDevAvgCorr50',FILE_PREFIX)

#RF.DLSPlot(AllTimes/3600, AvgScatterPerCorrelation ,['Time (hours)', 'Scatter (kHz)'],'ScatterNoAvg')

#RF.DLSSaveData(AllTimes/3600, AvgScatterPerCorrelation,'ScatterNoAvgHr',FILE_PREFIX)