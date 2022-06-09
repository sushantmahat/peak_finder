# -*- coding: utf-8 -*-
"""
trying to make a python code that can be integrated into Origin
Should be able to open acoustic files, read data, do any type of 
background substration, FFT filters, and the like.
This is a temporary script file.
"""

import os
import glob
import numpy as np



def main_import(file_name):
    """
    takes in txt dat file
    returns a list of list. 
    Details:
    import function of the code. Will take in a file (not a file name!),
    convert its content into a list, each column wiull be a array/list.
    length of nexted list will be the length of the column. 
    Number of columns will be the length of the primary list. 
    For TDTR1, list 1 will be time column and list 2 will be V_in and so on 
    """
    
    content = [i for i in file_name]
    nrows = len(content)                             #total row count
    
    for i in range(nrows):
        content[i] = content[i].rstrip().split("\t")
#        removed white space after string and split based on tab
    ncols = max(len(element) for element in content)
#   goes through all items in content and sets ncols to the longest item 
    
    data = []
    columns = []
#    place holders for data
    
    for i in range(ncols):
        columns = [element[i] for element in content]
        data.append(columns)
#   goes through all items in content and assigns them a column number   



    return data
        


 
    
    
file_name=glob.glob("acoustic*")
#reads and makes a list of  all file names in the folder starting with the
# keyword "acoustic"


#Non essential portion used solely for debugging below:
# =============================================================================
# print (file_name)
# dtfile= open(file_name[0])
# data = main_import(dtfile)
# 
# print (data[5])
# 
# =============================================================================
# =============================================================================
# for i in range(0,len(file_name)):
#     dtfile = open(file_name[i])
#     data = main_import(dtfile)
#     print (data[1])
#         
# =============================================================================
        
        

