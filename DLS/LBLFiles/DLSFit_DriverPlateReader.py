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
Path0 = '/Users/rebeccarapflbl/Desktop/ExperimentalData/PlateReaderDLS/ExtractedPlateReaderData/'

#prename = "200211_OOAandBA"

#read_in = pd.read_csv("./"+prename+"CleanCorr.csv")

SAVE_DATA = 'yes'

os.chdir(Path0)
print os.getcwd()
outputfolder = "Fitted"
isdir = os.path.isdir(outputfolder)
if isdir == False:
    os.mkdir(outputfolder)

ListFiles = pd.read_csv('PlateReaderDLSCorrFilesedit0512.csv')

for idx, row in ListFiles.iterrows():
    p_file = row.FileNames
    print p_file
    prename = row.OutputNames
    print prename
    read_in = pd.read_csv(p_file)
    data = read_in.copy()
    #print data.head()
    data = data.drop(data.index[0])
    data = data.drop(data.columns[0], axis = 1)
    num_meas = len(data.columns)-1

#PlateReaderDLSCorrFilesedit0512
    #print num_meas #how many files are we dealing with
    
    #
    ## =============================================================================
    ## =============================================================================
    #
    modelParamsDict = DFL.initializeExponentialModelParams();
    #
    ## =============================================================================
    ## =============================================================================
    FitArray = pd.DataFrame()
    R2Array = np.zeros(num_meas)
    RadiiArray = np.zeros(num_meas)
    RadVarArray = np.zeros(num_meas)
    RadStdArray = np.zeros(num_meas)
    
    IndexNames = range(num_meas-2)+["AvgNormCorr:","AvgUnNormCorr"]
    
    for entry in range(num_meas):
        print entry
        Decays = data.iloc[:,0]/1000 #units needs to be in ms. Plate Reader Data is in us.
        #print Decays
        
        Corr = data.iloc[:,entry+1]
        #print Corr
        CurrName = data.columns[entry+1]
    
        modelParamsDict["DecayTime"] = Decays
        #print AvgData.iloc[:,i]
        Radius, RadVar = curve_fit(DFL.ExponentialModel, modelParamsDict, Corr, maxfev = 100000)
        #print Radius
        RadiiArray[entry] = Radius
        RadVarArray[entry] = RadVar
        RadStdArray[entry] = np.sqrt(RadVar)
        #print RadStd
    
        FitArray['Fit'+CurrName] = (DFL.ExponentialModel(modelParamsDict,Radius))
    #    
        R0 = np.sum((DFL.ExponentialModel(modelParamsDict,Radius) - Corr)**2)
    #    #print AvgR0
        R1 = np.sum((Corr - np.mean(Corr))**2)
        R2 = 1 - (R0/R1)
        R2Array[entry] = R2
        
        #print R2
    
    ExtractedRadii = pd.DataFrame(index = IndexNames)
    
    ExtractedRadii[prename+'Radii']=RadiiArray
    ExtractedRadii[prename+'RadVar']=RadVarArray
    ExtractedRadii[prename+'RadStd']=RadStdArray
    ExtractedRadii[prename+'R2']=R2Array
    #
    
    if SAVE_DATA == 'yes':
        FitArray.to_csv("./"+outputfolder+"/"+prename+'Fits.csv')
        ExtractedRadii.to_csv("./"+outputfolder+"/"+prename+'Radii.csv')
    else:
        print "DATA WAS NOT SAVED"
    ##if MAKE_GRAPHS == 'yes':
