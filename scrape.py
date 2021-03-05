  
import requests

r = requests.get('https://services5.arcgis.com/54falWtcpty3V47Z/arcgis/rest/services/City_Maintained_Trees/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
data = r.text
if data is None:
    print("Data was None")
else:
  print(data)
