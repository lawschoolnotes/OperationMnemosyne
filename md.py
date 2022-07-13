# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 13:56:46 2022

@author: labra
"""
#%%
import glob
import os
import re

#%%

path = input('Enter File Path \n')
file_type = input('Enter File Extension \n')
recurs = input('Recursive? Y/N \n')
valid = ['y', 'Y', 'n', 'N']

#%%

if recurs[0] in valid:
    recurs = recurs.capitalize()
    if recurs.startswith("Y") == True:
        globpath = f"{path}\\**\\*.{file_type}"
        files = glob.glob(globpath, recursive=True)
    else:
        globpath = f"{path}\\*.{file_type}"
        files = glob.glob(globpath, recursive=False)
else:
    raise Exception("Please enter Y or N")

#%%

print(globpath)
