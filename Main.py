# -*- coding: utf-8 -*-
"""
Created on Thu May 23 10:30:43 2019

@author: Mahat

Main program 

Code that subtracts any but the SAW frequency background from the data.

Required modules:
    main_import.py (the reason import gets it own module is becuase I suspect I will
    be using that particular code with other programs and I want it to be easily
    distriutable.)
"""

import main_import
import glob
import numpy as np





def smooth_dt(data,timen):
    """
    the fucntion will take in a data file that is long enough, and a time period
    in terms of n. The it will smooth out the funciton. The length of the output
    file will be smaller by 2n. I could use the clunky way but that would
    just give a bunch of bogus values at the end AND would cost more computing
    time
    """
    return_data = []
    datalen = len(data)
    limlen = datalen - 2 * timen -1 # the 1 is for safety
    
    for i in range(limlen):
        old1 = float(data[i+timen])
        old2 = float(data[i])
        old3 = float(data[i-timen])        
#Clunky way of ensuring iteration stays within bounds.
# =============================================================================
#         if i - timen < 0:
#             old2 = 0 
#         else: 
#             old2 = i - timen
#             
#         if i + timen + 1 > len(data):
#              old3 = 0
#         else:
#              old3 = i + timen
#              
# =============================================================================
             
             
        new = 0.5 * old1 - 0.25 * old2 - 0.25 * old3
        return_data.append(new)
        
    return return_data


def shrtn_dt(data, timen):
    """shortens list to match the length as output by the smooth function.
    """
    return_data = []
    datalen = len(data)
    newlen = datalen - 2 * timen -1
    
    for i in range(newlen):
        old = data[i + timen]
        new = float(old)
        return_data.append(new)
    return return_data
    

def main(data1, data2, timen):
    data3 = np.array((shrtn_dt(data1,timen), smooth_dt(data2,timen)))
    data4 = np.transpose(data3)
#   if i == 2: print(data3)
    return data4
    

    #for j in range(len(data[0])):
        
     #   print (len(data[0]) )
     
     
#Non essential portion used solely for debugging below:
# =============================================================================
#file_name = glob.glob("Acs*")
#print (file_name)
#dtfile= open(file_name[2])
#data = import1(dtfile)
#data1 = shrtn_list(data[5],2)
#data2 = smooth_dt(data[5],2)
#data3 = [data1,data2]
#print(data3)


# 
# =============================================================================
# =============================================================================
# for i in range(0,len(file_name)):
#     dtfile = open(file_name[i])
#     data = main_import(dtfile)
#     print (data[1])
#         
# =============================================================================
        
        

   
     