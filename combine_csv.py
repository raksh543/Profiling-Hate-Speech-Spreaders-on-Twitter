# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 19:15:16 2021

@author: raksh
"""

import os
import glob
import pandas as pd
os.chdir("en_csv")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

#combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
#export to csv
combined_csv.to_csv( "en.csv", index=False, encoding='utf-8-sig')