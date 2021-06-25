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

Path0 = '/Users/rebeccarapflbl/Desktop/ExperimentalData/DLS/CUDLS/'
os.chdir(Path0)
ListFiles = pd.read_csv('./testfolder.csv')
#WorkingList = ListFiles.FileNames
#OutputNames = ListFiles.OutputNames
#filename = '20200313_OOAandPA_Histo.csv'

#prename = '200312_OOAandPA'

#os.chdir(Path0)
#print os.getcwd()
CompileData = pd.DataFrame()

for idx, row in ListFiles.iterrows():
    p_file = row.FileNames
    prename = row.OutputNames
    print prename
    data = pd.read_excel(p_file)
    
    NumMeasure = len(data.columns)-1
    print NumMeasure
    
    length = range(0,61)
    
    CleanedData = pd.DataFrame(index = length)
    
    AvgRadius = np.zeros(len(length))
    AvgMeas = np.zeros(len(length))
    #a = np.zeros(5)
    #CleanedData['aa'] = a
    #print CleanedData
    
    for entry in range(NumMeasure):

        dataname = data
        
        dataname = dataname.dropna(subset = [dataname.columns[entry+1]])
        dataname = dataname.dropna(axis=1)

        RadName = prename+'Radius'+str(entry)
        MeasName = prename+str(entry)
        

        RadiusCol = dataname.iloc[:,0].values.tolist()
        MeasCol = dataname.iloc[:,1].values.tolist()
        #print len(RadiusCol)
        

        if len(RadiusCol) < len(length):
            missing = len(length) - len(RadiusCol)
            #print missing
            RadiusCol.append(RadiusCol[len(RadiusCol)-1]+0.1) 
            MeasCol.append(0)
        AvgRadius += RadiusCol
        AvgMeas += MeasCol
        
        #print AvgRadius
        CleanedData[RadName] = RadiusCol
        CleanedData[MeasName] = MeasCol
    
    AvgRadius = AvgRadius/NumMeasure
    AvgMeas = AvgMeas/NumMeasure
    #print AvgRadius
    CleanedFinalData = pd.DataFrame()
    CleanedFinalData[prename+"AvgRadius"] = AvgRadius
    CleanedFinalData[prename+"AvgMeas"] = AvgMeas
    CleanedFinalData = pd.concat([CleanedFinalData,CleanedData],axis=1)
    IndexNames = ["avg"]+range(NumMeasure)+["std"]
    #print IndexNames
    
    PeakStatistics = pd.DataFrame(index = IndexNames)
    AvgOnlyPeakStatistics = pd.DataFrame(index = [prename])
    #PeakStatistics = PeakStatistics.add_prefix(prename)
    #print PeakStatistics
    StartBin = []
    EndBin = []
    for meas in range(NumMeasure+1):
        #print meas*2
        RadiiColumn = CleanedFinalData.iloc[:,meas*2]
        PerIntColumn = CleanedFinalData.iloc[:,meas*2+1]
        #print CleanedData.columns[meas*2]
    #RadiiColumn = CleanedData.iloc[:,-2]
    #PerIntColumn = CleanedData.iloc[:,-1]
        SumWeights = 0
        WeightBins = 0
        CroppedRadii = []
        CroppedWeights = []
        peaknum = 0
        
        for entry in range(len(RadiiColumn)):
            #print PerIntColumn[entry]
    
            
            PeakDetected = PerIntColumn[entry] != 0
            OldPeakDetected = 0
            if entry == 0:
                OldPeakDetected = 0
            elif entry >= 0:
                OldPeakDetected = PerIntColumn[entry-1] != 0
            #print PeakDetected
            
            if PeakDetected == True:
                CroppedRadii.append(RadiiColumn[entry])
                CroppedWeights.append(PerIntColumn[entry])
                SumWeights += PerIntColumn[entry]
                WeightBins += PerIntColumn[entry]*RadiiColumn[entry]
                
                #print SumWeights
                #print WeightBins
            elif OldPeakDetected == True:
                peaknum += 1
                #print peaknum
                
                WeightedAvg = WeightBins/SumWeights
                #print WeightedAvg
                
                Squares = CroppedWeights*(CroppedRadii - WeightedAvg)**2
                SumSquares = sum(Squares)
                WeightedStd = np.sqrt(SumSquares/SumWeights)
                #print WeightedStd
                
                PercentPoly = WeightedStd/WeightedAvg
                #print PercentPoly
                
                if PeakStatistics.get(prename+"Radius_Pk"+str(peaknum)) is None:
                    #print "hi"
                    PeakStatistics[prename+"Radius_Pk"+str(peaknum)] = np.zeros(len(IndexNames))
                    PeakStatistics[prename+"Pd_Pk"+str(peaknum)]= np.zeros(len(IndexNames))
                    PeakStatistics[prename+"PerPoly_Pk"+str(peaknum)] = np.zeros(len(IndexNames))
                    
                    
                    
                #print "AAA " + str(peaknum)+" "+ str(PeakStatistics.get(prename+"Radius_Peak"+str(peaknum)))
                #print meas
                if meas == 0:
                    StartBin.append(CroppedRadii[0])
                    EndBin.append(CroppedRadii[-1])
                    #print StartBin
                    #print EndBin
                    PeakStatistics.iloc[meas,(peaknum-1)*3] = WeightedAvg
                    #print PeakStatistics.iloc[peaknum,entry]
                    PeakStatistics.iloc[meas,((peaknum-1)*3+1)] = WeightedStd
                    PeakStatistics.iloc[meas,(peaknum-1)*3+2] = PercentPoly
                    
                    AvgOnlyPeakStatistics["Radius_Pk"+str(peaknum)] = WeightedAvg
                    AvgOnlyPeakStatistics["Pd_Pk"+str(peaknum)] = WeightedStd
                    AvgOnlyPeakStatistics["PerPoly_Pk"+str(peaknum)] = PercentPoly
                    
                else:
                    NumPeaks = len(StartBin)
                    #print NumPeaks
                    for peak in range(NumPeaks):
                        if WeightedAvg > StartBin[peak] and WeightedAvg < EndBin[peak]:
                            #print StartBin[peak], EndBin[peak]
#                            PeakStatistics.iloc[meas,(peak)*3] = WeightedAvg
##                                #print PeakStatistics.iloc[peaknum,entry]
#                            PeakStatistics.iloc[meas,((peak)*3+1)] = WeightedStd
#                            PeakStatistics.iloc[meas,(peak)*3+2] = PercentPoly
                            if PeakStatistics.iloc[meas,(peak)*3] == 0:
                                PeakStatistics.iloc[meas,(peak)*3] = WeightedAvg
                                #print PeakStatistics.iloc[peaknum,entry]
                                PeakStatistics.iloc[meas,((peak)*3+1)] = WeightedStd
                                PeakStatistics.iloc[meas,(peak)*3+2] = PercentPoly
                            else:
                                #print meas, peak
                                print "shifting to not rewrite"
                                print PeakStatistics.iloc[meas,(peak)*3]
                                print "filling" + str(meas) +"and "+  str((peak+1)*3)
                                PeakStatistics.iloc[meas,(peak+1)*3] = WeightedAvg
                                #print PeakStatistics.iloc[peaknum,entry]
                                PeakStatistics.iloc[meas,((peak+1)*3+1)] = WeightedStd
                                PeakStatistics.iloc[meas,(peak+1)*3+2] = PercentPoly
                
                SumWeights = 0
                WeightBins = 0
                CroppedRadii = []
                CroppedWeights = []
    #print AvgOnlyPeakStatistics       
    for cols in range(len(PeakStatistics.columns)):
        print len(PeakStatistics.columns)
        PeakStatistics.iloc[-1,cols] = PeakStatistics.iloc[1:-2,cols].std() 
        print cols
        print str(AvgOnlyPeakStatistics.columns[cols])+"_Std"
        AvgOnlyPeakStatistics[AvgOnlyPeakStatistics.columns[cols]+"_Std"] = PeakStatistics.iloc[1:-2,cols].std()     
                
    CompileData = pd.concat([CompileData,AvgOnlyPeakStatistics], sort = False)        
    #print CompileData  

    #print RadiiColumncorr
    
    #data1.iloc[:,0].values.tolist()
    #CleanedData[MeasName] = b
    #print CleanedData
    #Trial = AvgData = pd.concat([Data1,Data2],axis=1)
    #print CleanedData
    CleanedFinalData.to_csv('./ExtractedData/'+prename+'CleanOutput.csv')
    PeakStatistics.to_csv('./ExtractedData/'+prename+'PeakStats.csv')
#print ListFiles.FattyAcidID

#CompileData["FattyAcidID"] = ListFiles.FattyAcidID.get_values()
CompileData["PlateReaderFileName"] = ListFiles.FileNames.get_values()

CompileData.to_csv('./ExtractedData/'+'CompiledOutput.csv')


    #AvgRadius = 