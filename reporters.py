#%%
import json

with open('./data/reporterslist.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

reporters = [datum['short_name'] for datum in data]
#%%
reps = [*set(reporters)]
reps.sort()
# %%
with open('./data/schemas/reporters.schema.json', 'a', encoding='utf-8') as g:
    json.dump(reps, g)
# %%
