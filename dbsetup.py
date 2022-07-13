#%%
from tinydb import TinyDB, Query
import json
#%%
db = TinyDB("ctdb2.json")
# %%
with open('ctdb.json', 'r', encoding='utf-8') as infile:
    data = json.load(infile)
#%%
db.insert_multiple(data)
#%%
length = Query()
db.search(len(length.parties) < 10)
# %%
db.all()
# %%
