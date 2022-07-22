#! usr/bin/env python3
#%%
TRCPmd = ""
with open('TRCP.md', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('PART'):
            TRCPmd = TRCPmd + '### ' + line + "\n"
        elif  line.startswith('RULE'):
            TRCPmd = TRCPmd + '#### ' + line + "\n"
        else:
           TRCPmd = TRCPmd + '## ' + line + "\n" 
# %%
with open('TRCP-1.md', 'w', encoding='utf-8') as g:
    g.write(TRCPmd)
# %%
