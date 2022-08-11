
# @author Tecumseh
#%%

import PyPDF2
import requests
import json
#%%

#%%
reader = PyPDF2.PdfReader('W6c.pdf')
#%%
page = reader.pages

# %%
txtstr = ""
for p in page:
    text = p.extract_text()
    txtstr = txtstr + text
# %%
with open('DiscFinal.md', 'a', encoding='utf-8') as tstr:
    tstr.write(txtstr)

