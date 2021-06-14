#!/usr/bin/env python
# coding: utf-8

# In[2]:



def FigStyle(OutputName): #axis will be shared
    import pandas as pd
    import numpy as np
    import matplotlib as mpl
    import matplotlib.pyplot as plt 
    import os 
    import glob
    from FigStyleFile import FigStyle
    from VariablesAndMathFile import VariablesAndMath
    #import everything
    mpl.rcParams['font.family'] = 'Arial'
    plt.rcParams['font.size'] = 12
    ###########################
    
    plt.rcParams['axes.linewidth'] = 1
    mpl.rcParams['axes.spines.right'] = True
    mpl.rcParams['axes.spines.top'] = True
    plt.axis(xmin=250,xmax=600)
    ###########################
    
    mpl.rcParams['xtick.top']=False
    mpl.rcParams['ytick.right']=False
    plt.tick_params(direction='inout')
    plt.tick_params('both', length=5, width=2, which='major')
    ###########################
   
    plt.xlabel(XLabel, size=15) #x axis label
    plt.ylabel(YLabel, size=17) #y axis label
    ###########################
    
    plt.legend(legendNames, framealpha=1, frameon=False, bbox_to_anchor=(1.02, 1)) #creates legend and specifies location + formatting
    ###########################
    
    plt.savefig(OutputName+".png", dpi=300, transparent=False) 
    plt.show() #shows the final plot
    ###########################

    #sets basic formatting for our plot
    return()
    ###########################


# In[ ]:




