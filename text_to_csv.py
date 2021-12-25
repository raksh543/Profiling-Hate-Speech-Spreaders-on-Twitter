# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:18:14 2021

@author: raksh
"""

# importing panda library 
import pandas as pd 

 #readinag given csv file 
 #and creating dataframe 
dataframe1 = pd.read_csv('C:/users/raksh/Downloads/pan20-author-profiling-test-2020-02-23/es/truth.txt')
  
 # storing this dataframe in a csv file 
dataframe1.to_csv('truth_es.csv',  
                   index = None)