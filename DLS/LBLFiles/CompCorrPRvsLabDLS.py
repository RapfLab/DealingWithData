#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:20:30 2019

@author: rebeccarapflbl
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
import glob
import os
import pandas as pd
#import datetime
import DLSFunctionLibrary as DFL

# =============================================================================
# FILE DETAILS
# =============================================================================
Path0 = '/Users/rebeccarapflbl/Desktop/ExperimentalData/DLS/Alina/CompiledExtractedData/'
#FOLDER = os.getcwd()
#print FOLDER #prints the folder where the python code lives
SAVE_DATA = 'yes'

os.chdir(Path0)
ListFiles = pd.read_csv('CompCorrPSLLabvsPlateReader.csv')


namefolder = "CompPlateReaderLabDLS"
isdir = os.path.isdir(namefolder)
if isdir == False:
    os.mkdir(namefolder)

PathLabDLS = "./"
PathPRDLS = "../PlateReaderCorrelation/"
#print ListFiles.head()
ListFiles = ListFiles.drop(ListFiles.columns[0], axis = 1)
ListFiles = ListFiles.dropna(axis = 1)
ListTwoFiles = ListFiles.loc[6:7]
#print ListFiles.head()
#data = data.drop(data.columns[0], axis = 1)

for idx, row in ListFiles.iterrows():
    print row.LabCorrFiles
    PlateReaderData = pd.read_csv(PathPRDLS+row.PRFileNames)
    
    PlateReaderData = PlateReaderData.drop(PlateReaderData.index[0])
    PlateReaderData = PlateReaderData.drop(PlateReaderData.columns[0], axis = 1)
    PlateReaderData = PlateReaderData.dropna(axis = 1)
    
    PRDecayTimes = PlateReaderData.iloc[:,0]
    
    PRCorrFunc = PlateReaderData.iloc[:,-1].values
    #print PRCorrFunc
    ReducedPRDecayTimes = []
    ReducedPRCorrFunc = []
    
    InterpPR = interp1d(PRDecayTimes, PRCorrFunc,kind = 'linear')
    xnew = np.logspace(-0.6,6.68, num =183, endpoint = True)
    #print xnew

    
    LabData = pd.read_csv(PathLabDLS+row.LabCorrFiles)
    
    LabData = LabData.drop(LabData.columns[0], axis = 1)
    LabData = LabData.dropna(axis = 1)
    
    LabDecayTimes = LabData.iloc[:,3]*1000
    #print LabDecayTimes
    LabCorrFunc = LabData.iloc[:,0].values
    print LabCorrFunc
    ReducedLabDecayTimes = []
    ReducedLabCorrFunc = []
    
    InterpLab = interp1d(LabDecayTimes, LabCorrFunc,kind = 'linear')
    
    LabInterpCorrFunc = InterpLab(xnew)
    PRInterpCorrFunc = InterpPR(xnew)
    
    DiffCorrFunc = PRInterpCorrFunc - LabInterpCorrFunc #"Residuals" -- element-wise difference
    SqDiffCorrFunc = DiffCorrFunc**2
    SumDiff = np.sum(SqDiffCorrFunc)
    print SumDiff
    
    plt.plot(xnew, InterpPR(xnew), 'x',xnew, InterpLab(xnew), "o", LabDecayTimes, LabCorrFunc, "-", xnew, SqDiffCorrFunc, "*" )
    plt.xscale('log')
    plt.show()
    
    #    
    modelParamsDict = DFL.initializeExponentialModelParams();
#   
#    for point in range(len(LabDecayTimes)):
#        if LabDecayTimes[point]*2.% 1 == 0:
#            ReducedLabDecayTimes.append(LabDecayTimes[point])
#    for entry in range(len(LabDecayTimes)):
#        for item in range(len(PRDecayTimes)):
#            if PRDecayTimes[item]==LabDecayTimes[entry]:
#                ReducedLabDecayTimes.append(LabDecayTimes[entry])
#                ReducedPRDecayTimes.append(PRDecayTimes[item])
#                ReducedLabCorrFunc.append(LabCorrFunc[entry])
#                ReducedPRCorrFunc.append(PRCorrFunc[item])
    
