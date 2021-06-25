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
Path0 = '/Users/rebeccarapflbl/Desktop/ExperimentalData/DLS/MIJ_DLS/CompiledExtractedData'
#FOLDER = os.getcwd()
#print FOLDER #prints the folder where the python code lives
SAVE_DATA = 'yes'

NUM_AVG = [50]

#NUM_AVG = [3,5,25,50,100] #maybe reverse order for speed
lenAvg = len(NUM_AVG)
R2FILTName = 5
R2FILT = R2FILTName/10.

os.chdir(Path0)
ListFiles = pd.read_csv('TempSeriesNAmes.csv')

for i in range(lenAvg):
    namefolder = "Avg" + str(NUM_AVG[i])+"Filter"+str(R2FILTName)+"Temp"
    isdir = os.path.isdir(namefolder)
    if isdir == False:
        os.mkdir(namefolder)

for idx, row in ListFiles.iterrows():
    os.chdir(Path0)
    #print FileLocation
    File_Prefix = row.FilePrefix
    print File_Prefix
    Scatter_File = row.ScatterFiles
    Temp = row.Temperature
    
    Corr_File = row.CorrFiles

    data = pd.read_csv(Corr_File)
    print len(data.columns)-1
    #print len(data)
    data = data.dropna(axis = 1)
    #print len(data)
    ScatterTime = pd.read_csv(Scatter_File)
    print Scatter_File
    print len(ScatterTime)
    ScatterTime = ScatterTime.dropna()
    print len(ScatterTime)
#
    NUM_FILES = len(data.columns)-1
    CorrLength = len(data.index)
    Decays = data.columns.values[0]
    print NUM_FILES #how many files are we dealing with
    
    
    #print MeanAvgData.iloc[:,7507]
    # =============================================================================
    # 
    # =============================================================================
    
    modelParamsDict = DFL.initializeExponentialModelParams(Temp);
    
    
    # =============================================================================
    
    # =============================================================================
    MeanAvgData = 0
    for entry in range(len(NUM_AVG)):
        print NUM_AVG[entry]
        
        outputfolder = "Avg" + str(NUM_AVG[entry])+"Filter"+str(R2FILTName)+"Temp"
        
        AvgCorrPrefix = File_Prefix+'OffSEtCorr_Avg'+str(NUM_AVG[entry])
        AvgRadPrefix =File_Prefix+'OffsetRad_Avg'+str(NUM_AVG[entry])+'_Fpt'+str(R2FILTName)
        AllTime = ScatterTime.iloc[:,1]
        AllScatter = ScatterTime.iloc[:,2]
    
        LengthOfAvg = NUM_FILES/NUM_AVG[entry]
        print LengthOfAvg
        print "Length of AVG"+str(LengthOfAvg)
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
            StartingPosition = i*NUM_AVG[entry]
            #print AllTime.iloc[StartingPosition:StartingPosition+NUM_AVG]
            AvgTimesArray[i] = AllTime.iloc[StartingPosition:StartingPosition+NUM_AVG[entry]].mean()
            #print AvgTimesArray[i]
            AvgScatterArray[i] = AllScatter.iloc[StartingPosition:StartingPosition+NUM_AVG[entry]].mean()
            #print AllScatter.iloc[StartingPosition:StartingPosition+NUM_AVG].mean()
            AvgScatterStdDev[i] = AllScatter.iloc[StartingPosition:StartingPosition+NUM_AVG[entry]].std()
            
        #AvgData['AvgTimes']=AvgTimesArray  
#        
        for i in range(LengthOfAvg):
            #print i
            StartPos = i*NUM_AVG[entry]+1
            CurrentAvg= data.iloc[:,StartPos:StartPos+NUM_AVG[entry]].mean(axis=1)
            CurrentStd= data.iloc[:,StartPos:StartPos+NUM_AVG[entry]].std(axis=1)
            CurrName = "%4.0f" % (AvgTimesArray[i]/3600.*1000)
            #CurrName =  (AvgTimesArray[i]/3600.*1000)
