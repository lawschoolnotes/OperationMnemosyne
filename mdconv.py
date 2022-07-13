#! usr/bin/python3
#%%
import markdown
import glob
import os.path as path
#%%

file_path = 'C:\\Users\\Public\\School\\lawschoolnotes\\vault'
file_type = 'md'
globpath = f"{file_path}\\**\\*.{file_type}"
files = glob.glob(globpath, recursive=True)
#%%
for file in files:
    noext = path.splitext(file)[0]
    markdown.markdownFromFile(input=f'{file}', output=f'{noext}.html')
