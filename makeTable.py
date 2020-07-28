import pandas as pd
import requests
import json
import os

dict = os.system('cat /home/saki/source/web-api-async/vizier-data/.vizierdb/ds/bd52b624/6d1950e574d04349adeb60f41ec21d50/dataset.json')
#print(dict)

response = requests.post('http://localhost:8089/api/v2/query/data', data = json.dumps({ 'query' : 'SELECT * FROM VIEW_230163258', 'includeUncertainty' : True }))
json_response = response.json()
#print(json_response['colTaint'])
#boolean= json_response['colTaint']
boolean = [[False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False],
 [True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]]
boolData = []
boolRow = []
#make it sorted and make that thing in JS go through both lists??
#no wait make it go through both lists of same size and for the index at that num,
#check if it is 1 so for i to last num, if boolData[i] ==1, then color there
#try with smaller one first first the first 2 rows which is 62 entires so len == 62
#print(len(boolean[0]))
#nah just have it as a 2d array and save indicies for each array as it is
#and keep adding up rowids in JS and get that rowID's list and then color those indicies
index = -1
for i in boolean:
    for j in i:
        index +=1
        if j:
            boolRow.append(index)
    boolData.append(boolRow)
    boolRow = []
    index = -1
print(boolData)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print(boolData[32])
# if (boolData[4] == 1 and boolData[30] == 1 and boolData[31] == 1 and boolData[32] ==1):
#     print("yeah???????????????????????????????????????????///")
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
#print(dataTable)
