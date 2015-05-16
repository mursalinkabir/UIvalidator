import urllib.request
import requests
from bs4 import BeautifulSoup
url = "http://validator.w3.org/check?uri="
siteurl="www.northsouth.edu"
mainurl=url+siteurl
response =  urllib.request.urlopen(mainurl)

status=response.getheader('x-w3c-validator-status')
errors=response.getheader('X-W3C-Validator-Errors')
warnings=response.getheader('X-W3C-Validator-Warnings')
print("HTML is %s"%(status))
print("HTML has %s Errors"%(errors))
print("HTML has %s Warnings"%(warnings))
#getting line numbers
r = requests.get(mainurl)
html= r.content
soup = BeautifulSoup(html)
g_data = soup.find_all("em")
for itm in g_data:
    lines=itm.text
    print("There is Error in %s" %(lines))
