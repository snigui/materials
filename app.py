from flask import Flask, render_template, request, url_for, jsonify, json, redirect
import requests
import table
import plotly
from plotly import graph_objs as go
import pandas as pd
import csv
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output


app = Flask(__name__)
cache = {}
df = pd.DataFrame()
available_indicators = df
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# server = flask.Flask(__name__)
# plot = dash.Dash(__name__, server=server, url_base_pathname='/get/', external_stylesheets=external_stylesheets)

@app.route("/")
def home():
    table.makeTable.getCache([])
    tables= table.makeTable.outputTable()
                # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    tabledata = json.dumps(table.makeTable.getBoolData())
    print(tabledata)
    cols = tables.columns.tolist()
    colNames = json.dumps(cols)
    return render_template("index.html", table=[tables.to_html(header="true")], tabledata=tabledata, colNames=colNames)


@app.route("/add", methods=["POST", "GET"])
def add():
    #cache["first"] = json.loads(request.json), data=dara
    if request.method == "POST":
        #clicking add and remove will save this input
        data = request.json
        global cache
        cache = data
        initial = table.makeTable
        initial.getCache(cache["filters"])
        print(initial.queryString)
        global df
        tables = initial.outputTable()
        df = tables
        print(tables)
        tabledata = json.dumps(table.makeTable.getBoolData())
        cols = tables.columns.tolist()
        print(")()()()()()()()()()()())))(()())")
        colNames = json.dumps(cols)
        return render_template("output.html", table=[tables.to_html(header="true")], tabledata=tabledata, colNames=colNames)
    if request.method == "GET":
        #upon clicking submit this stuff will render
        colNames = []
        print("from GET!")
        print(cache)
        print(cache["filters"])
        # requests.post('https://localhost:8050/get', data = cache, verify=False)
        initial = table.makeTable
        initial.getCache(cache["filters"])
        tables = initial.outputTable()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        tabledata = json.dumps(table.makeTable.getBoolData())
        cols = tables.columns.tolist()
        print(cols)
        colNames = json.dumps(cols)
        return render_template("output.html", table=[tables.to_html(header="true")], tabledata=tabledata, colNames=colNames)
    return render_template("output.html")

# @app.route("/dash", methods=['GET'])
# def dash():
#     return plot.index()

plot = dash.Dash(__name__, server=app, url_base_pathname='/dash/',external_stylesheets=external_stylesheets)

print("broooooooooooooooooo hwy ")
print(df)

colNames = ['ABS_WF_D', 'STAT_CC_D', 'STAT_CC_A', 'STAT_CC_D_AN', 'STAT_CC_A_CA', 'STAT_N', 'STAT_N_D', 'STAT_N_A', 'ABS_F_D', 'CT_F_CONN_D', 'CT_F_CONN_D_AN', 'CT_F_CONN_A_CA', 'DISS_WF10_D', 'DISS_F10_D', 'DISS_F2_D', 'DISS_PROB_REACH_I', 'STAT_E', 'CT_E_CONN', 'CT_F_E_CONN', 'CT_E_D_AN', 'CT_E_A_CA', 'CT_N_D_ADJ_AN', 'CT_F_D_TORT1', 'CT_WTORT_D', 'CT_N_A_ADJ_CA', 'CT_F_A_TORT1', 'CT_WTORT_A', 'INT_X', 'INT_D', 'INT_G', 'INT_R', 'NOMALIZED_INTERFACE', 'JSC', 'JSC_D', 'INT_R_INT_D', 'INT_D_INT_G', 'JSC_INT_D']


plot.layout = html.Div([
    html.Div([


        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in colNames],
                value='STAT_N_A'
            ),
            dcc.RadioItems(
                 id='xaxis-type',
                 options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                 value='Linear',
                 labelStyle={'display': 'inline-block'}
             )
        ],style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in colNames],
                value='STAT_N_D'
            ),
             dcc.RadioItems(
                 id='yaxis-type',
                 options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                 value='Linear',
                 labelStyle={'display': 'inline-block'}
             )
        ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic'),

])


@plot.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-column', 'value'),
     Input('xaxis-type', 'value'),
     Input('yaxis-type', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type):
    dff = df
    print("whyyyyyyyyyyyyyyyyyy")
    print(dff)
    print(xaxis_column_name)
    return {
        'data': [dict(
            x=dff[xaxis_column_name],
            y=dff[yaxis_column_name],
            text=dff['STAT_N_D'] ,
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': dict(
            xaxis={
                'title': xaxis_column_name,
                #'type': 'linear'
                'type': 'linear' if xaxis_type == 'Linear' else 'log'
            },
            yaxis={
                'title': yaxis_column_name,
                #'type': 'linear'
                'type': 'linear' if yaxis_type == 'Linear' else 'log'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }



if __name__ == "__main__":
    plot.run_server(host="localhost", port=2000, debug=True)
    # app.run(host="localhost", port=2000, debug=True)
    # plot.run_server(host="localhost", port=2000, debug=True)
