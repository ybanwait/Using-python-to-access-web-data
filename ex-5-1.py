import urllib.request,urllib.parse,urllib.error
import xml.etree.ElementTree as ET

while True:
    url=input("Enter Location:")
    if len(url)<1:break
    parms=dict()
    
    print('Retrieving', url)
    sol=urllib.request.urlopen(url)
    data=sol.read()
    print('Retrieved', len(data), "characters")
    print(data.decode())
    tree=ET.fromstring(data)
    res=tree.findall('.//count')
    print('count', len(res))
    count=0
    for cnt in res:
        count+=int(cnt.text)
    print('sum', count)