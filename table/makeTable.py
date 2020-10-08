import pandas as pd
import requests
import json
import os
import re
import urllib.parse


queryString = "SELECT * FROM material_science"
filter = []
json_response = {}

class FilterCondition:

    def __init__(self, attribute):
        """A filter condition"""
        self.attribute = attribute

    def toSQL(self):
        raise NotImplementedError("")

class RangeCondition(FilterCondition):

    def __init__(self, attribute, lower, upper):
        self.attribute = attribute
        self.lower = lower
        self.upper = upper

    def toSQL(self):
        return self.attribute + " BETWEEN " + self.lower +" AND " +self.upper

def filtersToWhere(filters):
    return " AND ".join([f.toSQL() for f in filters])

def stringToRangeCondition(attribute, lower, upper):
    if not (is_number(lower) and is_number(upper) and isIdentifier(attribute)):
        print("yikessssssssssssssssssssssss")
        raise Exception("only numbers allowed as inputs for conditions")
    return RangeCondition(attribute, lower, upper)

def isIdentifier(s):
    if re.compile("[A-Za-z_]").match(s):
        return True
    return False

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def getCache(cache):
    global filter
    filter = cache

def returnResponse():
    # print("###########################################################", filter)
    queryString = makeQuery(filter)
    # print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    workflow_url = 'https://demo.vizierdb.info/vizier-db/api/v1/projects/9679e97a/branches/9d2942bd/head/sql?query='
    query = queryString
    url = 'https://demo.vizierdb.info/auth/public?workflow-url=' + urllib.parse.quote(workflow_url) + urllib.parse.quote(urllib.parse.quote(query))
    print(url)
    response = requests.get(url)
    resp = response.json()
    print("++++++++++++++++++++++++++++++")
    return resp

def outputTable():
    # print("~~~~~~~~~~~~~~~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@~~~~~~~~~~~~~~~~~~~~~~")
    # print(filter)
    # queryString = makeQuery(filter)
    # print(queryString)
    # response = requests.post('http://localhost:8089/api/v2/query/data', data = json.dumps({ 'query' : queryString, 'includeUncertainty' : True }))
    global json_response
    # #json_response = {}
    json_response = returnResponse()
    # requests.post('https://localhost:8050/get', data = json_response)
    #print("wiat what huhhhhhhhhhhhhhhhhhhhh ")
    #print(json_response)
    cols = []
    rows = []
    #col names:
    counter = -1
    for col in json_response['schema']:
        cols.append(col['name'])
    for row in json_response['data']:
        counter+=1
        rows.append(row)
        #print(row, "\n", counter)
    dataTable = pd.DataFrame(rows, columns=cols)
    #print("bruvvvvvvvvvv why???")
    #learn to process variable sql queries
    #then query the database...
    return dataTable

def getBoolData():
    print(queryString)
    boolean= json_response['colTaint']
    boolData = []
    boolRow = []
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
    if (len(boolData) < 1):
        return ["%"]
    return boolData


def makeQuery(filters):
    #assuming queries is a list of lists
    query = queryString
    addOn = ""
    chunks= []
    filterNum = len(filters)
    if (filterNum > 0):
        query = queryString + " WHERE "
    else:
        return query
    for filterString in filters:
        filter = filterString.strip().split(',')
        if (len(filter) > 2):
            addOn = stringToRangeCondition(filter[0], filter[1], filter[2])
            chunks.append(addOn)
        else:
            raise Exception("invalid range input")
    return query + filtersToWhere(chunks)

dict = os.system('cat /home/saki/source/web-api-async/vizier-data/.vizierdb/ds/649ed2dd/DATASOURCE_MATERIALS_16443958/dataset.json')


if __name__ == "__main__":
    main()
