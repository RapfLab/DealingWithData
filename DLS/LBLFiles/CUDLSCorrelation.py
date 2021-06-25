#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 13:11:27 2020

@author: rebeccarapflbl
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import glob
import os
import pandas as pd
#import datetime
#import DLSFunctionLibrary as DFL

Path0 = '/Users/rebeccarapflbl/Desktop/ExperimentalData/DLS/CUDLSFilesAOs/'
os.chdir(Path0)
ListFiles = pd.read_csv('./testfolder.csv')


#data = pd.read_csv(filename)
#print data.head()
#NumMeasure = len(data.columns)-1
#print NumMeasure

#CleanedData = pd.DataFrame()



#os.chdir(Path0)
##print os.getcwd()
for idx, row in ListFiles.iterrows():
    p_file = row.FileNames
    prename = row.OutputNames
    print prename
    data = pd.read_csv("./CorrelationFunctions/"+p_file)
    
    
    data = data.dropna(axis=1)
    print data.head()
    
    NumMeasure = len(data.columns)-1
    print NumMeasure
    
#    length = range(0,61)
#    
    CleanedData = pd.DataFrame()
#    
#    AvgRadius = np.zeros(len(length))
#    AvgMeas = np.zeros(len(length))
    #a = np.zeros(5)
    #CleanedData['aa'] = a
    #print CleanedData
    SumNormCorr = np.zeros(len(data))
    SumUnNormCorr = np.zeros(len(data))
    SumNormAvg = 0
    for entry in range(NumMeasure):
        if entry == 0:
            CleanedData[prename+"DecayTime"] = data.iloc[:,0]
        
        CopyArray =  data.iloc[:,entry+1]
        CopyArray = CopyArray.sub(1)
        NormAvg = CopyArray[1:25].mean()
        #print NormAvg
        NormCopyArray = CopyArray.div(NormAvg)
        CleanedData[prename+"Corr"+str(entry)] = NormCopyArray
        
        SumNormAvg += NormAvg
        
        SumUnNormCorr += CopyArray
        SumNormCorr += NormCopyArray  
        
    AvgNormCorr = SumNormCorr/NumMeasure
    AvgUnNormCorr = SumUnNormCorr/SumNormAvg
    
    CleanedData[prename+"AvgNormCorr"] = AvgNormCorr
    CleanedData[prename+"AvgUnNormCorr"] = AvgUnNormCorr
    
    CleanedData.to_csv('./ExtractedPlateReaderData/'+prename+'CleanCorr.csv')

#CleanedData = CleanedData.sub(1)


    #print entry
    #dataname = "Data"+str(entry)
    #print dataname
    #data1 = 0
