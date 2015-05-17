__author__ = 'Mursalin'
import requests
from bs4 import BeautifulSoup
r=requests.get("http://www.northsouth.edu/")

# print(r.status_code)
html= r.content
soup = BeautifulSoup(html)
links=soup.find_all("a")
down=0
for itm in links:
    chk=itm.get("href")

    if chk:
        halflink = itm.get("href")

        fulllink= "http://www.northsouth.edu/"+halflink

        r=requests.get(fulllink)
        stat= r.status_code
        if stat!=200:
            print("link is Down and url is %s"%(fulllink))
            down+=1

        else:
            print("Link is UP")
print("Total Down Links are %s"%(down))
