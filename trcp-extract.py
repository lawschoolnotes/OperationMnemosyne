#! usr/bin/env/python3.10
# @author Tecumseh
#%%

import PyPDF2
import requests
import json
#%%

#%%
reader = PyPDF2.PdfReader('texas-rules-of-civil-procedure.pdf')
#%%
page = reader.pages
#%%
textlist = []
for p in page:
    text = p.extract_text()
    textlist.append(text)
# %%
txtstr = ""
for p in page:
    text = p.extract_text()
    txtstr = txtstr + text
# %%
with open('trcpst.md', 'w', encoding='utf-8') as tstr:
    tstr.write(txtstr)
with open('trcplst.md', 'w', encoding='utf-8') as tlst:
    for t in textlist:
        tlst.write(t)
# %%
payload = json.dumps({
    "text": txtstr
})
#%%
response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

restext = response.text
# %%