#    R0 = np.sum((DFL.ExponentialModel(modelParamsDict,LabInterpCorrFunc) - PRInterpCorrFunc)**2)
#    #print AvgR0
#    R1 = np.sum((LabInterpCorrFunc - np.mean(LabInterpCorrFunc)**2))
#    R2 = 1 - (R0/R1)
#    R2Array[i] = R2
    
    CompilePRData = pd.DataFrame(index = PRDecayTimes)
    #CompileData["PRDecayTimes"] = PRDecayTimes
    CompilePRData["PRCorrFunc"] = PRCorrFunc
    CompileLabData= pd.DataFrame(index = LabDecayTimes)
    CompileLabData["LabCorrFunc"] =    LabCorrFunc
    
    #CompileData = [CompilePRData,CompileLabData]
    CompileData = pd.concat([CompilePRData,CompileLabData], axis = 1, sort=True)
    
    #hist = CompileData.hist()
    #CompileData.to_csv("test.csv")
#NUM_AVG = [1,5,10,25,50,100,250,500]
#lenAvg = len(NUM_AVG)
#R2FILTName = 5
#R2FILT = R2FILTName/10.
#
#os.chdir(Path0)
#ListFiles = pd.read_csv('AllPhotoNamesRestart2.csv')
#
#for i in range(lenAvg):
#    namefolder = "Avg" + str(NUM_AVG[i])+"Filter"+str(R2FILTName)
#    isdir = os.path.isdir(namefolder)
#    if isdir == False:
#        os.mkdir(namefolder)
#
#for idx, row in ListFiles.iterrows():
#    os.chdir(Path0)
#    #print FileLocation
#    File_Prefix = row.FilePrefix
#    print File_Prefix
#    Scatter_File = row.ScatterFiles
#    Corr_File = row.CorrFiles
#
#    data = pd.read_csv(Corr_File)
#    ScatterTime = pd.read_csv(Scatter_File)
##
#    NUM_FILES = len(data.columns)-1
#    CorrLength = len(data.index)
#    Decays = data.columns.values[0]
#    print NUM_FILES #how many files are we dealing with
#    
#    
#    #print MeanAvgData.iloc[:,7507]
#    # =============================================================================
#    # 
#    # =============================================================================
 
