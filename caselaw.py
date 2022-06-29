import requests

headers={'Authorization': 'Token d208f8f46b908b95f4872f86422d3845c5fcffd6'}

cases='https://api.case.law/v1/cases/?full_case=true&body_format=text&cite=160+Tex.+482'


r= requests.get(cases, headers=headers)

print(r)
