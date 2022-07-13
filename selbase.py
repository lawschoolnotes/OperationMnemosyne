#! usr/bin/python3
#%%
from selenium import webdriver
#from selenium.webdriver.chrome import *
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
#%%
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
#%%
bkstr_url = 'https://www.bkstr.com/northtexasatdallasstore/course-materials-results?shopBy=course&divisionDisplayName=%7C%7C%7C&departmentDisplayName=LAW%7CLAW%7CLAW%7CLAW&courseDisplayName=7414%7C7325%7C7214%7C7313&sectionDisplayName=001%7C001%7C001%7C301&programId=1660&termId=100075919'
# %%
from bs4 import BeautifulSoup
from urllib.request import urlopen

with open('books.html') as f:
    html = f.read()
soup = BeautifulSoup(html, "html.parser")
# %%
txt = soup.get_text()
# %%
import re
# %%
regex = r"(\n{2,})"
sub = r"\n"
test_str = txt
#%%
result = re.sub(regex, sub, test_str, 0, re.MULTILINE)

# %%
