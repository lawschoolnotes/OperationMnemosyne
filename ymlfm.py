#%%
from frontmatter import Frontmatter
import glob
import os.path
import json
#%%
basepath = 'C:\\Users\\Public\\School\\lawschoolnotes'
file_type = 'md'
stempath = '\\vault\\notes'
newpath = basepath + stempath
globpath = f"{basepath}\\**\\*.{file_type}"
files = glob.glob(globpath, recursive=True)
# %%
fronted = []
nofront = []
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        if f.readline(3) == '---':
            fronted.append(file)
        else:
            nofront.append(file)    
# %%
jdict = []
for front in fronted:
    base = os.path.basename(front)
    noext = os.path.splitext(base)[0]
    note = Frontmatter.read_file(front)
    newdict = {noext : note}
    jdict.append(newdict)

# %%
jsdict = json.dumps(jdict, indent=4, default=str)
# %%
loaddict = json.loads(jsdict)
# %%
with open('notes.json', 'w', encoding='utf-8') as f:
  json.dump(loaddict, f, ensure_ascii=False)
#%%
notedict = {"hasFrontmatter": fronted, "noFrontmatter": nofront}
# %%
with open('notedict1.json', 'w', encoding='utf-8') as g:
  json.dump(notedict, g, ensure_ascii=False)
# %%
needs_front = []
for name in nofront:
    if name.startswith(newpath):
        needs_front.append(name)
# %%
import re
#%%