#            if CurrName in MeanAvgData.columns:
#                print i
#                print CurrName
                
                
            
            MeanAvgData[CurrName] = CurrentAvg
            StdAvgData["Std_"+CurrName] = CurrentStd
            
        LengthOfAvg = len(MeanAvgData.columns)


        #AvgData.columns = AvgData.columns.sort_values()   
        #print AvgData.head()
        for i in range(LengthOfAvg):
            #print i
            modelParamsDict["DecayTime"] = data[Decays]
            #print AvgData.iloc[:,i]
            Radius, RadVar = curve_fit(DFL.ExponentialModel, modelParamsDict, MeanAvgData.iloc[:,i], maxfev = 100000)
            #print Radius
            RadiiArray[i] = Radius
            RadVarArray[i] = RadVar
            RadStdArray[i] = np.sqrt(RadVar)
            #print MeanAvgData.iloc[:,7507]
            CurrName = "%4.0f" % (AvgTimesArray[i]/3600.*1000)
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
            AvgData.to_csv(outputfolder+"/"+AvgCorrPrefix+'.csv')
            ExtractedRadii.to_csv(outputfolder+"/"+AvgRadPrefix+'.csv')
        else:
            print "DATA WAS NOT SAVED"
    #if MAKE_GRAPHS == 'yes':
        
    
    #Radii = np.zeros(NUM_FILES)
    #RadiiVariance = np.zeros(NUM_FILES)
    #RadStdDev = np.zeros(NUM_FILES)
    #
    #AvgCorr = np.zeros(CorrLength)
    #AvgRadii = np.zeros((NUM_FILES/NUM_AVG))
    #AvgRadStdDev = np.zeros((NUM_FILES/NUM_AVG))
    #AvgTimes = np.zeros((NUM_FILES/NUM_AVG))
    #
    #R2 =[]
    #AvgR2 = []
    #
    #counter = 0
    #index = 0
    #
    ##testarray = np.array([[0, 1, 2, 3],[4,5,6,7],[8, 9, 10, 11]])
    ##
    ##aa = testarray[0:2,:]
    #
    #
    ##print aa
    #
    #for i in range(NUM_FILES/NUM_AVG):
    #    #print i
    #    
    #    modelParamsDict["DecayTime"] = data[Decays]
    #    Radius, RadVar = curve_fit(DFL.ExponentialModel, modelParamsDict, data.iloc[:,i+1], maxfev = 100000)
    #    #print data.iloc[:,i+1]
    #
    #    
    #    AvgCorr = np.zeros(LineLocationsDict.get('CORRELATION_LENGTH'))
    #    while counter < NUM_AVG:
    #        AvgCorr = AvgCorr + AllNormCorr[(index)]
    #        index += 1
    #        counter += 1
    #        #print AvgCorr
    #    counter = 0
    #
    #    
    #    
    #
    #    #Radius, RadVar = curve_fit(DFL.ExponentialModel, DecayTime, NormCorr, maxfev = 100000)
    #    
    #    
    #    if (i+1)%NUM_AVG == 0:
    #        #print i
    #        AvgCorr = np.true_divide(AvgCorr, NUM_AVG)
    #        
    #        AvgTime = np.true_divide(sum(AllTimes[(i-NUM_AVG+1):i+1]), NUM_AVG)
    #        #print AllTimes[(i-NUM_AVG+1):i+1]
    #        AvgTimes[i/NUM_AVG] = AvgTime
    #        #print AvgCorr
    #        AvgRadius, AvgRadVar = curve_fit(DFL.ExponentialModel, modelParamsDict, AvgCorr, maxfev = 100000)
    ##        if AvgRadius > 500:
    ##            AvgRadius = 0
    #        AvgRadii[i/NUM_AVG] = AvgRadius
    #        AvgRadStdDev[i/NUM_AVG] = np.sqrt(np.diag(AvgRadVar))
    #        
    #        AvgR0 = np.sum((DFL.ExponentialModel(modelParamsDict, AvgRadii[i/NUM_AVG]) - AvgCorr)**2)
    #        AvgR1 = np.sum((AvgCorr - np.mean(AvgCorr))**2)
    #        AvgR2 = np.append(AvgR2, 1 - (AvgR0/AvgR1)) 
    #        
    #        if AvgR2[i/NUM_AVG] < R2FILT:
    #            AvgRadii[i/NUM_AVG] = 0
    #            AvgRadStdDev[i/NUM_AVG] = 0
    ##        if AvgRadii[i/NUM_AVG]>200:
    ##            AvgRadii[i/NUM_AVG] = 0
    ##            AvgRadStdDev[i/NUM_AVG] = 0
    #        
    #        AvgCorr = np.zeros(LineLocationsDict.get("CORRELATION_LENGTH"))
    #        #print AvgRadius
    #        counter = 0
    #
    #    #Radius, RadVar = curve_fit(ExponentialModel, DecayTime, NormCorr, maxfev = 100000)
    ##    if Radius > 500:
    ##        Radius = 0
    #
    #    
    #    Radii[i] = Radius
    #    RadiiVariance[i] = RadVar
    #    RadStdDev[i] = np.sqrt(np.diag(RadVar))
    #    
    #    #R**2 goodness of fit paramter
    #    R0 = np.sum((DFL.ExponentialModel(modelParamsDict, Radii[i]) - AllNormCorr)**2)
    #    R1 = np.sum((AllNormCorr - np.mean(AllNormCorr))**2)
    #    R2 = np.append(R2, 1 - (R0/R1)) 
    #    
    ##    if R2[i] < 0.7:
    ##        #print 'hi'
    ##        Radii[i] = 0
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