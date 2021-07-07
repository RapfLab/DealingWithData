#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 17:13:22 2019

@author: rebeccarapflbl
"""
import numpy as np
import datetime
import matplotlib.pyplot as plt
import os
import pandas as pd


def ReadFile(FILE, file_specifics):
    f = open(FILE)
    count = 0
    
    while count<file_specifics.get("TIME_LINE"): 
        count +=1
        #count
        if count == file_specifics.get("DATE_LINE"):
           date= f.readline()
        elif count == file_specifics.get("TIME_LINE"):
           time= f.readline()
        else:
           f.readline()
    x_corr = np.genfromtxt(f, skip_header =  file_specifics.get("HEADER_LENGTH"), max_rows = file_specifics.get("CORRELATION_LENGTH"))
    scatter_data = np.genfromtxt(f, skip_header = file_specifics.get("SPACE_BETWEEN"), max_rows = file_specifics.get("COUNTS_LENGTH"))

    f.close()
   
    return [date, time, x_corr, scatter_data]

def ReadUTSA(FILE):
    data = pd.read_csv(FILE, encoding= 'unicode_escape', skiprows = 1)
    num_meas = int(len(data.columns)/2)

    if num_meas == 5:
        data = data.drop(data.columns[[2,4,6,8]], axis = 1)#,inplace = True)
        data = data.rename(columns={data.columns[0]: "t_us",data.columns[1]: "C_1",
                                data.columns[2]: "C_2", data.columns[3]: "C_3",
                                data.columns[4]: "C_4",data.columns[5]: "C_5"})
    elif num_meas == 3:
        data = data.drop(data.columns[[2,4]], axis = 1)#,inplace = True)
        data = data.rename(columns={data.columns[0]: "t_us",data.columns[1]: "C_1",
                                data.columns[2]: "C_2", data.columns[3]: "C_3"})
    else: 
        print("Check the number of measurements")
    
    return [data,num_meas]

def ReadALV_KRW(FILE):
    data = pd.read_excel(FILE, header = None)
    data = data.drop(data.columns[[2,3,4]],axis = 1)
    data = data.rename(columns = {data.columns[0]: "t_ms",data.columns[1]: "C_1"})
    num_meas = int(len(data.columns)-1)
    return [data,num_meas]

def SplitTime(date, time):
    date = date.split('\t')
    date = date[1].split('\n')
    date = date[0][1:-2]
#    print date
    time = time.split('\t')
    time = time[1].split('\n')
    time = time[0][1:-2]
    TIME = date + ' ' + time
    
    my_time = datetime.datetime.strptime(TIME, '%m/%d/%Y %I:%M:%S %p')
    return my_time

def ReadAllFiles(FILES, file_specifics):
    num_files = len(FILES)
    print(num_files)
    corr_length = file_specifics.get('CORRELATION_LENGTH')
    AvgScatterPerCorrelation = np.zeros(num_files)
    AllNormCorr = np.zeros((num_files,corr_length))
    AllDecayTime = np.zeros((num_files,corr_length))
    AllTimes = np.zeros(num_files)
    FILES_SIZE = np.zeros(num_files)
    badfilename = []
    badfilesize = []
    baddiffromavg=[]
    for entry in range(num_files):
        FILES_SIZE[entry] = os.path.getsize(FILES[entry])
    AverageFileSize = np.mean(FILES_SIZE)
    print(AverageFileSize)
    count_good = 0
    count_bad = 0
    for i in range(num_files):
#        if os.path.getsize(FILES[i]) < (AverageFileSize-5):
#            print os.path.getsize(FILES[i])
#        elif os.path.getsize(FILES[i]) > (AverageFileSize+5):
#            print os.path.getsize(FILES[i])
        print(i)
        print(os.path.getsize(FILES[i]))
        #if os.path.getsize(FILES[i]) > 18800: 
        if os.path.getsize(FILES[i]) > (AverageFileSize-100) and os.path.getsize(FILES[i]) <(AverageFileSize+7000): #crude way of getting rid of partial files -- should fix
            count_good +=1
            #print i
            date,time,corr,scatter = ReadFile(FILES[i],file_specifics)
    
            CurrentTime = SplitTime(date,time)
    
            if i == 0:
                start = CurrentTime
                AllTimes[i] = (start-start).total_seconds()
            
            else:
                AllTimes[i] = (CurrentTime-start).total_seconds()
    
            NormCorr = corr[:,1]/np.average(corr[:,1][:50])
            DecayTime = corr[:,0]
    
            AvgScatterPerCorrelation[i] = np.average(scatter[:,1])
       
            AllNormCorr[i,:] = NormCorr
            #print i
            AllDecayTime[i,:] = DecayTime
        else:
            count_bad += 1
            AllNormCorr[i,:] = np.NaN
            AllDecayTime[i,:] = np.NaN
            AllTimes[i] = np.NaN
            AvgScatterPerCorrelation[i] = np.NaN
            #print os.path.getsize(FILES[i])
            badfilename.append(FILES[i])
            badfilesize.append(os.path.getsize(FILES[i]))
            baddiffromavg.append(os.path.getsize(FILES[i])-AverageFileSize)
            print("badfilename" +str(FILES[i]))
    print("GOOD "+ str(count_good))
    print("BAD " + str(count_bad))
    print("Total Files " +str(num_files))
    
    badstats = pd.DataFrame()
    badstats['Name'] = badfilename
    badstats['Size'] = badfilesize
    badstats['DiffFromAvgSize']=baddiffromavg
    
    badstats.to_csv("BADFileInfo.csv")
        
    return [AllTimes, AvgScatterPerCorrelation, AllNormCorr, AllDecayTime, badstats]


def DLSPlot(x, y, AxisLabels, GraphType):
    plt.plot(x,y, 'ko')
    #plt.ylim(0,300)
    plt.savefig(GraphType+'.png', dpi = 300)
    plt.xlabel(AxisLabels[0])
    plt.ylabel(AxisLabels[1])
    plt.show()
    plt.close()

def DLSSaveData(x,y, GraphType, FilePrefix,z = None, zz = None):
    if z is not None:
        columns = np.transpose(np.stack((x, y, z, zz)))
    else:
        columns = np.transpose(np.stack((x, y)))
    np.savetxt(FilePrefix+'_'+GraphType+'.txt', columns, delimiter = '\t')
    

def initializeExponentialModelParams(Temp, Laser, Visc):
  # =============================================================================
  # INSTRUMENT PARAMETERS
  # Change these values depending on your experimental setup
  # =============================================================================
    VISCOSITY = Visc #cP
    TEMPERATURE = Temp #K
    #print(TEMPERATURE)
    LASER_WAVELENGTH = Laser #nm 
    DETECTION_ANGLE = np.pi / 2
    REFRACTIVE_INDEX = 1.333

  # =============================================================================
  # Calculate Prefactor Based on Instrument Parameters
  # =============================================================================
    q = ( 4 * np.pi * REFRACTIVE_INDEX / (LASER_WAVELENGTH * 10**-9) ) * np.sin(DETECTION_ANGLE / 2)
    a_D = 1.38e-23 * TEMPERATURE / ( 6 * np.pi * VISCOSITY/1000 )
    PreFactor = 2 * q**2 * a_D
    #print(q)
    #print(a_D)

    paramDict = {"PreFactor": PreFactor};
    return paramDict


# =============================================================================
# define Fit Function
# =============================================================================
def ExponentialModel(paramDict, RadiusParameter): 
    #y = (np.exp(-(PreFactor * x / (1000 * 10**-9*RadiusParameter))))
    y = (np.exp(-(paramDict["PreFactor"] * paramDict["DecayTime"] / (1000 * 10**-9*RadiusParameter))))
    return y 
