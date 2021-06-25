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
SAVE_DATA = 'yes'

NUM_AVG = 10
R2FILTName = 5

DATARUN = "060120PSLs/conc/"
FILE_PREFIX = "psl 100nm"
DATA_SUBFOLDER = "/"+DATARUN+"/extracted" #where does the data live?
os.chdir(Path0+DATA_SUBFOLDER)
print os.getcwd() #prints where you are pulling data from



data = pd.read_csv(FILE_PREFIX+"_RawNormCorr.csv")
ScatterTime = pd.read_csv(FILE_PREFIX+"_RawScatter.csv")

NUM_FILES = len(data.columns)-1
CorrLength = len(data.index)
Decays = data.columns.values[0]
print NUM_FILES #how many files are we dealing with

R2FILT = R2FILTName/10.
#print R2FILT
AvgCorrPrefix = FILE_PREFIX+'Corr_Avg'+str(NUM_AVG)+"_"
AvgRadPrefix =FILE_PREFIX+'Rad_Avg'+str(NUM_AVG)+'_Fpt'+str(R2FILTName)+"_T293"


# =============================================================================
# 
# =============================================================================

modelParamsDict = DFL.initializeExponentialModelParams();


# =============================================================================

# =============================================================================

#print NUM_AVG
#AvgCorrPrefix = DATARUN+'Corr_Avg'+str(NUM_AVG)+"_"
#AvgRadPrefix =DATARUN+'Rad_Avg'+str(NUM_AVG)+'_Fpt'+str(R2FILTName)+"_"
AllTime = ScatterTime.iloc[:,1]
AllScatter = ScatterTime.iloc[:,2]

LengthOfAvg = NUM_FILES/int(NUM_AVG)
print LengthOfAvg
AvgData = pd.DataFrame()
MeanAvgData = pd.DataFrame()
StdAvgData = pd.DataFrame()
AvgTimesArray = np.zeros(LengthOfAvg)
RadiiArray = np.zeros(LengthOfAvg)
RadVarArray = np.zeros(LengthOfAvg)
RadStdArray = np.zeros(LengthOfAvg)
AvgScatterArray = np.zeros(LengthOfAvg)
AvgScatterStdDev = np.zeros(LengthOfAvg)
R2Array = np.zeros(LengthOfAvg)
FitArray = pd.DataFrame()

for i in range(LengthOfAvg):
    StartingPosition = i*NUM_AVG
    #print AllTime.iloc[StartingPosition:StartingPosition+NUM_AVG]
    AvgTimesArray[i] = AllTime.iloc[StartingPosition:StartingPosition+NUM_AVG].mean()
    AvgScatterArray[i] = AllScatter.iloc[StartingPosition:StartingPosition+NUM_AVG].mean()
    #print AllScatter.iloc[StartingPosition:StartingPosition+NUM_AVG].mean()
    AvgScatterStdDev[i] = AllScatter.iloc[StartingPosition:StartingPosition+NUM_AVG].std()
    
#AvgData['AvgTimes']=AvgTimesArray  

for i in range(LengthOfAvg):
    
    StartPos = i*NUM_AVG+1
    CurrentAvg= data.iloc[:,StartPos:StartPos+NUM_AVG].mean(axis=1)
    CurrentStd= data.iloc[:,StartPos:StartPos+NUM_AVG].std(axis=1)
    CurrName = "%4.0f" % (AvgTimesArray[i]/3600.*1000)
    MeanAvgData[CurrName] = CurrentAvg
    StdAvgData["Std_"+CurrName] = CurrentStd

#AvgData.columns = AvgData.columns.sort_values()   
#print AvgData.head()
for i in range(LengthOfAvg):
    print i
    modelParamsDict["DecayTime"] = data[Decays]
    #print AvgData.iloc[:,i]
    #print MeanAvgData.iloc[:,i]
    Radius, RadVar = curve_fit(DFL.ExponentialModel, modelParamsDict, MeanAvgData.iloc[:,i], maxfev = 100000)
    print Radius
    RadiiArray[i] = Radius
    RadVarArray[i] = RadVar
    RadStdArray[i] = np.sqrt(RadVar)
    
    CurrName = "%4.0f" % (AvgTimesArray[i]/3600.*100)
    FitArray['Fit'+CurrName] = (DFL.ExponentialModel(modelParamsDict,Radius))
    
    R0 = np.sum((DFL.ExponentialModel(modelParamsDict,Radius) - MeanAvgData.iloc[:,i])**2)
    #print AvgR0
    R1 = np.sum((MeanAvgData.iloc[:,i] - np.mean(MeanAvgData.iloc[:,i]))**2)
    R2 = 1 - (R0/R1)
    R2Array[i] = R2
    
    #print R2

    if R2Array[i] < R2FILT:
##        #print 'hi'
        RadiiArray[i] = 0
        RadStdArray[i]= 0

ExtractedRadii = pd.DataFrame()
ExtractedRadii["hvSec"]=AvgTimesArray
ExtractedRadii["hvHr"]=AvgTimesArray/3600.
ExtractedRadii['Scat']=AvgScatterArray
ExtractedRadii['ScatStd']=AvgScatterStdDev
ExtractedRadii['Radii']=RadiiArray
ExtractedRadii['RadVar']=RadVarArray
ExtractedRadii['RadStd']=RadStdArray
ExtractedRadii['R2']=R2Array

ExtractedRadii= ExtractedRadii.add_prefix(AvgRadPrefix)

AvgData = pd.concat([MeanAvgData,StdAvgData,FitArray],axis=1)
AvgData['DecayTime']=data[Decays]
AvgData= AvgData.add_prefix(AvgCorrPrefix)


if SAVE_DATA == 'yes':
    AvgData.to_csv(AvgCorrPrefix+'.csv')
    ExtractedRadii.to_csv(AvgRadPrefix+'.csv')
else:
    print "DATA WAS NOT SAVED"
#if MAKE_GRAPHS == 'yes':
    


#    
#
#plt.plot(np.log10(AllDecayTime), AllNormCorr)
#plt.show()
#plt.close()
## =============================================================================
## Save and plot analyzed data
## =============================================================================
#
#
#
##RF.DLSPlot(AllTimes/3600, Radii,['Time (hours)', 'Radius (nm)'],'SizeNoAvg')
#DFL.DLSPlot(AvgTimes/3600, AvgRadii,['Time (hours)', 'Radius (nm)'],'SizeAvgCorrFiltpt5'+str(NUM_AVG))
#
##RF.DLSSaveData(AllTimes/3600, Radii,'SizeNoAvgFilt',FILE_PREFIX,R2, RadStdDev)
##DFL.DLSSaveData(AvgTimes/3600, AvgRadii,'SizeFiltpt5AvgCorr'+str(NUM_AVG),FILE_PREFIX, AvgR2,AvgRadStdDev)
##RF.DLSSaveData(AvgTimes/3600, AvgR2,'R2AvgCorr50',FILE_PREFIX)
##RF.DLSSaveData(AvgTimes/3600, AvgRadStdDev,'StdDevAvgCorr50',FILE_PREFIX)
#
##RF.DLSPlot(AllTimes/3600, AvgScatterPerCorrelation ,['Time (hours)', 'Scatter (kHz)'],'ScatterNoAvg')
#
##RF.DLSSaveData(AllTimes/3600, AvgScatterPerCorrelation,'ScatterNoAvgHr',FILE_PREFIX)