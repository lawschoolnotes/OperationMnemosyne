#! /usr/bin/python3
import requests
import json

jurlist = requests.get(url="https://api.case.law/v1/jurisdictions/")
jurs = jurlist.json()
jurs = jurs["results"]
jur = []
jurtup = []
for j in jurs:
    slug = j["slug"]
    longname = j["name_long"]
    jur.append(slug)
    jtup = (longname, slug)
    jurtup.append(jtup)
with open('jurisdictions.json', 'w') as f:
    json.dump(jurs, f)