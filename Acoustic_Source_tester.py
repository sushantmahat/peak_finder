# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:25:14 2019

@author: smahat2
"""

import scipy.signal
import Main
import main_import
import glob
import numpy as np



find_peaks = scipy.signal.find_peaks
peak_prom = scipy.signal.peak_prominences

prom = 0.005
stepN = 13
xRange = 200
xRangeF = 1000
fineNum = 0

def markPeak(data1, data2, stepN):
    """ data1 is the position (X axis) and data2 is the actual value used to determine
    the peaks. The stepN is the expected datapoitns between peaks, so basically the
    time period in terms of index.
    
    For acoustic data, data1 will be the time delay (ps) and data 2 will be delR
    
    The function returns arrays that contain the peak position in ps, 
    and how prominent each peak is    
    
    """   
    dataNew1 = []
    dataNew2 = []
    dataValley = []
    for i in range(len(data2)):
        new1 = float(data1[i])
        new2 = float(data2[i])
        new3 = float(data2[i]) * -1
        dataNew1.append(new1)
        dataNew2.append(new2)
        dataValley.append(new3)
    
    peaks, _ = find_peaks(dataNew2, distance = stepN, prominence = prom)
    valleys, _ = find_peaks(dataValley, distance = stepN, prominence = prom)

    # for some reason the output of find peaks are two lists.
    # One list is the position of the peaks, the other is the an empty list.
    # so if I set x,y = ... then you will get x to be the first list and y to be
    # an empty list. Assigning _ instead of y just tells python not to store the value
    rtnDataX = []
    rtnDataY = []
    
    peakValTT = []
    valleyValTT = []
    
    
    if len(peaks) > len(valleys): kk = len(valleys) 
    else:
        kk = len(peaks)
    #to make sure everything is within limits of indexing
    
    
    for i in range(kk):
        peakPos = dataNew1[peaks[i]]
        valPos  = dataNew1[valleys[i]]
        peakVal = dataNew2[peaks[i]] - dataNew2[valleys[i]]
        
        
        valleyValT = dataNew2[valleys[i]]
        peakValT = dataNew2[peaks[i]]
        
        rtnDataX.append(peakPos)
        rtnDataY.append(peakVal)
        #T represents temporary commands used for testing, should be removed once 
        #code is complete
        
        peakValTT.append(peakValT)
        valleyValTT.append(valleyValT)
        
        
    return dataNew1, dataNew2, rtnDataX, rtnDataY , peakValTT, valleyValTT       
    #return rtnDataX, rtnDataY
    
    


#Non essential portion used solely for debugging below:
# =============================================================================
import matplotlib.pyplot as plt


import1 = main_import.main_import
main1 = Main.main


file_name = glob.glob("smooth*")


#print (file_name)
dtfile= open(file_name[fineNum])

time_start = 100 #time after which peak will be detected

#Below is the main code that loops over all the input file and enforces time 
#range while writing a new smoothed file for each file

main_data= import1(dtfile)

data1 = main_data[0]
data2 = main_data[1]
dtfile.close()  

while time_start>float(data1[0]):
    data1 = np.delete(data1,0)
    data2 = np.delete(data2,0)

    
#print(data1)
data3 = markPeak(data1,data2, stepN)
data4 = data3[2]
plt.figure(figsize=(7,4))
plt.plot(data3[0],data3[1])
plt.plot(data3[2], data3[3],"x")
plt.vlines(data3[2], ymin=data3[5],ymax=data3[4])
plt.axis([xRange,xRangeF,-5.5,1])
plt.show()
 
# =============================================================================
# =============================================================================
# for i in range(0,len(file_name)):
#     dtfile = open(file_name[i])
#     data = main_import(dtfile)
#     print (data[1])
#         
# =============================================================================
        
        
