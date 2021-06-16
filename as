warning: LF will be replaced by CRLF in Langmuir/MultPlotLangmuirFixed.ipynb.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in Langmuir/ReadPlotSingleLangmuirRun.ipynb.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in Langmuir/ScrapeLangmuirData.ipynb.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in UVVisV2.ipynb.
The file will have its original line endings in your working directory
[1mdiff --git a/FigStyleImport.py b/FigStyleImport.py[m
[1mdeleted file mode 100644[m
[1mindex ab8ab64..0000000[m
[1m--- a/FigStyleImport.py[m
[1m+++ /dev/null[m
[36m@@ -1,54 +0,0 @@[m
[31m-#!/usr/bin/env python[m
[31m-# coding: utf-8[m
[31m-[m
[31m-# In[2]:[m
[31m-[m
[31m-[m
[31m-[m
[31m-def FigStyle(OutputName): #axis will be shared[m
[31m-    import pandas as pd[m
[31m-    import numpy as np[m
[31m-    import matplotlib as mpl[m
[31m-    import matplotlib.pyplot as plt [m
[31m-    import os [m
[31m-    import glob[m
[31m-    from FigStyleFile import FigStyle[m
[31m-    from VariablesAndMathFile import VariablesAndMath[m
[31m-    #import everything[m
[31m-    mpl.rcParams['font.family'] = 'Arial'[m
[31m-    plt.rcParams['font.size'] = 12[m
[31m-    ###########################[m
[31m-    [m
[31m-    plt.rcParams['axes.linewidth'] = 1[m
[31m-    mpl.rcParams['axes.spines.right'] = True[m
[31m-    mpl.rcParams['axes.spines.top'] = True[m
[31m-    plt.axis(xmin=250,xmax=600)[m
[31m-    ###########################[m
[31m-    [m
[31m-    mpl.rcParams['xtick.top']=False[m
[31m-    mpl.rcParams['ytick.right']=False[m
[31m-    plt.tick_params(direction='inout')[m
[31m-    plt.tick_params('both', length=5, width=2, which='major')[m
[31m-    ###########################[m
[31m-   [m
[31m-    plt.xlabel(XLabel, size=15) #x axis label[m
[31m-    plt.ylabel(YLabel, size=17) #y axis label[m
[31m-    ###########################[m
[31m-    [m
[31m-    plt.legend(legendNames, framealpha=1, frameon=False, bbox_to_anchor=(1.02, 1)) #creates legend and specifies location + formatting[m
[31m-    ###########################[m
[31m-    [m
[31m-    plt.savefig(OutputName+".png", dpi=300, transparent=False) [m
[31m-    plt.show() #shows the final plot[m
[31m-    ###########################[m
[31m-[m
[31m-    #sets basic formatting for our plot[m
[31m-    return()[m
[31m-    ###########################[m
[31m-[m
[31m-[m
[31m-# In[ ]:[m
[31m-[m
[31m-[m
[31m-[m
[31m-[m
[1mdiff --git a/Langmuir/MultPlotLangmuirFixed.ipynb b/Langmuir/MultPlotLangmuirFixed.ipynb[m
[1mindex e856959..dc94d31 100644[m
[1m--- a/Langmuir/MultPlotLangmuirFixed.ipynb[m
[1m+++ b/Langmuir/MultPlotLangmuirFixed.ipynb[m
[36m@@ -3,7 +3,7 @@[m
   {[m
    "cell_type": "code",[m
    "execution_count": 120,[m
[31m-   "id": "f16da609",[m
[32m+[m[32m   "id": "628495f7",[m
    "metadata": {},[m
    "outputs": [],[m
    "source": [[m
[36m@@ -26,7 +26,7 @@[m
   {[m
    "cell_type": "code",[m
    "execution_count": 121,[m
[31m-   "id": "1a9b71ef",[m
[32m+[m[32m   "id": "df0527e2",[m
    "metadata": {},[m
    "outputs": [[m
     {[m
[36m@@ -82,7 +82,7 @@[m
   {[m
    "cell_type": "code",[m
    "execution_count": 126,[m
[31m-   "id": "8bf49cf0",[m
[32m+[m[32m   "id": "3acf563d",[m
    "metadata": {},[m
    "outputs": [[m
     {[m
[36m@@ -196,7 +196,7 @@[m
   {[m
    "cell_type": "code",[m
    "execution_count": 127,[m
[31m-   "id": "de61b491",[m
[32m+[m[32m   "id": "52af1068",[m
    "metadata": {},[m
    "outputs": [],[m
    "source": [[m
[36m@@ -232,7 +232,7 @@[m
   {[m
    "cell_type": "code",[m
    "execution_count": 128,[m
[31m-   "id": "d51ffaa9",[m
[32m+[m[32m   "id": "92ed3a0e",[m
    "metadata": {},[m
    "outputs": [[m
     {[m
[36m@@ -264,7 +264,7 @@[m
   {[m
    "cell_type": "code",[m
    "execution_count": null,[m
[31m-   "id": "0e3ed8dc",[m
[32m+[m[32m   "id": "4ca8ef53",[m
    "metadata": {},[m
    "outputs": [],[m
    "source": [][m
[1mdiff --git a/Langmuir/ReadPlotSingleLangmuirRun.ipynb b/Langmuir/ReadPlotSingleLangmuirRun.ipynb[m
[1mindex 805bb24..e6636f3 100644[m
[1m--- a/Langmuir/ReadPlotSingleLangmuirRun.ipynb[m
[1m+++ b/Langmuir/ReadPlotSingleLangmuirRun.ipynb[m
[36m@@ -3,13 +3,18 @@[m
   {[m
    "cell_type": "code",[m
    "execution_count": 1,[m
[32m+[m[32m   "id": "d072eb03",[m
    "metadata": {},[m
    "outputs": [[m
     {[m
[31m-     "name": "stdout",[m
[31m-     "output_type": "stream",[m
[31m-     "text": [[m
[31m-      "/Users/rebeccarafp/Documents/RapfLabPython/TestData\n"[m
[32m+[m[32m     "ename": "FileNotFoundError",[m
[32m+[m[32m     "evalue": "[WinError 3] The system cannot find the path specified: '/Users/rebeccarafp/Documents/RapfLabPython/TestData/'",[m
[32m+[m[32m     "output_type": "error",[m
[32m+[m[32m     "traceback": [[m
[32m+[m[32m      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",[m
[32m+[m[32m      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",[m
[32m+[m[32m      "\u001b[1;32m<ipython-input-1-54cac3ca2ec1>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     45\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     46\u001b[0m \u001b[1;31m##Set file path to where data is being held locally\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 47\u001b[1;33m \u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mchdir\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mFilePath\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     48\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgetcwd\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",[m
[32m+[m[32m      "\u001b[1;31mFileNotFoundError\u001b[0m: [WinError 3] The system cannot find the path specified: '/Users/rebeccarafp/Documents/RapfLabPython/TestData/'"[m
      ][m
     }[m
    ],[m
[36m@@ -67,6 +72,7 @@[m
   {[m
    "cell_type": "code",[m
    "execution_count": 2,[m
[32m+[m[32m   "id": "30700b7c",[m
    "metadata": {},[m
    "outputs": [],[m
    "source": [[m
[36m@@ -95,6 +101,7 @@[m
   {[m
    "cell_type": "code",[m
    "execution_count": 3,[m
[32m+[m[32m   "id": "d576cd04",[m
    "metadata": {[m
     "scrolled": true[m
    },[m
[36m@@ -116,6 +123,7 @@[m
   {[m
    "cell_type": "code",[m
    "execution_count": 4,[m
[32m+[m[32m   "id": "69d0cbe5",[m
    "metadata": {},[m
    "outputs": [[m
     {[m
[36m@@ -235,6 +243,7 @@[m
   {[m
    "cell_type": "code",[m
    "execution_count": 5,[m
[32m+[m[32m   "id": "015a8255",[m
    "metadata": {},[m
    "outputs": [[m
     {[m
[36m@@ -272,6 +281,7 @@[m
   {[m
    "cell_type": "code",[m
    "execution_count": 6,[m
[32m+[m[32m   "id": "a9966675",[m
    "metadata": {},[m
    "outputs": [[m
     {[m
[36m@@ -303,6 +313,7 @@[m
   {[m
    "cell_type": "code",[m
    "execution_count": null,[m
[32m+[m[32m   "id": "7fc5365d",[m
    "metadata": {},[m
    "outputs": [],[m
    "source": [][m
[36m@@ -324,7 +335,7 @@[m
    "name": "python",[m
    "nbconvert_exporter": "python",[m
    "pygments_lexer": "ipython3",[m
[31m-   "version": "3.8.3"[m
[32m+[m[32m   "version": "3.8.8"[m
   }[m
  },[m
  "nbformat": 4,[m
[1mdiff --git a/Langmuir/ScrapeLangmuirData.ipynb b/Langmuir/ScrapeLangmuirData.ipynb[m
[1mindex 9167285..4305702 100644[m
[1m--- a/Langmuir/ScrapeLangmuirData.ipynb[m
[1m+++ b/Langmuir/ScrapeLangmuirData.ipynb[m
[36m@@ -3,6 +3,7 @@[m
   {[m
    "cell_type": "code",[m
    "execution_count": 1,[m
[32m+[m[32m   "id": "a4167eaf",[m
    "metadata": {},[m
    "outputs": [[m
     {[m
[36m@@ -70,14 +71,19 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": 10,[m
[32m+[m[32m   "execution_count": 1,[m
[32m+[m[32m   "id": "a7c9d779",[m
    "metadata": {},[m
    "outputs": [[m
     {[m
[31m-     "name": "stdout",[m
[31m-     "output_type": "stream",[m
[31m-     "text": [[m
[31m-      "[]\n"[m
[32m+[m[32m     "ename": "NameError",[m
[32m+[m[32m     "evalue": "name 'glob' is not defined",[m
[32m+[m[32m     "output_type": "error",[m
[32m+[m[32m     "traceback": [[m
[32m+[m[32m      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",[m
[32m+[m[32m      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",[m
[32m+[m[32m      "\u001b[1;32m<ipython-input-1-1f726beac115>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mfiles\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0msorted\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mglob\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mglob\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"*\"\u001b[0m\u001b[1;33m+\u001b[0m\u001b[0mFileType\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[0mfiles\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msort\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpath\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mgetmtime\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfiles\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mnum_files\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mlen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mfiles\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",[m
[32m+[m[32m      "\u001b[1;31mNameError\u001b[0m: name 'glob' is not defined"[m
      ][m
     }[m
    ],[m
[36m@@ -129,13 +135,14 @@[m
     "        AllFiles[outname+\"_MMA\"]=MMA\n",[m
     "        \n",[m
     "        IndFile.to_csv(\"../../\"+OutFolder+\"/\"+outname+\"_Processed.csv\")\n",[m
[31m-    " \n",[m
[32m+[m[32m    "\n",[m
     "AllFiles.to_csv(\"../../\"+OutFolder+\"/\"+Surfactant+\"_AllProcessed.csv\")\n"[m
    ][m
   },[m
   {[m
    "cell_type": "code",[m
    "execution_count": null,[m
[32m+[m[32m   "id": "edc4961f",[m
    "metadata": {},[m
    "outputs": [],[m
    "source": [][m
[36m@@ -157,7 +164,7 @@[m
    "name": "python",[m
    "nbconvert_exporter": "python",[m
    "pygments_lexer": "ipython3",[m
[31m-   "version": "3.8.3"[m
[32m+[m[32m   "version": "3.8.8"[m
   }[m
  },[m
  "nbformat": 4,[m
[1mdiff --git a/README.md b/README.md[m
[1mdeleted file mode 100644[m
[1mindex cdf3df6..0000000[m
[1m--- a/README.md[m
[1m+++ /dev/null[m
[36m@@ -1,9 +0,0 @@[m
[31m-# DealingWithData[m
[31m-[m
[31m-This is a repository of how Rapf Lab deals with data and plotting.[m
[31m-[m
[31m-Adam was here[m
[31m-[m
[31m-AG added this from new git 2.32.0 install[m
[31m-[m
[31m-Tim was here[m
\ No newline at end of file[m
[1mdiff --git a/UVVisV2.ipynb b/UVVisV2.ipynb[m
[1mindex a7846b2..cb372ce 100644[m
[1m--- a/UVVisV2.ipynb[m
[1m+++ b/UVVisV2.ipynb[m
[36m@@ -2,7 +2,7 @@[m
  "cells": [[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": 18,[m
[32m+[m[32m   "execution_count": 1,[m
    "id": "adac2204",[m
    "metadata": {},[m
    "outputs": [],[m
[36m@@ -18,7 +18,7 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": 29,[m
[32m+[m[32m   "execution_count": 2,[m
    "id": "5583d65d",[m
    "metadata": {},[m
    "outputs": [],[m
[36m@@ -100,7 +100,7 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": 30,[m
[32m+[m[32m   "execution_count": 3,[m
    "id": "e9255fa8",[m
    "metadata": {},[m
    "outputs": [],[m
[36m@@ -140,7 +140,7 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": 47,[m
[32m+[m[32m   "execution_count": 4,[m
    "id": "a889f973",[m
    "metadata": {},[m
    "outputs": [],[m
[36m@@ -162,13 +162,13 @@[m
   },[m
   {[m
    "cell_type": "code",[m
[31m-   "execution_count": 48,[m
[32m+[m[32m   "execution_count": 5,[m
    "id": "d5bbfd27",[m
    "metadata": {},[m
    "outputs": [[m
     {[m
      "data": {[m
[31m-      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAZcAAAELCAYAAAAVwss1AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAAAyeUlEQVR4nO3dd5xdVbn/8c9zptdMejKppBACMQZIAFGaegPIVUBBEAJIR4pXRb3ci0qxv36AWBFBKUpTWuCCCqEJUqSlgCEFCCkkmfSZSZn6/P5Y+yQnkylnklPmJN/363Vec/Zea+/9nJ3JeWbtvdda5u6IiIikUizbAYiIyO5HyUVERFJOyUVERFJOyUVERFJOyUVERFJOyUVERFIu48nFgjvM7JvtlJ1pZjMTXu+bWZOZDYzKV7cpPz3T8YuISNfyM3kwMxsP/Bo4GJjTttzd7wTujOoWAP8AfuLuK81sHLDW3Sd143jqxCMishPc3XZl+4wmF+AS4FZgcRJ1/xuocfebo+VDgRYzex7oBdwP/NDdWzrbiTqJioh0j9ku5RUgw8nF3S8FMLOpndUzs37A5cCBCavzgRnAFUAB8BhQC9zYzvae8D5+7F2KXUREkpfplkuyLgCmu/t78RXufktiBTO7Afgq7SQXERHJrp76tNgpwG2JK8zsDDObmLgKaGpvY3e3+PVCd1erRUQkw3pccjGz3sAY4MU2RROAa80sz8xKgEuB+zIdn4iIdC3rycXMJpvZzIRVY4Dl7t62VXINsJbwlNlsQvK5NSNBiohIt9jufMnIzHx3/nwiIulgZrv8KHLWWy4iIrL7UXIREZGUU3IREZGUU3IREZGUU3IREckRjz32GBMnTmTcuHGcfPLJ1NbW8uUvf5nrrrsu26HtQMlFRCQHrFq1irPPPpsHHniAefPmMWrUKK644opsh9UhPYosItKBax59m39/WJvWY+xbXclVn92vy3p33XUXd999N4899hgAixYt4qMf/SgnnHACdXV1rFixgpUrVzJhwgTuvvtuysrKKCoq4vjjj2fWrFncddddTJ48OamY9CiyiMgeYsmSJQwbNmzr8tChQ6mtraWuro5ly5YxY8YM5s+fz9KlS3nwwQcBaGxs5LOf/Szz5s1LOrGkSk8duFJEJOuSaVFkSmtra7tD4efl5XHCCSdQWloKwIQJE6ipqdlafthhh2UsxkRquYiI5IDhw4fz4Ycfbl1etmwZvXv3pqysjIKCgq3ro0taW5fLy8szGmeckouISA6YOnUqL7/8MgsWLADgt7/9Lccff3yWo+qYkouISA4YMGAAt912GyeddBLjx49nzpw5XH/99dkOq0N6WkxERLajp8VERKRHUnIREZGUU3IREZGUU3IREZGUU3IREZGUU3IREZGUU3IREZGUU3IREZGUy3hyseAOM/tmB+XXm9liM5sZve6L1ueZ2Y1m9o6ZLTSzizIbuYhI9rk7Z5111nYThP3mN7/hgAMOYPz48UybNo2GhgYgdIZcvXp1VuLMaHIxs/HAU8BJnVQ7FDjV3SdFr1Oi9RcCewMTgCnA18zsoLQGLCLSg8ydO5dPfepT3H///VvXPfjgg/zyl79kxowZvP3222zevJmf/exnWYwyyPSQ+5cAtwKL2ys0syJgf+DbZjYamA983d0XAycCv3P3ZmCdmd0LTAP+1c5+POE9ABoGRkS67a9XwIo56T3GoI/AsT9Jquqvf/1rzjvvPIYPH7513Z133snll19Onz59gDCgZWNj49byq666ipdffpk1a9bwrW99i0suuYTbb7+d3//+92zcuJFevXrxzDPPpPYzkeGWi7tf6u53d1KlGnga+A4wEXgZmG4hQwwDliTUXQoMTVesIiI9za9+9StOO+207dbNnz+fmpoajjnmGCZOnMjVV19NVVXV1vJRo0bx+uuv89BDD3H55ZfT1NQEwNtvv82zzz6blsQCPWyyMHd/H/hMfNnMrgO+C4wkJMLE5ocBLR3sx6LtNXCliOy8JFsU2dTU1MSTTz7J9OnTKS4u5qyzzuLKK6/kxhtvBNiajCZNmkRDQwO1tWHa5okTJ1JZWZm2uHrU02JmNtHMzmi7GmgiXEqrTlhfTWi9iIjssaqrq/n85z9PZWUlhYWFTJs2jZdeemlreXwisba3CNI9iViPSi5AK/ALM9srWv4KMNvdlwLTgXPMLN/MqoBTgYezEqWISA9x0kkn8ec//5nNmzfj7jz88MNMmTIl22Fl/7KYmU0Gbo2eDHvLzC4DHjWzPELL5EtR1ZuA0cAsoBC42d2fy0rQIiI9xMUXX8zatWs58MADaWlp4YADDugRk4hpsjAREdmOJgsTEZEeSclFRERSTslFRERSTslFRERSTslFRERSTslFRERSTslFRERSTslFRERSTslFRERSTslFRERSTslFRERSTslFRERSTslFRERSTslFRERSTslFRERSTslFRERSTslFRERSTslFRERSTslFRERSTslFRERSLuPJxYI7zOybHZRPM7NZZjbTzF40s8kJZauj9fHX6ZmLXEREkpWfyYOZ2Xjg18DBwJx2yscB/w84wN2Xm9lngAeB4VHZWneflMGQRURkJ2Q0uQCXALcCizsobwDOc/fl0fJrwCAzKwQOBVrM7HmgF3A/8EN3b2m7EzPzhPcAuHvbaiIikiYZTS7ufimAmU3toHwRsCiqY8ANwCPu3mhm+cAM4AqgAHgMqAVuTHfcIiLSPZluuSTFzMqA24FhwDEA7n5Lmzo3AF+lneTi7hbVcbVYREQyr8c9LWZmw4EXgRbgKHdfH60/w8wmJlYFmjIfoYiIdKVHJRczqwCeBR5091PdfXNC8QTgWjPLM7MS4FLgviyEKSIiXehWcjGzIjM7zMxONbPeZjZ0VwMws8lmNjNavBQYAZzY5pHjvsA1wFrCU2azCa2bW3f1+CIiknqW7D0JMzsf+DHQB3BgCnAt4eb6CW1aGT2C7rmIiHSfmW29d72zkmq5mNmXgJuB6cAJhPsdEC5LHQZ8d1eCEBGR3UtSLRczmwX8090vNrM8wo30ye7+hpl9G7jA3cekOdZuU8tFRKT7MtZyAcYBD3VQ9gowZFeCEBGR3UuyyWU1MKqDsjHAmtSEIyIiu4Nkk8tDwPfN7PCEdW5mo4D/BR5JeWQiIpKzkr3nUgE8DRwArAd6E4ZpGQIsAA5397Vpi3InmZm3tLQSi+3SpUMRkT1KKu65dOdR5ALgDODTQD9CknkWuK0nPoYMIbms29hAVWlhtkMREckZqUguSY8t5u5NZvZ3d/9DdPC+wIiemljiVtcruYiIZFqy/VyqzOwp4KmE1VOA18xsupmVpiW6FKipa8h2CCIie5xkb+j/mDC21/cS1j0DnAQcBFyd2rBSZ5WSi4hIxiWbXD4LfNPd/xxf4e4N7v4g4WmxL6YjuFRYWbsl2yGIiOxxkk0uVUBNB2XLgIEpiSYNamrVchERybRkk8vbwGkdlJ0MzE1NOKm3UpfFREQyLtmnxW4A7jGz/sCDwEqgP2EQy+PoOPFkXY0ui4mIZFxSycXd74s6Ul5LNO1wZBXwFXfvsZN26WkxEZHM604/l1uBW81sb7Z1onzH3VvTFFtKqOUiIpJ5SSeXOHefD8xPQyxpsbGxhfqGZsqLuv1RRURkJyX1jRt1krwG+BxQxo4PAri799hh92tqt1DevzzbYYiI7DGS/XP+RuBcwlhiS4EefSmsrZq6BkYpuYiIZEyyyeULwHfc/cfpDCZd1JFSRCSzku3nUgS8lIoDWnCHmX2zg/LjzGy2mc0zs7+YWWW0Ps/MbjSzd8xsoZldlOwxNQSMiEhmJZtcngGO2tWDmdl4wuCXJ3VQ3h+4DfiCu48D3gN+EhVfCOxNGONsCvA1Mzuoq2MW5cfUchERybBkL4v9DLjbzEqAF4FNbSu4+xNJ7OcS4FZgcQflU4FX3X1BtHwTMMvMLgFOBH7n7s3AOjO7F5gG/KuzAw6sLFZfFxGRDEs2ucyIfra9lOWART/zutqJu18KYGZTO6gyDFiSsLwUqAQqOiib2N5OzGzrDGjzZ7/K/Deb+fmp+3cVnoiIpEiyyWWXL4klKUZIVG21tFNm0fpOtdSvo7D/iNREJyIiSUl2+Jfn0h1IZDFwcMLyEGCdu280s8VAdUJZNaH1soP49Jxm5pecM40HXm+3moiIpEnS3dbNbC/gcKCQ0GqA0JooA45w98+lIJ4ngOvNbGx03+UiYHpUNh04x8weBcqBU6PyTg2oLKKuoZlNjc2UFqqXvohIJiTbQ/+LwJ+i+vFLU5bw/t87G4CZTQZudfdJ7l5jZmcD95tZIfAucGZU9SZgNDCLkOBuTqZFNbCiGAjzuozsp+QiIpIJyX7bXgG8DlwMXEq4ef9TwnD7PwS+3p2DuvuXE96/BkxKWH4ceLydbZqBr3XnOBBaLhA6Uo7sV9bdzUVEZCckm1z2AU539zfN7Bng6+4+F5hrZtWEqY5ndLqHLBlYGbVc9DiyiEjGJNuJ0oE10fuFwHgzi993eQzYL9WBpcqAim0tFxERyYxkk8sC4IDo/XygmG0JpTR69Ui9SgoozI9pCBgRkQxKNrn8EfiRmX3T3dcCLwO/MbOTgauBOWmKb5eZGQMqinRZTEQkg5K953IDYfbJeI/4S4G/AfcBG4DPpj601BlQUaTLYiIiGZRsJ0oH/idh+Q0zGwWMJ0x1XJem+FJiYGUxC2rqsx2GiMgeo1sdP8ysH/AJoDewEnixpycWCC2XFxauznYYIiJ7jGQ7UeYR+rNcBpQkFG02sx+6+4/SEVyqDKgspm5LM5sbWygp7HJ8TRER2UXJ3tD/DmFE5FuAIwiXw44i9Nq/1swuTk94qTG4V+jrsnzD5ixHIiKyZ0j2stg5wI/d/bsJ6+YBz5lZPfAN4DepDi5VqqtCY+vD9VsY1b88y9GIiOz+km25DAA6Gsfr/wijF/dYQ7YmF7VcREQyIdnk8gLwnx2UfQJ4LTXhpMfAymLMYJmSi4hIRnR4WazNbJEPAzeYWRmhb8sKoA+hf8v5wHlpjHGXFebHGFhRrOQiIpIhnd1z+RvbpjGOOzd6JQ67DyHh9OjHsKqrinVZTEQkQzpLLpma2jgjqqtKeGvZhmyHISKyR+gwuSROxGVmNwB3R3Ov5KQhvUt44t8raW11YjHregMREdlpyd7QP5fQKz9nDakqobG5ldUbNYCliEi6JZtc3gIOTWcg6Vbda1tfFxERSa9kO1H+HbjSzD5DSDQr25S7u1+Z0shSrDqhr8ukYVXZDUZEZDeXbHK5Ovo5JXq15UCPTi5DeqsjpYhIpiQ75H6yl896rMrifMqL8tXXRUQkA7qdNMxsHzM7xMxG78wBzew4M5ttZvPM7C9mVtmm/Ewzm5nwet/MmsxsYFS+uk356Ukel+qqYpatU3IREUm3pJOLmX3RzJYCbwP/BOab2RIz+1I39tEfuA34gruPA94DfpJYx93vdPdJ7j6JcAluBXCpu680s3HA2nh59Lor2eNXV5XwoUZGFhFJu6SSi5kdA9wDfABcAnyeMLfLEuBPZnZ0ksebCrzq7gui5ZuA082so44n/w3UuPvN0fKhQIuZPR+1fr4XzTXTNl43M4/eE9/9kKoSPS0mIpIByd7Q/y7wqLuf0Gb9b8zsYeB/CU+UdWUYISHFLQUqgQqgNrFiNOvl5cCBbeKdAVwBFACPRdvdmMyHqK4qYe3GRk0aJiKSZsleFtsf+F0HZb+LypM9nrezvqWddRcA0939vfgKd7/F3S9z943uvh64ATix7Ybubu5u0XvcwyG3Dr2vS2MiImmVbHJZC5R1UFZB+8mhPYuB6oTlIcA6d9/YTt1TCPdntjKzM8xsYuIqoCnJY299HFk39UVE0qs787l8x8yqEleaWW9C/5Z/JLmfJ4BDzGxstHwRML1tpWi/Y4AX2xRNIEyrnGdmJcClhBGZk1KtScNERDIi2Xsu/wu8DrxnZn8jPME1CDiGMNR+Uk+MuXuNmZ0N3G9mhcC7wJlmNhm4NXpCDEJiWe7ubVsl1wC/AuYQ7rn8Bbg1yc/AwIoi8mPG4rWbkt1ERER2gsXvR3RZ0WwfQk/9IwkTha0FngGucfd30hTfLjEzb/v5jrruWfatruTXpx2QpahERHo2MyN+33pnJdtyIUogp+7KwXqCEX1L+WBNe7d4REQkVbrTibLKzIZF74vM7Eoz+52ZfSp94aXeiD6lfLB6E8m22EREpPuS7UT5MbZ1oAT4JfB94CTg72a2w+PAPdWIvmXUNTSzdmNjtkMREdltJdtyuZYw7MvNZlYGnA781t37AL8H/idN8aXcyH6lACxao5v6IiLpkmxyOQj4vru/TxjCpRj4U1R2H7BfGmJLixF9Q3cd3XcREUmf7oyKHB+U62igHnglWi4HcqYZMLR3CTGDD9RyERFJm2SfFpsNnG9mm4GTgSfcvcXM+gLfBt5IV4CpVpSfR3VViVouIiJplGxy+R7wKGFIls3Aj6L1c4FCQmsmZ4zsW6Z7LiIiaZTUZTF3fwb4CKEn/nh3fzMquhyY6O6vdLhxD6S+LiIi6dWdTpTvA+9H/V32Ala5+x/TF1r6jOhbyrpNTWzY1ESv0oJshyMistvpTifKY8zsVWANsBBYb2YvmtnhaYsuTbY+MbZWrRcRkXRIthPlF4HHCS2dq4GLgR8AVcCTZnZkWqJLk5FRcnl/tZKLiEg6JHtZ7Ergfnf/YuJKM7uWcKP/p8DBKY4tbUb0LSVm8O4qJRcRkXRI9rLYOEJP/O24eythKJiJO2zRgxUX5DGsTynv1tRnOxQRkd1SssllISHBtGcgYYbJnDKmfznvrlJyERFJhw6Ti5kVxl+Ey2LXmNnp0TIWHEe49/LtzISbOmMGlPPe6o20tGp0ZBGRVOus5bKF0GFyM/Ag0Au4E9hkZquBBuARQsvlljTHmXKj+5fT2NzKEs1KKSKScp3d0L8WSPbP+r1TEEtGjR5QDsDCmnpG9ivLcjQiIruXDpOLu1/d2YZmFgM+R5jj5ZOEYfhzxph4cllVz6cZmOVoRER2L0n30I8zs4HA+cAFwBCgEfhLiuNKu14lBfSvKGKhnhgTEUm57vTQP9zM7iXMSHkNoaf+ZcBgdz+1G/s5zsxmm9k8M/uLmVW2U+d6M1tsZjOj133R+jwzu9HM3jGzhWZ2UbLHbc+Y/uVKLiIiadBpcjGzcjO72MzmAM8AnwJuj4r/y91/4+7rkz2YmfUHbgO+4O7jgPeAn7RT9VDgVHefFL1OidZfSLi/MwGYAnzNzA5K9vhtjRtUwfyVdbTqiTERkZTq7FHk3wDLgF8AS4FTgWrgCsB28nhTgVfdfUG0fBNwuplt3Z+ZFQH7A982szlm9oCZDY+KTwRuc/dmd18H3AtMayd2NzOP3pOw++3sO7iSTY0tfKAnxkREUqqzlstFhJbFx9z9WHf/i7s3kfwTZO0ZBixJWF4KVAIVCeuqgaeB7xB6/r8MTI8SUHvbD93ZYMYPDlfk5i6v3dldiIhIOzpLLtcDg4GXzex1M7vEzKpScLz2klNL/I27v+/un3H3t9zdgeuA0cDIdra3xG0T9mHubtF7wm52NHZgOXkxU3IREUmxDpOLu3+L0Cr4IlAD/Bz4EPgD4Qt+Z1owiwktk7ghwDp33zqCpJlNNLMz2mxnQFM721cTWi87pbggj1H9ypi7vG5ndyEiIu3o9IZ+dG/jAXc/ltBy+ClwAOHL/s9m9jMzm9KN4z0BHGJmY6Pli4Dpbeq0Ar+IJiQD+Aow292XRnXPMbP8qBV1KvBwN46/g/GDK9VyERFJsaQfRXb3pe5+DTAKOAZ4gfDF/7KZzUtyHzXA2cD9ZjaXMHXy5WY22cxmRnXeIjzi/GhU50TC9MoQHgB4F5gFvAr83t2fS/YztGefwRUsW7+ZDZubdmU3IiKSwDq6H5HUxmZ9gS8D57j7fqkKKlXMzLv6fM/Mq+Hs217lvgsO4eBRfTMUmYhIz2VmxO9b76ykWy7tcfc17n59T0wsydpXT4yJiKTcLiWX3cGAiiL6lBXqpr6ISArt8cnFzNivupLZyzZkOxQRkd3GHp9cAPYfVsW8FbVsamzOdigiIrsFJRdg/xG9aXWYtUStFxGRVNj9k8uq+dDFE2OThlYB8OaSdRkISERk99ft+Vxyzq+nQHEVVFZDWX8oHwAFpVBYBv3HQV4RvQtLObZ3Davmb4ADykK9vN3/1IiIpMsu9XPp6czM/fU7YdnrUF8DG2vCz6ZN0FAPzZvb37CgDPrsBQPGQ98xMOoo6DcWSvtk9gOIiGRBKvq57P7JpaPP19wI9SuhtQk2r+f5mf/mT/9cwA+OqqJ/80pY+y6sfBtql23bpt/eMOl02O9E6D0iMx9CRCTDlFy6kEwP/bj3V2/kqOue5UcnfoTTDh6+rWDdIlg1LySaBU/A4pfC+iGT4aOnwoFn6xKaiOxWlFy60J3k4u5M+eFTfHxMX35+6v4dVYLlM+HdZ+DtB2HFnNCamXIeHHAWFBSnLngRkSzJ+vAvuxMz4+Nj+vLPhas7nvbYDKr3h8O+ARc+D6f8KTwY8Ndvw68mw6x7oXFj+9uKiOxBlFwSHD62P6vrG5m7Iolxxsxg/GfhgmfhzEegpDc8dCH8/KOw6IW0xyoi0pMpuSQ4bGw/AP4xf3X3Nhx1REgyJ/0BCkrg9uPgwQugdnnqgxQRyQFKLgkGVBazz6AKnl+wqvsbx/Jgwhfg4ldgyvnw1gNwy1HwwYupD1REpIdTcmnj8L3789qidTs/zlhhKRx3HVzwHMTy4bZj4a9XQGtLagMVEenBlFzaOHxsfxpbWnnlvbW7tqNBE+Dil+Dgr8ArN8E9X4I176YmSBGRHk7JpY3JI3tTXBDjmXk1u76zogo49ifwH9eGy2M3HwHvPLbr+xUR6eGUXNooLsjjyL0H8Le3VnT8SHJ3ffy/4JKXoe9ouPc0eOI70NKUmn2LiPRASi7t+MzEwdTUNfD64hSOktxrKJzz99Dh8sVfwr2nQ1MHY5uJiOS4jCcXMzvOzGab2Twz+4uZVbZTZ5qZzTKzmWb2oplNTihbHa2Pv05PdYyf3GcARfkxHn5zWdeVu6OgGI67PrwW/B1u+jjUzE3tMUREeoCMJhcz6w/cBnzB3ccB7wE/aVNnHPD/gGPcfRLwA+DBhLK17j4p4XVXquMsL8rnuI8MZvrMD9MzO+WU8+CMh0Nv/j8cDYtfTv0xRESyKNMtl6nAq+6+IFq+CTjdzBLHsGkAznP3eA/E14BBZlYIHAq0mNnzUevne2aWl45Av3TwcOobmvm/2WnqCDn6KDjnr1DaD/74eZh1X3qOIyKSBZlOLsOAJQnLS4FKoCK+wt0XuftjAFHSuQF4xN0bCZObzQCOAQ4HjgYua3sQM3Mz8+g92+eu5Ewe0ZsxA8q551+Lu71t0vqMgi8/BtWT4KELYPql0LgpfccTEcmQTCeXGNDeI1g79DA0szLgz8AY4DwAd7/F3S9z943uvp6QeE5MR6BmxukHD+fNxet5M5U39tuqHBzGJjv8W/Dmn+DWT4WpmUVEclimk8tioDpheQiwzt23G0rYzIYDLxKSzlFRIsHMzjCziYlVgR2e6XV3iw8X7e7s7LQCJ08eRmVxPrc8/95ObZ+0vHz45Hdg2gNhpszfHQkLnkzvMUVE0ijTyeUJ4BAzGxstXwRMT6xgZhXAs8CD7n6quyc+rzsBuNbM8sysBLgUSNvNivKifM742Aj++tYK5q2oS9dhthnzKbjohdAf5u5T4O9XQksaHigQEUmzjCYXd68BzgbuN7O5wEeAy81sspnNjKpdCowATmzzyHFf4BpgLTAHmE1o3dyazpjPP2wU5YX53PDkvHQeZpvKwXD247Dv5+ClX8Gfz4DNabwsJyKSBpqJMgk/n7GAn82YzwNfOZQDR/ROQWRJevm38MSVUFENJ98OQw/M3LFFZI+lmSgz5NzD9mJwr2K+ff8stjRlcHTjQy4Kvfrx0B/m5ZvCVMsiIj2ckksSyovy+ekXJvLuqo1c/0SGLo/FDZ0MF/4Dxv4H/O0KuG+aLpOJSI+n5JKkw/fuz7RDhnPrC+/zr/d3cTj+7irtA6feDVN/CPP/BjcfDgtnqBUjIj2W7rl0w8aGZo79+fMAPHLpx6kqLUzZvpO25FW4/2zYsASO+G844gqI6W8EEUmdVNxzUXLpplcXreX0W15hVP8y7r3gkOwkmMZN8Ng3YNY90G9v+NK94fFlEZEUUHLpQjqSC8DzC1Zx7h2vsc+gCv547sH0KilI+TG61NoKbz0Aj10OzVvgyCvgY5dCfhaSnYjsVpRcupCu5ALw1NyVXPSn19l3cCW3nDWZARXFaTlOl9Z9AI9/KwzhP2Bf+M+fwfBDshOLiOwWlFy6kM7kAjDj3yu59J43qCwu4A9fnsKEIb3SdqxOtbbC2w/CjKthw1L4+FfD/ZjCsuzEIyI5TcmlC+lOLgBzl9dy3h2vsXzDZs782EjO/cReDOtTmtZjdmjzOnjkqzD3ERiwHxz7Exh5GOzEqNAisudSculCJpILwJK1m/j5Uwt44I2lFOTFOOnAoZz3ib0Y1b88Lcdzd9ZvamJF7RaWrN3Ev5fXMn9lHfmxGFsamxm9/p9ctP56enktLxYcwq+Kzmf+ll40NLUyvG8phfkxepcWMqCiiFZ3BlUWU7ulmaP3G0RBnjGyXxn9yovSEruI9HxKLl3IVHKJW1hTxy+eWsjf3l5BY3Mrnx4/kM9NquYTY/rRp6x7N9pbWp11mxqZt6KOeSvqWLRmIx+s2cTq+gZW1zewsrZhh20GVRbTq6SAXiUFDChq5Oj66Uxd+ydi3sprpZ/g7wPO5ZUNVbg7C2vqqSjOZ2NjC43NrdvtpyDPGNm3jFH9y6ipa+Dwsf352Oi+HDKq7y6dHxHJDUouXch0col7b1U9D725jDteXETtlmbyYsaw3iWM6FtGdVUJI/qWMqiyGDNoaG6loamFzU0trNvUxDvLa/lg7SbW1DeyYfO22QQqivIZ0a+UARXFFBfEOGB4bwb3KmFwVTHjBlZQXJBHXqyd34X1S+CfP4dZ90JLIxx0Phx6GV4+MP4LxMKaevLzYsxbUUthfoxn563igzWbmLu8lpq6bUlsYGURBwzvzcShVVRXFTNuUAX7DKrMxCkVkQxSculCtpJLXHNLK299WMtTc1fyzoo63llRy8aGFtZubGy3fsxgSO8SxvQvZ3BVCYMqixk/uJL9h1fRt6xwp2bU3Kp2Ocy4CubcD4XlcOCZcNCFUDWs081qarewqbGFGXNXMmfZBt5YvI4la7fNgnDshEFMGdmH8YMrOXivPsTaS3AiklOUXLqQ7eTSkbotTaysbcAM1m9qZFCvEnqVFFBWmLdrCSQZq+bDMz+EuY+G5b0Og0MugdGfDJOWJWH9pkb+9f5aXvtgHfe9umRrC2tUvzKm7jeIYycMYuLQXun/LCKSFkouXeipyaVHWL8E3rgDXr8DNtZAfjEcfCGMnQpDDoSCkqR24+6s3djICwtX84d/LmLWkvUAjO5fxlHjBvClg4czOk0PNohIeii5dEHJJQnNjWEwzFdvgff/EdYVlIUWTf99YP9p0GcUxPKS2l1N7RYen7Ocx99awWuL1tLqcNBefThl8jA+PqYfg3plqbOpiCRNyaULSi7dtGktLHkF3rgT5j2+bX1J73DZbO9jw4RlheVQPqDL3a2s3cKDbyzj9hffZ2VtAyUFeXx634F85YjR7FutBwFEeiolly4oueyCjauh5t+w9n1492mY91doiZ4csxiU9IFeQ2DUUeEy2sD9QgunnfssTS2tLFhZz2+fe5dn3qmhrqGZob1LOGXyMD43qZoRfTWSgEhPouTSBSWXFNqyAZa9AR++AfWr4L1noKEeapduq5NXGJJOZTUMngil/WDgvjDwI1DWD4oq2dDg3PHSIp5+p4aZS9aTFzMOG9uPo/cbxNR9B9JXnTdFsk7JpQtKLhlQXwPrF8OHb8La96BmLmxaA+sWQUPt9nVjBVBUDs0NMHA/6qvGMXtNjFdWF7F0Yx7rrBdjRwxlYPUwjj9sMn0qy/XEmUgWKLl0Qckly2qXQ92HUPNOSDgblkLz5nCprb4mLLc0QGtzh7uoKRiK9RpC7969yS/tHQbjLChN+FkKVSOhpAqKKqC4FxRVhqfdlJhEdkpOJhczOw74MVAEzAbOdffaZOqYWR5wPXAMkA9c5+6/7eRYSi49nTusWQgtTdBQS8vG1SxbtoRlb71Ar6YaNmxsIL91MxW2hT55WyizBop8C/mtOw5/s51YfrhEV1Qenn4rKAnv8wrDAwlF5ZBfEh5MyC8K6/MKorJKKK6EPqPDY9plA6CgOCTE8gGwpRYqBmsGUNlt5VxyMbP+wNvAx919gZn9FKhw94uTqWNmFwP/CXwOqABeAs509391cDwllxzX2uq8sXgdj89ZwZxl63lneR11Dc3EaKWEBsptCx/rtY5RVTEGFTXSN38LlbaZcq+nl9dR2LqZgpZNFNJErLEeb2kk1lBLXmMt1tpErGnjTsXl+dEj1SW9wVux0r44YHkF0NIc7jFZLFwCLK4M/YgKSsJyaR9Y8VZIVH3HhHo7vAyIfndj+R288kJytlh4H982lgeWF+rkFYRXcyO0NoX1FguJMXFflpgobbsfYb95YT+xAvDWENt2sdqOnwGH1pZQPx4LhGVvDdvE444fMLG1ufW9JSx39L5tvfaWk6nTzjZ7YAs4F5PL6cBp7n5ctDwSmAVUxbNAZ3WAJ4DfuftforKrgT7u/tU2x9nhQynJ7B7inTaXrtvM7KXrWVnbwMKaehbU1LGytoGNjc0k/0/tFNFEIc0U0EwRTZTaFirZRJXV85G8xdS0VtDf6mhyo5YyhuatpaalgqG2ijK2kE8LZtArtgVvbSGfFjCjyurJN9jkhVRRRzFNFNJEAwUMYC1l1kCLGy3EiOHhteOvrfRArVEC8q0/E237Pna2/27u7F/Xse1eXX2r+3bvOz5mx4zW6Fjb1oSjA1Res3yXk0ty432kzjBgScLyUqCS0AqpTaJOe2UT0xWs9DxmRt/yIvqWF/HRYVU7lG9pamFTYwt1W5pYXd/A5sZWGppbWFPfSCxmFOQZRfkxGlucxubW6NVCi0OeQXOrbx1MtKG5FdvSzGpgQEURfVqdFVuaGN6nNNSJjrmxoZktTa1UFOfj7rS409zi1DU0U1oQOp860OpOzIw8c2IWIxaz7f8odid8PbTS2tJC/ZYWSovyaWpqojDWSoG1YC3NxLyZmLdgRH/9e/Q14S3EaMW8Nbz3FmLeTJ4302yFtFoe0Lp125iH97HWZuJfV7b1ayu+TNgfrcRaG4l5C07UWnHf9hUVtWbi781bcYtFa2LEaCHmTbDdF2jidvHPH4+h7Ve2s+2vhm1fgttv0/ZctlnvO+7TE75e2+4z8TzQYR1PKIuvcWyHY+3It5b5dv/25tDp13rCrrf/3Dueg/aSTfz8WvRHzbat48nGgNs6CSA5mU4uUVt5By1J1mlbZm22BdiacXVZbM9TXJBHcUEefcoK1X9GZGd9fdeTS6bvSC4GqhOWhwDr3H1jknXallUTWi8iItKDZDq5PAEcYmZjo+WLgOndqDMdOMfM8s2sCjgVeDitEYuISLdl9LKYu9eY2dnA/WZWCLwLnGlmk4Fb3X1SR3WiXdwEjCbc4C8Ebnb35zL5GUREpGvqRCkiIttJxaPI6gUmIiIpp+QiIiIpt9sml/Y6UuYSM8vpQRsVf3Yp/uzJ5diBlMW+2yYXERHJnt32hn6ut1xERLIp14Z/ybhdPUHZEk+Oij87FH925XL8uRw7pO4Pc10WExGRlNttL4uJiEj2qOUiIiIpp+QiIiIpl9PJxcymmdksM5tpZi9GY5RhZqujdfHX6dH6sWb2DzP7t5n9y8z2yXL8l5rZ22b2lplNN7MBZpZnZjea2TtmttDMLkqo3+Pjj9bnxPmPYjrBzOqi9zlz7uMS44+Wc+Lcm9n1ZrY4Ic77cun8txd/tD5Xzv9HzOxZM3vTzF4zswNTfv7dPSdfwDhgOTA4Wv4MYUj+ccD8Drb5F2GWS4BjgbeI7jtlIf4DgUVAr2j5OuBm4GLgccKTfL2Bd4CDcij+nDj/UQxjgYVAfbScE+e+k/hz6dy/BBzaZl3OnP8O4s+J8w+URt+dn4mWj4/OdUrPf1b+YVJ0gkYCxyUsDwAagQuBucDzwGzge0AeYV6YWiCWsM0i4IAsfoaC6GcxcA/wI+BJ4OSEOlcDv8ih+M/OhfMf/Qd7BfhcwpdzLp379uLPlXNfBGwhTJcxB3gAGJ4r57+T+HPl/J8AvJCwbIQZfVN6/nP2spi7L3L3xwAsjFdwA/AI0ArMAI4BDgeOBi4jTJH8obu3JuxmKTA0k3EncvcmMzshiuNwwtyi7U3lPJTciT+f3Dj/N0ev2Qnrcubc0378uXLuq4Gnge8QvtReJszVNJzcOP8dxZ8r539vYIWZ/d7MXiMklXxS/Puf850ozawMuJ1wAo5x9/Vtym8Avkpo1rV97rrdaZIzyd0fBh42s/OBvwPbJjQP4jG2N/1zT4x/TOIvYU88/2Z2MdDs7n8ws5EJRR1No92jzn1H8bv7LW3q9bhzD+Du7xMuY4dAzK4DvguUkAPnv5P4ZyT+G/TU8w8UEOI/yt1fMbPjCZfDNpPC85+zLRcAMxsOvEj4kEe5+3ozO8PMJiZWA5oI92MGR62cuKxNk2xmY8zsEwmr/gCMAJbR/lTOuRJ/Lpz/LwNTzGwm4T9VSfR+KTlw7ukgfjM7KwfOPWY20czOaLsaeI4cOP+dxP+JXDj/wIfAXHd/BcDdpxMu371HKs9/Nq75pei6YUV0Mq5qs/6nhGuheYS/hJ4Fzo/KXgNOjd4fTZjlMpapmNvEeVj0j9MvWj6TMMPmZcCjhFZlFeEa7hE5FH9OnP+EzzGSbfcscuLcdxJ/Tpx7YAKwDtgrWr4Y+GeunP9O4s+V8z8IWAscGC0fDtSk+vxn9T/GLp6g/yG0WGa2eQ0h/BX9b2AB4SZzfCSCsdE/+FvRycraDdkonq9Escwk/AW6V/QPeyPwdhT/NxPq50L8pbly/qOYRrLtyzlnzn0H8efMuQemRbHMJVzzH55L57+D+HPp/B9OeCDkLeB14BOpPv8a/kVERFIup++5iIhIz6TkIiIiKafkIiIiKafkIiIiKafkIiIiKafkIj2SmT1kZs+2s36JmbmZDWmz/mdmNi8DcR0ZHT9jQ3eYWR8zOydh+XYzm7GT+3nHzPqmNsKt+y82szltRj2QPZSSi/RUTwMHmVlBfIWZjQcGAyuAqW3qH0YY12l39FNCJ9VddSPwe3dfk4J97cDdtwA/AW7pqq7s/pRcpKd6mtDLeVLCuqnAG8DfCL2EATCz8qjek5kLL6Os6ypd7CAk5i8AN+16OJ26B9jPzD6Z5uNID6fkIj2Su78NrAQOTVg9lZBAZgD/YWbx3994nWcAzOwiCxOYbTGzOjN7wszGRGXPmdnticcysy+a2SYzq4yWzzezeWa2ObrMc1ZHcZpZkYWJo5abWW20/0MSyq82s7+Z2XejOuvM7BEzq06os3cU40YzWxSNj9ccXYK7GjgXOCK6HDcy2qzQwsROa6Lj3hkN4tqRrwF/dff66Jgjo/19wczeiD7/TAujXMfjetbMrjGzO6LYPozOzWEWJunbZGYvmNnohH+3VsIQ9N/oJBbZE2RzCAK99OrsRfgr+L7ofSFQDxxJmLunlW0TGX0feDl6fxJhdNdTCANpHgHMAx6Oys8BNgDFCcd5GLgrev8VwjhLJwGjCcN8rAfOisqPJIwQOzRavg94lXBZbm/gquj4e0flVwMNwP3AfoQEuQa4NSovIwwM+ChhzKr/AN6PjnEkUA7cRRigdRBh3Krbo/JfE4blOC465vc6OZcfAuckLI+M9vEeYYj4CYQpKzYAZVGdZwnzllwOjCK0ehoJw/wfAUyOYr2vzbGOibYryfbvkF7Ze2U9AL306ugFnAcsid4fFSWXwmh5JvDd6P2zwPej90cAX2qzn2uAd6P3FcBG4PPRcu/oy//oaHkpcEmb7a8E5kXvtyYXYEz0fr829Z8Ebo7eX00YGbciofxG4O3o/dmEiZh6JZT/Zzy5RMu3As8mlN9OmHfDEtZNBx7p4DwOj/Z3cMK6eHL5SsK6SdG6KQnn9Z8J5ftF5WcnrPtp/LMkrBsa1Tu0vXj02jNeuiwmPdnTwNBoaoWphC/YxqjsSeBIMysEDiK6me/uzwFzzOwqM7vHzN4A/pfwFz/uXgc8BHwp2s/JwGpghpn1Jwx8ep2Z1cdfhLk6RkfHSrR/9POVNvWPBMYn1FsRHTduPaElBnAAYfjzDQnlLyRxbha6e+LAgOsI96jaMzD6ubqdsvlt4iIhNgjTKMdtjH6+m7BuM2FmxkSr2hxX9kA5P1mY7L7c/T0zWwQcAnwa+FNC8ZPAJVFZK2FOc8xsGmFk2j8C/wB+SZjzO3H+jTuAR8ysAjiNcEmsxcziiesywl/tbTW3WY7X/xjhSzZRQwfv4+I36ZvZuXuf7U3U1NGN/3gSau84ncUGodXVVms76xLlRT+zOpGdZJdaLtLTPUO4JLY/8ETC+ucJv79nA/9IaNH8F/Bbdz/X3W9y9xcJl68SvzCfIvwVfw7hXsmdAFHrYRkw0t0Xxl+ExPZN336aVwhDkwMMbFP/68DxSX6+2cA+ZtYrYd3Bbers6tDly6Of/XdxP8mKH2d5p7Vkt6bkIj3d04Sb6svdfW58pbtvJlw+Opnt+7esIswI+FEzG2tmVxFu7hclbNtKaAV9H5jp7m8lbP8D4BtmdoGZjTaz04AbCH1rthMlkvuA35nZsVH9HwIXEeb5SMY9hMtRd5jZBDM7CvhV/BDRzzpgiJntZWbdvtrg7ssISXP/ruqmyAHAJsLcH7KHUnKRnu5pwhNT7fVheZLwtFVicrmM8GX9ImF2wCnAhcCA6N5N3B2Em/t3Ju7Q3X9LmIjuW4RJn35ASELXdBDfeYSJ0m4jfJkeS3hY4KlkPpyHjofHEh4seI1wSe93UXG8NXYb4VLTXHY+QTxKaAFmwpHAE9EfALKH0mRhIllkZiOAMYnJKOon8xIw3N2XpOg4+xEemR7q7mtTsc8OjlNAaCWd4u7PpOs40vOp5SKSXaXAE2Z2cdSx8SDCZbh/pCqxwNZOqQ8RLtml02mER5OVWPZwarmIZJmZnUJ4XHpvQl+e/wO+5e7tPTq8K8fpT7hUeGiq9x3tv5gwPM9n3f3drurL7k3JRUREUk6XxUREJOWUXEREJOWUXEREJOWUXEREJOWUXEREJOWUXEREJOX+P6vHYd8YQblGAAAAAElFTkSuQmCC\n",[m
[32m+[m[32m      "image/png": "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\n",[m
       "text/plain": [[m
        "<Figure size 432x288 with 1 Axes>"[m
       ][m