#    
#    # =============================================================================
#    
#    # =============================================================================
#    MeanAvgData = 0
#    for entry in range(len(NUM_AVG)):
#        print NUM_AVG[entry]
#        
#        outputfolder = "Avg" + str(NUM_AVG[entry])+"Filter"+str(R2FILTName)
#        
#        AvgCorrPrefix = File_Prefix+'Corr_Avg'+str(NUM_AVG[entry])
#        AvgRadPrefix =File_Prefix+'Rad_Avg'+str(NUM_AVG[entry])+'_Fpt'+str(R2FILTName)
#        AllTime = ScatterTime.iloc[:,1]
#        AllScatter = ScatterTime.iloc[:,2]
#    
#        LengthOfAvg = NUM_FILES/NUM_AVG[entry]
#        print LengthOfAvg
#        print "Length of AVG"+str(LengthOfAvg)
#        AvgData = pd.DataFrame()
#        MeanAvgData = pd.DataFrame()
#        StdAvgData = pd.DataFrame()
#        AvgTimesArray = np.zeros(LengthOfAvg)
#        RadiiArray = np.zeros(LengthOfAvg)
#        RadVarArray = np.zeros(LengthOfAvg)
#        RadStdArray = np.zeros(LengthOfAvg)
#        AvgScatterArray = np.zeros(LengthOfAvg)
#        AvgScatterStdDev = np.zeros(LengthOfAvg)
#        R2Array = np.zeros(LengthOfAvg)
#        FitArray = pd.DataFrame()
#
#        for i in range(LengthOfAvg):
#            StartingPosition = i*NUM_AVG[entry]
#            #print AllTime.iloc[StartingPosition:StartingPosition+NUM_AVG]
#            AvgTimesArray[i] = AllTime.iloc[StartingPosition:StartingPosition+NUM_AVG[entry]].mean()
#            #print AvgTimesArray[i]
#            AvgScatterArray[i] = AllScatter.iloc[StartingPosition:StartingPosition+NUM_AVG[entry]].mean()
#            #print AllScatter.iloc[StartingPosition:StartingPosition+NUM_AVG].mean()
#            AvgScatterStdDev[i] = AllScatter.iloc[StartingPosition:StartingPosition+NUM_AVG[entry]].std()
#            
#        #AvgData['AvgTimes']=AvgTimesArray  
##        
#        for i in range(LengthOfAvg):
#            #print i
#            StartPos = i*NUM_AVG[entry]+1
#            CurrentAvg= data.iloc[:,StartPos:StartPos+NUM_AVG[entry]].mean(axis=1)
#            CurrentStd= data.iloc[:,StartPos:StartPos+NUM_AVG[entry]].std(axis=1)
#            CurrName = "%4.0f" % (AvgTimesArray[i]/3600.*1000)
#            #CurrName =  (AvgTimesArray[i]/3600.*1000)
##            if CurrName in MeanAvgData.columns:
##                print i
##                print CurrName
#                
#                
#            
#            MeanAvgData[CurrName] = CurrentAvg
#            StdAvgData["Std_"+CurrName] = CurrentStd
#            
#        LengthOfAvg = len(MeanAvgData.columns)
#
#
#        #AvgData.columns = AvgData.columns.sort_values()   
#        #print AvgData.head()
#        for i in range(LengthOfAvg):
#            #print i
#            modelParamsDict["DecayTime"] = data[Decays]
#            #print AvgData.iloc[:,i]
#            Radius, RadVar = curve_fit(DFL.ExponentialModel, modelParamsDict, MeanAvgData.iloc[:,i], maxfev = 100000)
#            #print Radius
#            RadiiArray[i] = Radius
#            RadVarArray[i] = RadVar
#            RadStdArray[i] = np.sqrt(RadVar)
#            #print MeanAvgData.iloc[:,7507]
#            CurrName = "%4.0f" % (AvgTimesArray[i]/3600.*1000)
#            FitArray['Fit'+CurrName] = (DFL.ExponentialModel(modelParamsDict,Radius))
#            
#            R0 = np.sum((DFL.ExponentialModel(modelParamsDict,Radius) - MeanAvgData.iloc[:,i])**2)
#            #print AvgR0
#            R1 = np.sum((MeanAvgData.iloc[:,i] - np.mean(MeanAvgData.iloc[:,i]))**2)
#            R2 = 1 - (R0/R1)
#            R2Array[i] = R2
#            
#            #print R2
#        
#            if R2Array[i] < R2FILT:
#        ##        #print 'hi'
#                RadiiArray[i] = 0
#                RadStdArray[i]= 0
#        
#        ExtractedRadii = pd.DataFrame()
#        ExtractedRadii["hvSec"]=AvgTimesArray
#        ExtractedRadii["hvHr"]=AvgTimesArray/3600.
#        ExtractedRadii['Scat']=AvgScatterArray
#        ExtractedRadii['ScatStd']=AvgScatterStdDev
#        ExtractedRadii['Radii']=RadiiArray
#        ExtractedRadii['RadVar']=RadVarArray
#        ExtractedRadii['RadStd']=RadStdArray
#        ExtractedRadii['R2']=R2Array
#        
#        ExtractedRadii= ExtractedRadii.add_prefix(AvgRadPrefix)
#        
#        AvgData = pd.concat([MeanAvgData,StdAvgData,FitArray],axis=1)
#        AvgData['DecayTime']=data[Decays]
#        AvgData= AvgData.add_prefix(AvgCorrPrefix)
#        
#        
#        if SAVE_DATA == 'yes':
#            AvgData.to_csv(outputfolder+"/"+AvgCorrPrefix+'.csv')
#            ExtractedRadii.to_csv(outputfolder+"/"+AvgRadPrefix+'.csv')
#        else:
#            print "DATA WAS NOT SAVED"
#    #if MAKE_GRAPHS == 'yes':
#        
#    
