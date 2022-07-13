#%%
import os
from dotenv import load_dotenv
import json
import cap

load_dotenv()
capp = cap.Cap()

#%%
with open("thomasMajority.json", "r") as f:
    thomasMajority = json.load(f)
#%%
thomasMajority = thomasMajority["results"]
#%%
offCite = []
for r in thomasMajority:
   citation = r["citations"][0]["cite"]
   name = r["name_abbreviation"]
   case = r["id"]
   ctdict = {"style": name, "cite": citation, "id": case}
   offCite.append(ctdict)


#%%
with open("ctCites.json", "w") as j:
    CThomas = json.dump(offCite, j)
#%%
with open("ctCases.json", "a") as g:
    for cite in offCite:
        ids = cite["id"]
        fullcase = capp.get_case(ids, full_case=True)
        json.dump(fullcase, g)
    
# %%
