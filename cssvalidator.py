__author__ = 'Mursalin'
import requests
from bs4 import BeautifulSoup
url="https://jigsaw.w3.org/css-validator/validator?uri="
siteurl="http://www.heppnetz.de"
mainurl=url+siteurl
localurl="http://localhost/cssvalid/validator.htm"
r = requests.get(mainurl)
html= r.content

soup = BeautifulSoup(html)
g_data = soup.find_all("h3")#error count
g_data2 = soup.find_all("td",{"class":"linenumber"})#line number fetch
print(g_data)
print("Below are the Line Numbers")
for itm in g_data2:
    Errorval = itm.text
    print("There Is an Error at Line Number %s"%(Errorval))