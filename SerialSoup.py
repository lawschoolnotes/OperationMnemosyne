#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@author: Tecumseh

This is a script to parse JSON into presentable formats
"""
#%%
import json
from bs4 import BeautifulSoup
#%%
data = 'TRCPTOC.json'
#%%
with open(data, 'r', encoding='utf-8') as datafile:
            dataJ = json.load(datafile)
#%%

dataS = "\n".join(dataJ)
#%%
textout = ""
for dat in dataJ:
    textout = textout +
#%%
"""
UNCOMMENT WHEN READY TO CONVERT TO A CLASS


class JsonToHTML:
    
    def __init__(self, data):
        self.data = data
        
        with open(self.data, 'r', encoding='utf-8') as datafile:
            dataJ = json.load(datafile)
"""
                