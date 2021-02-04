import requests,urllib

#https://stackoverflow.com/questions/8928730/processing-http-get-input-parameter-on-server-side-in-python
#r = requests.get('http://127.0.0.1:8000/?param=hazard')

import sys
sys.path
sys.path.append('C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/seismic_risk_v3/Database/')
#print(sys.path)

name="1"
import Writes
path= "C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/seismic_risk_v3/Database/param.txt"
Writes.writefile(path, name)

url='http://127.0.0.1:8000/?param='+ name

headers={}
headers['User-Agent']='Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
req=urllib.request.Request(url, headers=headers)
resp=urllib.request.urlopen(req)
data=resp.read()

print ("python 2.7, not waiting the response")

print (url)

#exec(open("C:/Users/AG/AppData/Roaming/QGIS/QGIS3/profiles/default/python/plugins/seismic_risk_v3/django/request.py").read())

