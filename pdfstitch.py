#%%
from PyPDF2 import PageRange, PdfReader
# %%
pdffile = 'conlaw21.pdf'
reader = PdfReader(pdffile)
#%%
page = reader.pages[15:29]
#%%
first = reader.pages[0]

# %%
txtstr = ""
for p in page:
    text = p.extract_text()
    txtstr = txtstr + text
# %%
