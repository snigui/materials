import pandas as pd
import requests
import json
import os

dict = os.system('cat /home/saki/source/web-api-async/vizier-data/.vizierdb/ds/bd52b624/acda8df615cc41e7866dbb29ae1fe36b/dataset.json')
print(dict)

response = requests.post('http://localhost:8089/api/v2/query/data', data = json.dumps({ 'query' : 'SELECT * FROM VIEW_883197945', 'includeUncertainty' : False }))
json_response = response.json()
cols = []
rows = []
#col names:
counter = -1
for col in json_response['schema']:
    cols.append(col['name'])
    #print(col['name'])
for row in json_response['data']:
    counter+=1
    rows.append(row)
    #print(row, "\n", counter)

dataTable = pd.DataFrame(rows, columns=cols)
print(dataTable)
