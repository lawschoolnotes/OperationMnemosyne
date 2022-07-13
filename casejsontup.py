#! usr/bin/python3
#%%
import json

#%%
with open('casedata.json', 'r', encoding='utf-8') as f:
    cases = json.load(f)

casePairs = []
pairDict = {}
#%%
for case in cases:
    party = case['parties'][0]
    opinion = case['opinions'][0]
    opinion = opinion['text']
    caseTup = (party, opinion)
    casePairs.append(caseTup)
    pairDict[party] = opinion
#%%
""" Kept for possible future uses

with open("partyop.json", "w") as outfile:
    json.dump(pairDict, outfile)

"""
# %%
