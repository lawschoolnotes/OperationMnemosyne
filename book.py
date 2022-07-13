# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 13:56:46 2022

@author: labra
"""
#%%
import glob
import os
import re
from nbconvert.utils import pandoc
import win32com.client as win32
from win32com.client import constants

#%%

paths = glob.glob("C:\\Users\\Public\\School\\lawschoolnotes\\vault\\2L\\Summer\\TexCivPro\\OTRCT\\**\\*.doc", recursive=True)

#%%

def save_as_docx(path):
    # Opening MS Word
    word = win32.gencache.EnsureDispatch('Word.Application')
    doc = word.Documents.Open(path)
    doc.Activate ()

    # Rename path with .docx
    new_file_abs = os.path.abspath(path)
    new_file_abs = re.sub(r'\.\w+$', '.docx', new_file_abs)

    # Save and Close
    word.ActiveDocument.SaveAs(
        new_file_abs, FileFormat=constants.wdFormatXMLDocument
    )
    doc.Close(False)
#%%

for path in paths:
    save_as_docx(path)

#%%

files = glob.glob("C:\\Users\\Public\\School\\lawschoolnotes\\vault\\2L\\Summer\\TexCivPro\\OTRCT\\**\\*.md", recursive=True)

#%%

for file in files:
    pandoc.pandoc(file, "docx", "gfm", "--wrap=preserve")
    
