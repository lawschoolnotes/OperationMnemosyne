#%%
import os
from dotenv import load_dotenv
import json
import capUpdate

load_dotenv()
capp = capUpdate.Cap()
# %%
# %%
def caseSearch(caseName: str, fullCase: bool = False):
    results = capp.search_cases(name_abbreviation=f'{caseName}', full_case= fullCase)
    if results['count'] >= 1:
        return results["results"][0]
    else:
        raise Exception(f"Search for {caseName} returns no results.")
#%%
def listSearch(caseList: list, fullCase: bool = False):
    result_List = []
    if fullCase == True:
        try:
            for case in caseList:
                search_results = caseSearch(case, fullCase)
                casebody = search_results["casebody"]
                data = casebody["data"]
                opinions = data["opinions"]
                opinion = opinions[0]
                opinion = opinion["text"]        
                result_Dict = {"caseStyle": case, "id": search_results["id"], "opinion": opinion}
                result_List.append(result_Dict)
            print("Search Complete")
            return result_List
        except:
            Exception(f"Search for {case} failed")
        finally:
            print("Search Incomplete")
            return result_List
    else:
        for case in caseList:
            search_results = caseSearch(case, fullCase)
#%%    
with open('conlawcases.md', 'r', encoding='utf-8') as f:
    cases = f.read().splitlines()
#%%
with open('conlawQuim.json', 'r', encoding='utf-8') as j:
    cason = json.load(j)

# %%
conlaw = listSearch(cases)
# %%
for case in cason:
    cite = case['cite']
    