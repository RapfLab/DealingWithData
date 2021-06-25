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
Path0 = '/Users/rebeccarapflbl/Desktop/ExperimentalData/DLS/MIJ_DLS/CompiledExtractedData/Avg50Filter5Temp/'
#FOLDER = os.getcwd()
#print FOLDER #prints the folder where the python code lives
SAVE_DATA = 'yes'
PullCorr = "yes"

TimePoints = [1,2,3,4,5,6,8,10,15,100]
lenAvg = len(TimePoints)
R2FILTName = 5
R2FILT = R2FILTName/10.

os.chdir(Path0)
ListFiles = pd.read_csv('AllAvg50Filt5Temp.csv')
ListTwoFiles = ListFiles.loc[0:1]
ListTwoFilesB = ListFiles.loc[6:7]
#print ListTwoFiles

for i in range(len(TimePoints)):
    os.system("say starting next time point")
    namefolder = "ExtractedTime" + str(TimePoints[i]) + "Hours_Corr"
    isdir = os.path.isdir(namefolder)
    if isdir == False:
        os.mkdir(namefolder)
        os.mkdir("ExtractedTime" + str(TimePoints[i]) + "Hours_Radii")
    CompileData = pd.DataFrame()
    ReSetIndex = []
    #TempData = []
    for idx, row in ListFiles.iterrows():
        os.chdir(Path0)
        #print FileLocation
        File_Prefix = row.FilePrefix
        print File_Prefix
        Rad_File = row.RadiiFiles
        #print Rad_File
        Corr_File = row.CorrFiles
        #if os.path.getsize(Rad_File) > 500: 
        CorrData = pd.read_csv(Corr_File)
        RadiiData = pd.read_csv(Rad_File)
#
        CorrData = CorrData.drop('Unnamed: 0', axis = 1)
        RadiiData = RadiiData.drop('Unnamed: 0', axis = 1)
    
        if len(RadiiData) == 0:
            continue
    
        NUM_TIMES = (len(CorrData.columns)-1)/3
        
        RadiiTimes = RadiiData.iloc[:,1].values
        #print RadiiTimes
        AddedRow = 0
        for InnerIdx, InnerRow in RadiiData.iterrows():
            
            #print "InnerIdx"+str(InnerIdx)
            if round(InnerRow.iloc[1]) == TimePoints[i] and AddedRow == 0:
                ReSetIndex.append(File_Prefix)
                TempData = RadiiData.iloc[[InnerIdx]]
                TempData.columns = ["hvSec","hvHr","Scat","ScatStd","Radii","RadVar","RadStd","R2" ]
                CompileData = pd.concat([CompileData,TempData])
                AddedRow = 1
        if AddedRow == 0:
           ReSetIndex.append(File_Prefix)
           TempData = RadiiData.iloc[[-1]]
           TempData.columns = ["hvSec","hvHr","Scat","ScatStd","Radii","RadVar","RadStd","R2" ]
           CompileData = pd.concat([CompileData,TempData])
           
           
        if PullCorr == 'yes':
    
            CorrLength = len(CorrData.index)
            CorrCols = CorrData.columns[:NUM_TIMES]
            #print CorrData.columns
            #Decays = data.columns.values[0]
            #print "NUM TIMES " + str(NUM_TIMES) #how many files are we dealing with
            times = np.zeros(NUM_TIMES)
            timestring = []
        
            for entry in range(len(CorrCols)):
                #print CorrCols[entry]
                marker = CorrCols[entry].find("Avg50")
                endmarker = marker+5
                timestring.append(CorrCols[entry][endmarker:])
                #print (CorrCols[entry][endmarker:])
                times[entry] =(float(CorrCols[entry][endmarker:]))/1000
            #print times
            timeslength = len(timestring[entry])
            #timeslength = len(str(times[-1]))-1    
            AccessPoint = len(times)-1
            #print "Last Access Point " + str(AccessPoint)
            AccessName = CorrCols[-1][:-timeslength]
            Flag = np.zeros(CorrLength)
            Flag = Flag + 1
            
            PullRow = 0
            for entry in range(len(times)):
                if round(times[entry]) == TimePoints[i] and PullRow == 0:
                    #print times[entry]
                    #print timestring[entry]
                    timeslength = len(timestring[entry])
                    
                    AccessPoint = entry
                    AccessName = CorrCols[entry][:-timeslength]
                    Flag = np.zeros(CorrLength)
                    PullRow = 1
                    print "AccessName " +AccessName
            
            
            
            PullCorrData = pd.DataFrame()
            PullCorrData[File_Prefix+'DecayTimes'] = CorrData.iloc[:,-1]
            PullCorrData[File_Prefix+'Corr'] = CorrData[AccessName+timestring[AccessPoint]]
            PullCorrData[File_Prefix+'Std'] = CorrData[AccessName+"Std_"+timestring[AccessPoint]]
            PullCorrData[File_Prefix+'Fit'] = CorrData[AccessName+"Fit"+timestring[AccessPoint]]
            PullCorrData[File_Prefix+'Flag'] = Flag
            #print PullCorrData.columns
            PullCorrData.to_csv(namefolder+"/"+File_Prefix+"_"+timestring[AccessPoint]+".csv")
    CompileData.index = ReSetIndex  
    CompileData.to_csv("ExtractedTime" + str(TimePoints[i]) + "Hours_Radii"+"/"+"ExtractRad"+str(TimePoints[i])+"Hrs.csv")
os.system("say all done")#
