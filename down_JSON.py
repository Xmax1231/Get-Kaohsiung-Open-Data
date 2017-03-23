# -*- coding: utf-8 -*-

# import
import requests

URL = "http://data.kcg.gov.tw/api/action/datastore_search?resource_id=b0f29421-a111-4c4e-b5d0-a21dc2f9a043&limit=23038"
data = {'limit':23038}
s = requests.session()
file = open('t.json', 'w')
t = s.post(URL)
file.write(t.text)
print('a')