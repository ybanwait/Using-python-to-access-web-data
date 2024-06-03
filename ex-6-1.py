import urllib.parse, urllib.error, urllib.request
import json

while True:
    url=input("Enter Location:")
    if len(url)<1:break
    param=dict()

    print("Retrieving:", url)
    data=urllib.request.urlopen(url)
    dt=data.read().decode()
    print("Retrieved", len(dt), "characters")
    
    try:
       jdata=json.loads(dt)
    except:
        jdata=False        

    if jdata!=False:
        
        print("count", len(jdata["comments"]))
        total=0
        for item in jdata["comments"]:
            total+=int(item["count"])

        print("sum:", total)    