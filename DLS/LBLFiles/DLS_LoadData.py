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
os.chdir(Path0)
#ListFiles = pd.read_csv('AllFolders.csv')

FOLDER = os.getcwd()
#print FOLDER #prints the folder where the python code lives
DATARUN = "060120PSLs/dilute3/"
DATA_SUBFOLDER = "/"+DATARUN+"/" #where does the data live?
#DATA_SUBFOLDER = "/Test/"
FILE_EXTENSION ='*.ASC'
os.chdir(FOLDER+DATA_SUBFOLDER)
print os.getcwd() #prints where you are pulling data from
FILES = sorted(glob.glob(FILE_EXTENSION))
FILE_PREFIX = FILES[0][:-8]
#FILE_PREFIX = DATARUN+FILES[0][:-8]
print FILES

NUM_FILES = len(FILES)
print NUM_FILES #how many files are we dealing with

storage = 'extracted'
#print storage
isdir = os.path.isdir(storage)
#print isdir
if isdir == False:
    os.mkdir(storage)
##os.mkdir(storage+"/"+conditions)
    #os.mkdir(storage+"/figures")


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
[AllTimes, AllScatter, AllNormCorr, AllDecayTime] = DFL.ReadAllFiles(FILES,LineLocationsDict)
ScatterTime = pd.DataFrame()

ScatterTime[FILE_PREFIX+'AllTimes']=AllTimes
ScatterTime[FILE_PREFIX+'AllScatter']=AllScatter
#AllTimesNames =np.zeros(len(AllTimes))
#for entry in range(len(AllTimes)-1):
#AllTimesNames[entry] = str(int(AllTimes[entry]))

AllTimesNames = ["%.0f" % number for number in AllTimes]
#print AllTimesNames
    

DecayTimeIndex = AllDecayTime[0]
AllNormCorr = np.transpose(AllNormCorr)

RawNormCorr = pd.DataFrame(index = DecayTimeIndex, columns = AllTimesNames, dtype = 'float64')
RawNormCorr.index.name = FILE_PREFIX+'DecayTime'
RawNormCorr.columns.name = FILE_PREFIX+'PhotoTime'

for i in range(NUM_FILES):
    RawNormCorr.iloc[:,i] = AllNormCorr[:,i]
    
RawNormCorr = RawNormCorr.add_prefix(FILE_PREFIX+"PhotoTime")
#RawNormCorr['DecayTimes']=DecayTimeIndex
#print RawNormCorr
RawNormCorr.to_csv('./'+storage+'/'+FILE_PREFIX+"_RawNormCorr.csv")
ScatterTime.to_csv('./'+storage+'/'+FILE_PREFIX+"_RawScatter.csv")
# =============================================================================

