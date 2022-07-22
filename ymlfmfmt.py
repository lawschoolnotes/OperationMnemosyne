#%%
from frontmatter import Frontmatter
import glob
import os.path
import json
import re
#%%
basepath = 'C:\\Users\\Public\\note-recover\\lawschoolnotes.github.io\\vault\\notes'
file_type = 'md'
stempath = '\\1L'
newpath = basepath + stempath
globpath = f"{basepath}\\**\\*.{file_type}"
files = glob.glob(globpath, recursive=True)
regex = r"(^\w* ?:\n)"
sub = ""
# %%
fronted = []
nofront = []
for file in files:
    with open(file, 'r+', encoding='utf-8') as f:
        if f.readline(3) == '---':
            fronted.append(file)              
        else:
            nofront.append(file)
            print(f'No frontmatter in {file}')

# %%
safety = {}
for note in fronted:
    with open(note, 'r+', encoding='utf-8') as g:
        test_str = g.read()
        resulttup = re.subn(regex, sub, test_str, 0, re.MULTILINE)
        result = resulttup[0]
        subs = resulttup[1]
        safety[note] = subs
#%%
pairs = safety.items()
nosub = []
for pair in pairs:
    if pair[1] > 0:
        file = pair[0]
        substitutions = str(pair[1])
        print(f'{file} will have {substitutions} replacements')
    else:
        nosub.append(pair[0])
    
#%%
        if subs > 0:
            g.write(result)
            print(f'{subs} substitutions made')
        else:
            print(f'{subs} substitutions made in {note}')