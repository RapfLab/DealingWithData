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

Path0 = '/Users/rebeccarapflbl/Desktop/ExperimentalData/DLS/MIJ_DLS/'
os.chdir(Path0)
ListFiles = pd.read_csv('NoSpin_Fig3.csv')
#print ListFiles.columns

storage = "CompiledExtractedData"
isdir = os.path.isdir(storage)
if isdir == False:
    os.mkdir(storage)

BadFiles = pd.DataFrame()
for idx, row in ListFiles.iterrows():
    os.chdir(Path0)
    FileLocation = row.FolderNames
    #print FileLocation
    File_Prefix = row.OutputNames

    OutputLabel = row.OutputNames
#    isdir = os.path.isdir(storage+"/"+OutputLabel)
#    if isdir == False:
#        os.mkdir(storage+"/"+OutputLabel)

    FILE_EXTENSION ='*.ASC'
    os.chdir(FileLocation)
    print os.getcwd() #prints where you are pulling data from
    FILES = sorted(glob.glob(FILE_EXTENSION))

    NUM_FILES = len(FILES)
    print NUM_FILES #how many files are we dealing with
#
#storage = DATARUN+'extracted'
#isdir = os.path.isdir(storage)
#if isdir == False:
#    os.mkdir(storage)
###os.mkdir(storage+"/"+conditions)
#    #os.mkdir(storage+"/figures")
#
#
    LineLocationsDict = {"DATE_LINE": 2,
                         "TIME_LINE": 3,
                         "HEADER_LENGTH":23, #remaining lines in header (so full header is 3+HEADER_LENGTH)
                         "CORRELATION_LENGTH": 190,#207,#215,#190, #number of lines/datapoints in correlation function data
                         "SPACE_BETWEEN": 3, #lines between correlation function data and scatter intensity data
                         "COUNTS_LENGTH" : 254}
    
    # =============================================================================
    # 
    # =============================================================================
    
    modelParamsDict = DFL.initializeExponentialModelParams();
    
    # =============================================================================
    # READ IN ALL FILES 
    # =============================================================================
    RawNormCorr = 0
    [AllTimes, AllScatter, AllNormCorr, AllDecayTime, BadFileInfo] = DFL.ReadAllFiles(FILES,LineLocationsDict)
    #print BadFileInfo
    ScatterTime = pd.DataFrame()
    
    ScatterTime[OutputLabel+'AllTimes']=AllTimes
    ScatterTime[OutputLabel+'AllScatter']=AllScatter
    #AllTimesNames =np.zeros(len(AllTimes))
    #for entry in range(len(AllTimes)-1):
    #AllTimesNames[entry] = str(int(AllTimes[entry]))
    
    AllTimesNames = ["%.0f" % number for number in AllTimes]
    #print AllTimesNames                                                                                                    

    DecayTimeIndex = AllDecayTime[0]
    AllNormCorr = np.transpose(AllNormCorr)
    
    RawNormCorr = pd.DataFrame(index = DecayTimeIndex, columns = AllTimesNames, dtype = 'float64')
    RawNormCorr.index.name = OutputLabel+'DecayTime'
    RawNormCorr.columns.name = OutputLabel+'PhotoTime'
    
    for i in range(NUM_FILES):
        
        RawNormCorr.iloc[:,i] = AllNormCorr[:,i]
        
    RawNormCorr = RawNormCorr.add_prefix(OutputLabel+"PhotoTime")
    #RawNormCorr['DecayTimes']=DecayTimeIndex
    #print RawNormCorr
    os.chdir(Path0)
    RawNormCorr.to_csv('./'+storage+'/'+OutputLabel+"Offset2_RawNormCorrTest.csv")
    ScatterTime.to_csv('./'+storage+'/'+OutputLabel+"Offset2_RawScatterTest.csv")
    BadFiles = BadFiles.append(BadFileInfo)
BadFiles.to_csv(Path0+"BadFiles.csv")
# =============================================================================

