#%%
import os
from capexamples import *
from capexamples.python_wrapper import cap
from dotenv import load_dotenv
#%%
load_dotenv()

#%%
capp = cap.Cap()

#%%
whether = capp.search_cases(search_term="whether ", full_case=False)
#%%
scotus =  capp.get_courts(name="Supreme Court")
#%%
results = scotus["results"]
#%%
jur = []
for result in results:
    pairs = {"name":result["name"], "jurisdiction":result["jurisdiction"]}
    jur.append(pairs)
# %%
