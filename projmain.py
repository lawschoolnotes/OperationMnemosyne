#! usr/bin/env/python3
# @author: tecumseh
# Main script
#%% Import what you need 
import json
import capCase
from dotenv import load_dotenv
#%% Load environmental variables
load_dotenv()

#%% Instantiate the class
cap = capCase.Cap()

#%% Set the location variables
data_dir = "./data/"
case_list = "data_obj.json"
case_list_path = rf"{data_dir}{case_list}"

#%% Build the query data
with open(case_list_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
data = data['caseList']
#%%
for datum in data:
    parCites = datum['cite']
    for cite in parCites:
        vol = cite.get('vol')
        rep = cite.get('reporter')
        page = cite.get('page')
        combCite = f"{vol} {rep} {page}"
        if rep == "U.S.":
            cite['primary'] = True
        else:
            cite['primary'] = False
        
# %% API call section
def caseSearch(citation: str, fullCase: bool = False):
    results = cap.search_cases(citation=f'{citation}', full_case= fullCase)
    if results['count'] == 1:
        call_results = results['results']
        return call_results
    elif results['count'] == 0:
        raise Exception(f"Search for {citation} returns no results.")
    elif results['count'] > 10:
        raise Exception('Too many results. Please validate your request')
    else:
        confirmation(call_results)

def bulkSearch(caseList: list):
    global readyList
    global missingList
    global confirmList
    readyList = []
    missingList = []
    confirmList = []
    for case in caseList:
        results = cap.search_cases(citation=f'{case}', full_case= False)
        if results['count'] == 1:
            resultsFull = cap.search_cases(citation=f'{case}', full_case= True)
            caseResults = resultsFull['results']
            case_data = {"id": caseResults["id"],
                "name": caseResults["name"],
                "name_abbreviation": caseResults["name_abbreviation"],
                "decision_date": caseResults["decision_date"],
                "court_id": caseResults["court"]["id"],
                "court_name": caseResults["court"]["name"],
                "court_slug": caseResults["court"]["slug"],
                "judges": str(caseResults["casebody"]["data"]["judges"]),
                "attorneys": str(caseResults["casebody"]["data"]["attorneys"]),
                "citations": str(caseResults["citations"]),
                "url": caseResults["url"],
                "head": caseResults["casebody"]["data"]["head_matter"],
                "body": caseResults["casebody"]["data"]["opinions"][0]["text"]}
            readyList.append(case_data)
        elif results['count'] == 0:
            missingList.append(case)
        else:
            confirmList.append(case)

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

def confirmation(result: list):
    pick_result = [r['name'] for r in result]
    print('The search returned more results than expected. Please confirm the search result which matches your request')
    print
    
#%% Load data
with open(case_list_path, 'r', encoding='utf-8') as f:
    data = json.load(f) 
cases = data['caseList']
