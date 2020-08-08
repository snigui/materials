import pandas as pd
import requests
import json
import os
## TODO:
# change the path of serving the table and plot to /charts or something
# have the input json and build the sql query out of it
# plot the tableand plotwith the data from that query
# next steps:
# make the table better!
# make the plot not use csv



def outputTable(cache):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(cache)
    queryString = makeQuery(cache)
    print(queryString)
    response = requests.post('http://localhost:8089/api/v2/query/data', data = json.dumps({ 'query' : queryString, 'includeUncertainty' : True }))
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
    #learn to process variable sql queries
    #then query the database...
    return dataTable

def makeQuery(filters):
    #assuming queries is a list of lists
    query = "SELECT * FROM VIEW_230163258"
    addOn = ""
    count = 0
    filterNum = len(filters)
    if (filterNum > 0):
        query = "SELECT * FROM VIEW_230163258 WHERE "
    else:
        return query
    for filterString in filters:
        filter = filterString.split(',')
        count += 1
        if (count == filterNum):
            addOn = filter[0] + " BETWEEN " + filter[1] + " AND " + filter[2]
        else:
            addOn = filter[0] + " BETWEEN " + filter[1] + " AND " + filter[2] + " AND "
        query += addOn
    return query

dict = os.system('cat /home/saki/source/web-api-async/vizier-data/.vizierdb/ds/bd52b624/6d1950e574d04349adeb60f41ec21d50/dataset.json')
#print(dict)
# template = 'SELECT * FROM VIEW_230163258 WHERE {{name}} BETWEEN {{lower}} AND {{upper}} AND {{name1}} BETWEEN {{lower1}} AND {{upper1}}'
# data = {"name": "JSC", "lower":1, "upper":10, "name1": "STAT_N_D", "lower1":0, "upper1":215}
# query, bind_params= j.prepare_query(template,data)
# print(query)
# print(bind_params)
# queryString = makeQuery(filters)
# print(queryString)
# response = requests.post('http://localhost:8089/api/v2/query/data', data = json.dumps({ 'query' : queryString, 'includeUncertainty' : True }))
# json_response = response.json()
#print(json_response)
#print(json_response['colTaint'])
#boolean= json_response['colTaint']
boolean = [[True, False, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]]
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
    if (len(boolRow) > 0):
        boolData.append(boolRow)
    boolRow = []
    index = -1
#print(boolData)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print(boolData[32])
# if (boolData[4] == 1 and boolData[30] == 1 and boolData[31] == 1 and boolData[32] ==1):
#     print("yeah???????????????????????????????????????????///")

#print(dataTable)
