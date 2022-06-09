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

#Shortening some calls
import1 = main_import.main_import
main1 = Main.main

#Input variables

#define x and y column position in the data
# default is 1 and 2 (i.e. second and third column as indexing starts at 0!!)

colx = 1    
coly = 2
file_name = glob.glob("Acoustic0")
timeT = 12 #rough estimate of time period in ps
stepS = 1 #step size used in data taking


timeN = int(timeT/stepS)  #time period in step size

#Below is the main code that loops over all the input file and writes a new 
#smoothed file for each file


for i in range(len(file_name)):
    dtfile = open(file_name[i])
    main_data= import1(dtfile)
    dtfile.close()
    data1 = main_data[colx]
    data2 = main_data[coly]
    data4 = main1(data1,data2,timeN)
    new_file = "smooth_" + file_name[i] + "_w_t_" + str(timeN*stepS) + 'ps_'  
    print(data4)
    with open(new_file, "w+") as f:
        np.savetxt(f,data4,delimiter='\t',fmt = ['%f','%f'])
    f.close()
    
    






















