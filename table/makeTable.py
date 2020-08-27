import pandas as pd
import requests
import json
import os
import re


queryString = "SELECT * FROM VIEW_512252299"
filter = []
json_response = {}

class FilterCondition:

    def __init__(self, attribute: str):
        """A filter condition"""
        self.attribute = attribute

    def toSQL(self):
        raise NotImplementedError("")

class RangeCondition(FilterCondition):

    def __init__(self, attribute: str, lower: float, upper: float):
        self.attribute = attribute
        self.lower = lower
        self.upper = upper

    def toSQL(self):
        return f"{self.attribute} BETWEEN {self.lower} AND {self.upper}"

def filtersToWhere(filters: list):
    return " AND ".join([f.toSQL() for f in filters])

def stringToRangeCondition(attribute: str, lower: str, upper: str):
    if not (is_number(lower) and is_number(upper) and isIdentifier(attribute)):
        print("yikessssssssssssssssssssssss")
        raise Exception("only numbers allowed as inputs for conditions")
    return RangeCondition(attribute, lower, upper)

def isIdentifier(s: str):
    if re.compile("[A-Za-z_]").match(s):
        return True
    return False

def is_number(s: str):
    try:
        float(s)
        return True
    except ValueError:
        return False

def getCache(cache):
    global filter
    filter = cache

def returnResponse():
    print("###########################################################", filter)
    queryString = makeQuery(filter)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(queryString)
    response = requests.post('http://localhost:8089/api/v2/query/data', data = json.dumps({ 'query' : queryString, 'includeUncertainty' : True }))
    resp = response.json()
    return resp

def outputTable():
    print("~~~~~~~~~~~~~~~@@@@@@@@@@@@@@@@@@@@@@@@@@@@@~~~~~~~~~~~~~~~~~~~~~~")
    print(filter)
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

dict = os.system('cat /home/saki/source/web-api-async/vizier-data/.vizierdb/ds/bd52b624/4ea53dcdf4294958be89dfae1c8cb23f/dataset.json')


if __name__ == "__main__":
    main()
