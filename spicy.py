#! usr/bin/python3
#%%
from bs4 import BeautifulSoup

# %%
with open('conlawQuimbee.html', 'r', encoding='utf-8') as doc:
    soup = BeautifulSoup(doc, 'html.parser')
# %%
cases = soup.find_all('li', class_='c-index-list_item')
#%%

#for case in cases:
# %%
prettyCases = [case.prettify() for case in cases]
#%%
listStr = "\n".join(prettyCases)
# %%
caseNames = [case.get_text() for case in cases]
# %%
listSoup = BeautifulSoup(listStr, 'html.parser')
#%%
for string in listSoup.stripped_strings:
    print(repr(string))
#%%
print(*prettyCases, sep='\n')


# %%
print(*caseNames, sep='\n')
# %%
#def listsoup(caseList: list):
#%%
for case in prettyCases:
    souplist = BeautifulSoup(case, 'html.parser')
    stripsoup = souplist.stripped_strings
    soupstring = [soupstring.append(string) for string in stripsoup]
# %%
