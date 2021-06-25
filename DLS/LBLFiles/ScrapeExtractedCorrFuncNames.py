#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 08:38:52 2020

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

Path0 = '/Users/rebeccarapflbl/Desktop/ExperimentalData/DLS/Alina/CompiledExtractedData/Avg50Filter5/ExtractedTime100Hours_Corr/'
#filename = '20200313_OOAandPA_Histo.csv'
outfile = "Post.csv"


os.chdir(Path0)
print os.getcwd()
#folder_ext = "[0,1,2]*/*0001.ASC"
file_ext = "*Avg50.csv"
files = sorted(glob.glob(file_ext))
files.sort(key=os.path.getmtime)

num_files = len(files)
RadFiles = []
CorrFiles = []
FilePrefix = []
for entry in range(len(files)):
    name = files[entry]
    print name

    FilePreName = name[:-14]
    print FilePreName
    FilePrefix.append(FilePreName)
    
    RadFiles.append(FilePreName+"Rad_Avg50_Fpt5.csv")
    CorrFiles.append(name)


output = pd.DataFrame()
output["LabFilePrefix"] = FilePrefix
output["RadiiFiles"] = RadFiles
output["LabCorrFiles"]= CorrFiles

output.to_csv(outfile)