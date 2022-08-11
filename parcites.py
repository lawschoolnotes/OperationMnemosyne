#! usr/bin/env/python3
"""
_summary_: Script to split parallel cites and prioritize more modern syntax
@author: tecumseh
"""
#%%
import json
#%% Load the Json
with open('caseList.json', 'r', encoding='utf-8') as f:
    caseList = json.load(f)
#%% "Make" the form list
cite_form_list = ["vol","reporter", "page"]    
# %% Do the for loop
for case in caseList:
    case['cite'] = case['cite'].split(', ')

#%% Save your work
with open('cl2.json', 'w+', encoding='utf-8') as g:
    json.dump(caseList, g)
# %% Break it down now
for case in caseList:
    case['cite'] = [c.split(' ') for c in case['cite']]
    {cite_form_list: case['cite'] for cite_form_list, case['cite'] in zip(cite_form_list, case['cite'])}

#%%
for cite in cites:
    cite = cite.split(' ')
    case['cite'] = cite
    #citeDict = {cite_form_list: splut for cite_form_list, splut in zip(cite_form_list, splut)}

# %% Give up and use regex
import re

regex = r"(\"\d{1,4}) (?:(U\.S\.|S\.Ct\.|L\.Ed\.2d)) (\d{1,4}\")"
subst = "{\"vol\": \\g<1>\", \"reporter\": \"\\g<2>\", \"page\": \"\\g<3>}"