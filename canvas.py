#!/usr/bin/env python 3

#%%
import requests
import json
import webbrowser
#%%

token = '2860~zpeSkeHX3zZ2uCMpAzPaQbXGSAWc3XTGB5hIfCx8wcinf6GfIlNFRdjlWzYgcmTK'
headers = {'Authorization': f'Bearer {token}'}
course_id = '14645'
base = f"https://untdallaslaw.instructure.com/api/v1/courses/{course_id}/files/"

#%%
response = requests.get(base, headers=headers)
# %%

data = response.json()

# %%
texts = response.text
# %%

ids = [d['id'] for d in data]

# %%
urllist= []
for id in ids:
    id = str(id)
    file = requests.get(base + id, headers=headers)
    dlurl = file.json()
    geturl = dlurl['url']
    urllist.append(geturl)
# %%
for url in urllist:
    webbrowser.open(url)
# %%
