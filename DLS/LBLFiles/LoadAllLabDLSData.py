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

Path0 = '/Users/rebeccarapflbl/Desktop/ExperimentalData/DLS/MIJ_DLS/'
#filename = '20200313_OOAandPA_Histo.csv'
outfile = "MissedFolders.csv"


os.chdir(Path0)
print os.getcwd()
#folder_ext = "[0,1,2]*/*0001.ASC"
folder_ext = "[0,1,2]*/*0001.ASC"
files = sorted(glob.glob(folder_ext))
files.sort(key=os.path.getmtime)

files2ext = "[0,1,2]*/*/*0001.ASC"
files2 = sorted(glob.glob(files2ext))
files = files + files2
files.sort(key=os.path.getmtime)

num_files = len(files)
outputnames = []
folders = []
FilePrefix = []
for entry in range(len(files)):
    name = files[entry]
    #print name
    #snum = name.count("/")
    #print snum
    s = name.split("/")
    slen = len(s)
        #s = name.find("/")
    print s
    #print name
    if slen == 2:
        folders.append(s[0]+'/')
    elif slen == 3:
        folders.append(s[0]+"/"+s[1]+"/")
    else:
        folders.append("Fix me by hand")
        print "ISSUE WITH FOLDER NAMING APPEND"
    print folders[entry]
    FilePreName = s[-1]
    FilePreName = FilePreName[:-8]
    FilePrefix.append(FilePreName)
    #folders[entry] = name[:-8]
    CleanName = s[0]+"_"+s[-1]
    CleanName = CleanName[:-8]
    outputnames.append(CleanName)
    #outputnames[entry] = 
    print outputnames[entry]
    #print folders[entry]

output = pd.DataFrame()
output["FolderNames"] = folders
output["FilePrefix"] = FilePrefix
output["OutputNames"]= outputnames

output.to_csv(outfile)