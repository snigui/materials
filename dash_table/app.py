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
import csv
import requests

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

url = 'http://localhost:5000/vizier-db/api/v1/projects/12020d28/datasets/6070d166f8f846c2a609cdb0ea65ad12/csv'
resp = requests.get(url)

with open('data.csv','w') as f:
    writer = csv.writer(f)
    for line in resp.iter_lines():
        writer.writerow(line.decode('utf-8').split(','))

df = pd.read_csv('data.csv')

#df[' index'] = range(1, len(df) + 1)

print(df)
print("`~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")
print(df.columns)

app = dash.Dash(__name__)

PAGE_SIZE = 5

app.layout = dash_table.DataTable(
    id='table-paging-and-sorting',
    columns=[
        {'name': i, 'id': i, 'deletable': True} for i in sorted(df.columns)
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
def update_table(page_current, page_size, sort_by):
    if len(sort_by):
        dff = df.sort_values(
            sort_by[0]['column_id'],
            ascending=sort_by[0]['direction'] == 'asc',
            inplace=False
        )
    else:
        # No sort is applied
        dff = df

    return dff.iloc[
        page_current*page_size:(page_current+ 1)*page_size
    ].to_dict('records')

if __name__ == '__main__':
    app.run_server(debug=True)
