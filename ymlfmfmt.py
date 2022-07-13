#%%
from frontmatter import Frontmatter
import glob
import os.path
import json
import re
#%%
basepath = 'C:\\Users\\Public\\School\\lawschoolnotes'
file_type = 'md'
stempath = '\\vault\\notes'
newpath = basepath + stempath
globpath = f"{basepath}\\**\\*.{file_type}"
files = glob.glob(globpath, recursive=True)
regex = r"(^\w* ?:$)"
sub = ""
# %%
fronted = []
nofront = []
for file in files:
    with open(file, 'r+', encoding='utf-8') as f:
        if f.readline(3) == '---':
            fronted.append(file)
            test_str = f.read()
            resulttup = re.subn(regex, sub, test_str, 0, re.MULTILINE)
            result = resulttup[0]
            subs = resulttup[1]
            if subs > 0:
                f.write(result)
            else:
                print(f'{subs} substitutions made')

# %%
