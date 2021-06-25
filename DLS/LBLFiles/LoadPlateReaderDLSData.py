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

Path0 = '/Users/rebeccarapflbl/Desktop/ExperimentalData/DLS/CUDLS/'
#filename = '20200313_OOAandPA_Histo.csv'
outfile = "testfolder.csv"


os.chdir(Path0)
print os.getcwd()
folder_ext = "CroppedHisto/*.xlsx"
folders = sorted(glob.glob(folder_ext))
folders.sort(key=os.path.getmtime)

num_files = len(folders)

output = pd.DataFrame()
output["FolderNames"] = folders
output["OutputNames"]=np.zeros(num_files)

output.to_csv(outfile)