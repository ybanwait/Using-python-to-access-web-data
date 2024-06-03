import urllib.parse, urllib.error, urllib.request
import json

while True:
    address=input("Enter Location:")
    if len(address)<1:break
    param=dict()
    serviceurl='http://py4e-data.dr-chuck.net/json?'
    param['key']=42
    param['address']=address
    url=serviceurl+urllib.parse.urlencode(param)
    print("Retrieving:", url)
    data=urllib.request.urlopen(url)
    dt=data.read().decode()
    print("Retrieved", len(dt), "characters")
    
    try:
       jdata=json.loads(dt)
    except:
        jdata=False        

    if jdata==False or 'status' not in jdata or jdata['status']!='OK':
        print("=====Failure to retrieve======")
        print(dt)
        continue
    
    print("Place id", jdata['results'][0]["place_id"])