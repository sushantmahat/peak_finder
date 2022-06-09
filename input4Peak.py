# -*- coding: utf-8 -*-
"""
Created on Fri May 24 15:24:46 2019

@author: Mahat


The input folder that calls upon the main folder.
"""

import Main
import main_import
import glob
import numpy as np
import Acoustic as Acs


#Shortening some calls
import1 = main_import.main_import
main1 = Main.main
peakaboo = Acs.markPeak
#Input variables

#define x and y column position in the data
# default is 1 and 2 (i.e. second and third column as indexing starts at 0!!)

file_name = glob.glob("Smooth*")
timeT = 13 #rough estimate of time period in ps
stepS = 1  #step size used in data taking

time_start = 200 #time after which peak will be detected
timeN = int(timeT/stepS)  #time period in step size

prom = 0.005; #prominence of peaks 

colX = 0
colY = 1
#Below is the main code that loops over all the input file and writes a new 
#smoothed file for each file


for i in range(len(file_name)):
    dtfile = open(file_name[i])
    main_data= import1(dtfile)
    data1 = main_data[colX]
    data2 = main_data[colY]
    dtfile.close()  
    while time_start>float(data1[0]):
        data1 = np.delete(data1,0)
        data2 = np.delete(data2,0)
        
    data3 = peakaboo(data1,data2,timeN, prom)
    
   
    
    data4 = [data3[2],data3[3]]
    new_file = "peaks_" + file_name[i] + "w_t_" + str(timeN*stepS) + 'ps' 
    data5 = np.transpose(data4)
    # transpose : have to change the data from two lists for each column to
    # several lists for each row. This helps  format better dueing savetxt
    
    with open(new_file, "w+") as f:
        np.savetxt(f,data5,delimiter='\t',fmt = ['%f','%f'])
    f.close()
    
  






















