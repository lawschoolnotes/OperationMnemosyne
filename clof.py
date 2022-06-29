#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 17:00:15 2021

@author: braym
"""
import requests

citation = input('Input Citation as Vol Reporter Page (e.g 491 U.S. 397): ')

apiString = 'https://api.case.law/v1/cases/?full_case=true&cite=' + citation
tokenString ="d208f8f46b908b95f4872f86422d3845c5fcffd6"
caseToken = "Token " + tokenString
response = requests.get(apiString, headers={'Authorization': caseToken}
)

responseDic = response.json()['results'][0]
responseDic = responseDic['casebody']
responseDic = responseDic['data']
responseDic = responseDic['opinions'][0]
responseDic = responseDic['text']

cite_list = citation.split()
fn = cite_list[0]+'-'+cite_list[1]+'-'+cite_list[2]+'-opinion.md'

with open(fn, 'w') as text_file:
    text_file.write(responseDic)
    
