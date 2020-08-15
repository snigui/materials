from flask import Flask, render_template, request, url_for, jsonify, json, redirect
import requests
import makePlot
import makeTable
import plotly
from plotly import graph_objs as go
import pandas as pd
import csv


# make the index.html show only 1 input for form
# fix table with boolean coloring and remove search bar
# make plot not use csv and maybe directly read of sql data


app = Flask(__name__)
cache = {}

@app.route("/")
def home():
    # traceValues = makePlot.plotData()
    # print(traceValues)
    # trace = go.Scatter(x = traceValues['x'], y = traceValues['y'])
    # data =[trace]
    # scatter = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    # table = makeTable.dataTable
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # tabledata = json.dumps(makeTable.boolData)
    # print(tabledata)
    # table=[table.to_html(classes='data',header="true")]
    #table=[table.to_html(header="true")], tabledata=tabledata
    table = makeTable.outputTable([])
                # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    tabledata = json.dumps(makeTable.getBoolData())
    print(tabledata)
    cols = table.columns.tolist()
    colNames = json.dumps(cols)
                #table=[table.to_html(header="true")], tabledata=tabledata
    return render_template("index.html", table=[table.to_html(header="true")], tabledata=tabledata, colNames=colNames)


@app.route("/add", methods=["POST", "GET"])
def add():
    #cache["first"] = json.loads(request.json), data=dara
    if request.method == "POST":
        #clicking add and remove will save this input
        data = request.json
        global cache
        cache = data
        table = makeTable.outputTable(cache["filters"])
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        tabledata = json.dumps(makeTable.getBoolData())
        cols = table.columns.tolist()
        print(")()()()()()()()()()()())))(()())")
        print(cols)
        colNames = json.dumps(cols)
            #table=[table.to_html(header="true")], tabledata=tabledata
        return render_template("output.html", table=[table.to_html(header="true")], tabledata=tabledata, colNames=colNames)
        #print("from POST")
        #print(data)
        #print(cache["descriptors"])
            #table=[table.to_html(header="true")], tabledata=tabledata
    if request.method == "GET":
        #upon clicking submit this stuff will render
        colNames = []
        print("from GET!")
        print(cache)
        print(cache["filters"])
        table = makeTable.outputTable(cache["filters"])
            # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        tabledata = json.dumps(makeTable.getBoolData())
        cols = table.columns.tolist()
        print(")()()()()()()()()()()())))(()())")
        print(cols)
        colNames = json.dumps(cols)
            #table=[table.to_html(header="true")], tabledata=tabledata
        return render_template("output.html", table=[table.to_html(header="true")], tabledata=tabledata, colNames=colNames)
    return render_template("output.html")


if __name__ == "__main__":
    app.run(host="localhost", port=2000, debug=True)
