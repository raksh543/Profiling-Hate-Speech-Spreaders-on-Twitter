# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 18:38:17 2021

@author: raksh
"""
cd('C:/Users/raksh/Downloads/pan20-author-profiling-test-2020-02-23 (1)')
# Importing the required libraries 
import os
import xml.etree.ElementTree as Xet 
import pandas as pd

def make_csv(folderpath, xmlfilename):
  cols = ["id", "tweet"] 
  rows = [] 
  filename, _ = xmlfilename.rsplit('.', 1)
  # Parsing the XML file 
  xmlparse = Xet.parse(os.path.join(folderpath, xmlfilename))
  root = xmlparse.getroot()
  for i in root: 
    for member in i.getchildren():
      tweet = member.text 

      rows.append({"id": filename,"tweet": tweet}) 
  # for member in root.getchildren():
  #         submembers = member.getchildren()
  #         keys = submembers[0].attrib.keys()
  #         # csvwriter.writerow("\n")
  #         # csvwriter.writerow(keys)
  #         for submember in submembers:
  #             rows.append({"id": filename,"tweet": tweet}) 
  # for i in root: 
  # 	tweet = i.find("document").text 

  # 	rows.append({"tweet": tweet}) 

  df = pd.DataFrame(rows, columns=cols) 

  # Writing dataframe to csv 
  df.to_csv(filename+'.csv') 

path='pan20-author-profiling-test-2020-02-23/es';
for filename in os.listdir(path):
    if filename.endswith('.xml'):
        make_csv(path, filename)