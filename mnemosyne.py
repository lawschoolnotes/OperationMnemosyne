#%%
import os
from dotenv import load_dotenv
import json
import cap

load_dotenv()
capp = cap.Cap()

#%%
CThomas = capp.search_cases(court="us", author="Thomas", full_case=False)
#%%
