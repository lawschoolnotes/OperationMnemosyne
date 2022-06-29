#%%
import os
import cap
from dotenv import load_dotenv
#%%
load_dotenv()
#%%
capp = cap.Cap()
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
