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
#import datetime
import ReadFile as RF

# =============================================================================
# FILE DETAILS
# =============================================================================

FOLDER = os.getcwd()
#print FOLDER #prints the folder where the python code lives
DATA_SUBFOLDER = "/test/" #where does the data live?
#DATA_SUBFOLDER = "/Test/"
FILE_EXTENSION ='*.ASC'
os.chdir(FOLDER+DATA_SUBFOLDER)
print os.getcwd() #prints where you are pulling data from
FILES = sorted(glob.glob(FILE_EXTENSION))
FILE_PREFIX = FILES[0][:-9]
NUM_FILES = len(FILES)
print NUM_FILES #how many files are we dealing with
NUM_AVG = 2
R2FILT = 0.5

LineLocationsDict = {"DATE_LINE": 2,
                     "TIME_LINE": 3,
                     "HEADER_LENGTH":23, #remaining lines in header (so full header is 3+HEADER_LENGTH)
                     "CORRELATION_LENGTH": 190,#207,#215,#190, #number of lines/datapoints in correlation function data
                     "SPACE_BETWEEN": 3, #lines between correlation function data and scatter intensity data
                     "COUNTS_LENGTH" : 254}

# =============================================================================
# 
# =============================================================================
modelParamsDict = RF.initializeExponentialModelParams();

# =============================================================================
# READ IN FILE DATA and FIT IT
# =============================================================================
AvgScatterPerCorrelation = np.zeros(NUM_FILES)
Radii = np.zeros(NUM_FILES)
RadiiVariance = np.zeros(NUM_FILES)
RadStdDev = np.zeros(NUM_FILES)
AvgCorr = np.zeros(LineLocationsDict.get('CORRELATION_LENGTH'))
AvgRadii = np.zeros((NUM_FILES/NUM_AVG))
AvgRadStdDev = np.zeros((NUM_FILES/NUM_AVG))
AvgTimes = np.zeros((NUM_FILES/NUM_AVG))
AllTimes = np.zeros(NUM_FILES)
R2 =[]
AvgR2 = []

counter = 0
for i in range(NUM_FILES):
#    print i
    date,time,corr,scatter = RF.ReadFile(FILES[i],LineLocationsDict)

    CurrentTime = RF.SplitTime(date,time)

    if i == 0:
  
        start = CurrentTime
        AllTimes[i] = (start-start).total_seconds()
        
    else:
        AllTimes[i] = (CurrentTime-start).total_seconds()


    AvgScatterPerCorrelation[i] = np.average(scatter[:,1])
    #print AvgScatterPerCorrelation
    
    NormCorr = corr[:,1]/np.average(corr[:,1][:50])
    DecayTime = corr[:,0]
    
    
    while counter < NUM_AVG:
        counter += 1
        AvgCorr = AvgCorr+NormCorr
        #print "AVGCORR" +str(AvgCorr)
    
    modelParamsDict["DecayTime"] = DecayTime

    #Radius, RadVar = curve_fit(ExponentialModel, DecayTime, NormCorr, maxfev = 100000)
    Radius, RadVar = curve_fit(RF.ExponentialModel, modelParamsDict, NormCorr, maxfev = 100000)
    
    if (i+1)%NUM_AVG == 0:
        #print i
        AvgCorr = np.true_divide(AvgCorr, NUM_AVG)
        
        AvgTime = np.true_divide(sum(AllTimes[(i-NUM_AVG+1):i+1]), NUM_AVG)
        #print AllTimes[(i-NUM_AVG+1):i+1]
        AvgTimes[i/NUM_AVG] = AvgTime
        #print AvgCorr
        AvgRadius, AvgRadVar = curve_fit(RF.ExponentialModel, modelParamsDict, AvgCorr, maxfev = 100000)
        print AvgRadVar
#        if AvgRadius > 500:
#            AvgRadius = 0
        AvgRadii[i/NUM_AVG] = AvgRadius
        print np.diag(AvgRadVar)
        AvgRadStdDev[i/NUM_AVG] = np.sqrt(np.diag(AvgRadVar))
        
        AvgR0 = np.sum((RF.ExponentialModel(modelParamsDict, AvgRadii[i/NUM_AVG]) - AvgCorr)**2)
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
    print NormCorr
    R0 = np.sum((RF.ExponentialModel(modelParamsDict, Radii[i]) - NormCorr)**2)
    R1 = np.sum((NormCorr - np.mean(NormCorr))**2)
    R2 = np.append(R2, 1 - (R0/R1)) 
    
#    if R2[i] < 0.7:
#        #print 'hi'
#        Radii[i] = 0
    

plt.plot(np.log10(DecayTime), NormCorr)
plt.show()
plt.close()
# =============================================================================
# Save and plot analyzed data
# =============================================================================



#RF.DLSPlot(AllTimes/3600, Radii,['Time (hours)', 'Radius (nm)'],'SizeNoAvg')
RF.DLSPlot(AvgTimes/3600, AvgRadii,['Time (hours)', 'Radius (nm)'],'SizeAvgCorrFiltpt5'+str(NUM_AVG))

#RF.DLSSaveData(AllTimes/3600, Radii,'SizeNoAvgFilt',FILE_PREFIX,R2, RadStdDev)
RF.DLSSaveData(AvgTimes/3600, AvgRadii,'SizeFiltpt5AvgCorr'+str(NUM_AVG),FILE_PREFIX, AvgR2,AvgRadStdDev)
#RF.DLSSaveData(AvgTimes/3600, AvgR2,'R2AvgCorr50',FILE_PREFIX)
#RF.DLSSaveData(AvgTimes/3600, AvgRadStdDev,'StdDevAvgCorr50',FILE_PREFIX)

#RF.DLSPlot(AllTimes/3600, AvgScatterPerCorrelation ,['Time (hours)', 'Scatter (kHz)'],'ScatterNoAvg')

#RF.DLSSaveData(AllTimes/3600, AvgScatterPerCorrelation,'ScatterNoAvgHr',FILE_PREFIX)