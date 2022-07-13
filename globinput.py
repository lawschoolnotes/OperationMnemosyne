# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 13:56:46 2022

@author: labra
"""
#%%
import glob
import os
import re
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

#%%



#%%

path = input('Enter File Path \n')
mask = input('Enter Filename Glob \n')
ext = input('Enter File Extension \n')
recurs = input('Recursive? Y/N \n')
valid = ('Y','N')
recurs = recurs.capitalize()

#%%

if recurs[0] in valid:
    if recurs.startswith("Y") == True:
        globpath = f"{path}\\**\\{mask}.{ext}"
        files = glob.glob(globpath, recursive=True)
    else:
        globpath = f"{path}\\*.{ext}"
        files = glob.glob(globpath, recursive=False)
else:
    raise Exception("Please enter Y or N")

#%%

print(globpath)