#    dataname = data
#    
#    dataname = dataname.dropna(subset = [dataname.columns[entry+1]])
#    dataname = dataname.dropna(axis=1)
#    #print data1.head()
#    #data1 = data1.reindex()
#    #print "Radius " + str(data1.iloc[0,0])
#    #print "Meas " + str(data1.iloc[0,1])
#    RadName = prename+'Radius'+str(entry)
#    MeasName = prename+str(entry)
#    
#    #print data1.iloc[:,entry]
#    
#    #data1[RadName]=data1.iloc[0,:]
#    #print RadName
#    RadiusCol = dataname.iloc[:,0].values.tolist()
#    MeasCol = dataname.iloc[:,1].values.tolist()
#    #print len(RadiusCol)
#    
#    #b = data1.iloc[:,1].values.tolist()
#    #print a
#    #blah =  data1.columns[0].to_list()
#    #print data1.iloc[:,1]
#    #print data1["Radius_nm"]
#    if len(RadiusCol) < len(length):
#        missing = len(length) - len(RadiusCol)
#        #print missing
#        RadiusCol.append(RadiusCol[len(RadiusCol)-1]+0.1) 
#        MeasCol.append(0)
#    AvgRadius += RadiusCol
#    AvgMeas += MeasCol
#    
#    #print AvgRadius
#    CleanedData[RadName] = RadiusCol
#    CleanedData[MeasName] = MeasCol
#
#AvgRadius = AvgRadius/NumMeasure
#AvgMeas = AvgMeas/NumMeasure
##print AvgRadius
#
#CleanedData[prename+"AvgRadius"] = AvgRadius
#CleanedData[prename+"AvgMeas"] = AvgMeas
#IndexNames = range(NumMeasure)+["avg"]
##print IndexNames
#
#PeakStatistics = pd.DataFrame(index = IndexNames)
##PeakStatistics = PeakStatistics.add_prefix(prename)
##print PeakStatistics
#for meas in range(NumMeasure+1):
#    #print meas*2
#    RadiiColumn = CleanedData.iloc[:,meas*2]
#    PerIntColumn = CleanedData.iloc[:,meas*2+1]
#    #print CleanedData.columns[meas*2]
##RadiiColumn = CleanedData.iloc[:,-2]
##PerIntColumn = CleanedData.iloc[:,-1]
#    SumWeights = 0
#    WeightBins = 0
#    CroppedRadii = []
#    CroppedWeights = []
#    peaknum = 0
#    
#    for entry in range(len(RadiiColumn)):
#        #print PerIntColumn[entry]
#
#        
#        PeakDetected = PerIntColumn[entry] != 0
#        OldPeakDetected = 0
#        if entry == 0:
#            OldPeakDetected = 0
#        elif entry >= 0:
#            OldPeakDetected = PerIntColumn[entry-1] != 0
#        #print PeakDetected
#        
#        if PeakDetected == True:
#            CroppedRadii.append(RadiiColumn[entry])
#            CroppedWeights.append(PerIntColumn[entry])
#            SumWeights += PerIntColumn[entry]
#            WeightBins += PerIntColumn[entry]*RadiiColumn[entry]
#            
#            #print SumWeights
#            #print WeightBins
#        elif OldPeakDetected == True:
#            peaknum += 1
#            
#            WeightedAvg = WeightBins/SumWeights
#            #print WeightedAvg
#            
#            Squares = CroppedWeights*(CroppedRadii - WeightedAvg)**2
#            SumSquares = sum(Squares)
#            WeightedStd = np.sqrt(SumSquares/SumWeights)
#            #print WeightedStd
#            
#            PercentPoly = WeightedStd/WeightedAvg
#            #print PercentPoly
#            
#            if PeakStatistics.get(prename+"Radius_Pk"+str(peaknum)) is None:
#                #print "hi"
#                PeakStatistics[prename+"Radius_Pk"+str(peaknum)] = np.zeros(NumMeasure+1)
#                PeakStatistics[prename+"Pd_Pk"+str(peaknum)]= np.zeros(NumMeasure+1)
#                PeakStatistics[prename+"PerPoly_Pk"+str(peaknum)] = np.zeros(NumMeasure+1)
#            #print "AAA " + str(peaknum)+" "+ str(PeakStatistics.get(prename+"Radius_Peak"+str(peaknum)))
#            #print meas
#            PeakStatistics.iloc[meas,(peaknum-1)*3] = WeightedAvg
#            #print PeakStatistics.iloc[peaknum,entry]
#            PeakStatistics.iloc[meas,((peaknum-1)*3+1)] = WeightedStd
#            PeakStatistics.iloc[meas,(peaknum-1)*3+2] = PercentPoly
#            
#            SumWeights = 0
#            WeightBins = 0
#            CroppedRadii = []
#            CroppedWeights = []
    #print RadiiColumncorr
    
    #data1.iloc[:,0].values.tolist()
    #CleanedData[MeasName] = b
    #print CleanedData
    #Trial = AvgData = pd.concat([Data1,Data2],axis=1)
    #print CleanedData
    #CleanedData.to_csv('./ExtractedPlateReaderData/'+prename+'CleanOutput.csv')
    #PeakStatistics.to_csv('./ExtractedPlateReaderData/'+prename+'PeakStats.csv')
    
    #AvgRadius = 