import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

def parsing(url,count):
    if count>0:
        position=18
        poscount=1
        html=urllib.request.urlopen(url).read()
        sp=BeautifulSoup(html, 'html.parser')
        tags=sp('a')
        
        for tag in tags:
            if poscount==position:
                lnk=tag.get("href", 0)
                print(lnk)
                count=count-1
                parsing(lnk, count)
                break
            poscount=poscount+1
            

#Retrieve all of the anchor tags
count=7
parsing('http://py4e-data.dr-chuck.net/known_by_Austen.html', count)

