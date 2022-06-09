# -*- coding: utf-8 -*-
"""
imports a data file. returns the contents of a file in a list of list format
each nested list in the primary list will be a column in the data file.
"""

import os
import numpy as np



def main_import(txt_file):
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
    
    content = [i for i in txt_file]
    #doing this will make each individual line into a string
    #all the words in that sentence  will become string items in that list
    #So, the total number of lists = total number of lines = length of data file
    #That allows the next command to work
    
    nrows = len(content)                             #total row count
    
    for i in range(nrows):
        content[i] = content[i].rstrip().split("\t")
#        removed white space after string and split based on tab
#          
    ncols = max(len(sentence) for sentence in content)
#   content is a list of lists
#   each list in content is equal to a sentence in the text file
#   ncols looks for the longest sentence in content
#   the number of words in the longest sentence is the max possible column 

    
    data = []
    columns = []
#    place holders for data
    
    for i in range(ncols):
        columns = [element[i] for element in content]
        data.append(columns)
#   goes through all items in content and assigns them a column number   
#   more info: this for loop basically goes thorugh each sentence (list) and assigns the 
#   words in the sentence into a list based on its position in the sentence
#   So the first word in every sentence becomes comlumn 1, 2nd word becomes column2 and so on      


    return data
        


 
    
    

#reads and makes a list of  all file names in the folder starting with the
# keyword "acoustic"


#Non essential portion used solely for debugging below:
# =============================================================================
# import glob
# file_name = glob.glob("Acs*")
# print (file_name)
# dtfile= open(file_name[0])
# content = main_import(dtfile)
# 
# print (content)
# 
# =============================================================================
# =============================================================================
# for i in range(0,len(file_name)):
#     dtfile = open(file_name[i])
#     data = main_import(dtfile)
#     print (data[1])
#         
# =============================================================================
        
        

