import urllib.request

url = "http://validator.w3.org/check?uri="
siteurl="http://www.heppnetz.de"
mainurl=url+siteurl
response =  urllib.request.urlopen(mainurl)
server=response.getheader('x-w3c-validator-status')
print(server)

