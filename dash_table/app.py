# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
import matplotlib.pyplot as plt
import csv
import requests
import json
#import os


#cat vizier-data/.vizierdb/ds/bd52b624/0ab76909f90b4bbcb45fa9b055cc1a48/dataset.json

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#print(os.system('cat /home/saki/source/web-api-async/vizier-data/.vizierdb/ds/bd52b624/0ab76909f90b4bbcb45fa9b055cc1a48/dataset.json'))

# url = 'http://localhost:5000/vizier-db/api/v1/projects/bd52b624/datasets/acda8df615cc41e7866dbb29ae1fe36b/csv'
# resp = requests.get(url)
#
# with open('data1.csv','w') as f:
#     writer = csv.writer(f)
#     for line in resp.iter_lines():
#         writer.writerow(line.# app.layout = dash_table.DataTable(
#     id='table-paging-and-sorting',
#     columns=[
#         {'name': i, 'id': i, 'deletable': True} for i in sorted(dataTable.columns)
#     ],
#     page_current=0,
#     page_size=PAGE_SIZE,
#     page_action='custom',
#
#     sort_action='custom',
#     sort_mode='single',
#     sort_by=[]
# )
#
#
# @app.callback(
#     Output('table-paging-and-sorting', 'data'),
#     [Input('table-paging-and-sorting', "page_current"),
#      Input('table-paging-and-sorting', "page_size"),
#      Input('table-paging-and-sorting', 'sort_by')])decode('utf-8').split(','))
#
# df = pd.read_csv('data1.csv')

response = requests.post('http://localhost:8089/api/v2/query/data', data = json.dumps({ 'query' : 'SELECT * FROM VIEW_1726018377', 'includeUncertainty' : False }))
json_response = response.json()
print(json_response['data'])
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
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
print(cols)
print("~~~~~~~~~~~~~~~~")
print(rows)
dataTable = pd.DataFrame(rows, columns=cols)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(dataTable)
#loop through the dicts in schema and get col names with indicies, the corresponsing indicies in each list of data is the value of the col's index at the
#list's index as row number


#df[' index'] = range(1, len(df) + 1)


app = dash.Dash(__name__)

PAGE_SIZE = 5

app.layout = dash_table.DataTable(
    id='table-paging-and-sorting',
    columns=[
        {'name': i, 'id': i, 'deletable': True} for i in sorted(dataTable.columns)
    ],
    page_current=0,
    page_size=PAGE_SIZE,
    page_action='custom',

    sort_action='custom',
    sort_mode='single',
    sort_by=[]
)


@app.callback(
    Output('table-paging-and-sorting', 'data'),
    [Input('table-paging-and-sorting', "page_current"),
     Input('table-paging-and-sorting', "page_size"),
     Input('table-paging-and-sorting', 'sort_by')])
# def update_table(page_current, page_size, sort_by):
#     return 1
    #
    # if len(sort_by):
    #     dff = df.sort_values(
    #         sort_by[0]['column_id'],
    #         ascending=sort_by[0]['direction'] == 'asc',
    #         inplace=False
    #     )
    # else:
    #     # No sort is applied
    #     dff = df
    # # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``")
    # # print(dff.iloc[
    # #     page_current*page_size:(page_current+ 1)*page_size
    # # ].to_dict('records'))
    # return dff.iloc[
    #     page_current*page_size:(page_current+ 1)*page_size
    # ].to_dict('records')

dataTable.plot.scatter(x='CASE_NAME', y='JSC', c='DarkBlue')
plt.show

if __name__ == '__main__':
    app.run_server(debug=True)
