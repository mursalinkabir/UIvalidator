__author__ = 'Mursalin'
import urllib.request

#css validator
url = "https://jigsaw.w3.org/css-validator/validator?uri="
siteurl="http://www.heppnetz.de"
mainurl=url+siteurl
print(mainurl)
response =  urllib.request.urlopen(mainurl)
# server=response.getheader('x-w3c-validator-status')
print(response)