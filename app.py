from flask import Flask, render_template, request, url_for, jsonify, json, redirect, send_file
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
cache = {"filters": ""}
df = pd.DataFrame()
available_indicators = df
initial = table.makeTable
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', '/static/css/template.css']


#
# server = flask.Flask(__name__)
# plot = dash.Dash(__name__, server=server, url_base_pathname='/get/', external_stylesheets=external_stylesheets)

@app.route("/", methods=["GET"])
def home():
    global cache
    tabledata = {}
    initial.getCache(cache["filters"])
    tables = initial.outputTable()
    global df
    df = tables
    # if request.method == "POST":
    #     #clicking add and remove will save this input
    #     data = request.json
    #     print(data)
    #     #print(cache)
    #     cache = data
    #     initial.getCache(cache["filters"])
    #     tables = initial.outputTable()
    #     df = tables
    #     print("teh heckkkkkkk")
    #     print(df)
    #     colNames = ['choose filter', 'ABS_wf_D', 'STAT_CC_D', 'STAT_CC_A',
    #    'STAT_CC_D_An', 'STAT_CC_A_Ca', 'STAT_n', 'STAT_n_D', 'STAT_n_A',
    #    'ABS_f_D', 'CT_f_conn_D', 'CT_f_conn_D_An', 'CT_f_conn_A_Ca',
    #    'DISS_wf10_D', 'DISS_f10_D', 'DISS_f2_D', 'DISS_prob_reach_I', 'STAT_e',
    #    'CT_e_conn', 'CT_f_e_conn', 'CT_e_D_An', 'CT_e_A_Ca', 'CT_n_D_adj_An',
    #    'CT_f_D_tort1', 'CT_wtort_D', 'CT_n_A_adj_Ca', 'CT_f_A_tort1',
    #    'CT_wtort_A', 'int_x', 'int_d', 'int_g', 'int_r', 'NOMALIZED_INTERFACE',
    #    'jsc', 'jsc_d', 'int_r_int_d', 'int_d_int_g', 'jsc_int_d']
    #     print(data)
    #     return render_template("output.html", colNames=json.dumps(colNames))
    if request.method == "GET":
        # upon clicking submit this stuff will render
        colNames = []
        print("from GET!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(df)
        print(request.args)
        data = request.args
        filters = []
        for i in data:
            stringy = i + "," + data[i]
            filters.append(stringy)
        print("from inside ")
        cache = {"filters": filters}
        print(cache)
        initial.getCache(cache["filters"])
        tables = initial.outputTable()
        df = tables
        # cache1 = json.dumps(cache)
        colNames = ['choose filter', 'ABS_wf_D', 'STAT_CC_D', 'STAT_CC_A',
                    'STAT_CC_D_An', 'STAT_CC_A_Ca', 'STAT_n', 'STAT_n_D', 'STAT_n_A',
                    'ABS_f_D', 'CT_f_conn_D', 'CT_f_conn_D_An', 'CT_f_conn_A_Ca',
                    'DISS_wf10_D', 'DISS_f10_D', 'DISS_f2_D', 'DISS_prob_reach_I', 'STAT_e',
                    'CT_e_conn', 'CT_f_e_conn', 'CT_e_D_An', 'CT_e_A_Ca', 'CT_n_D_adj_An',
                    'CT_f_D_tort1', 'CT_wtort_D', 'CT_n_A_adj_Ca', 'CT_f_A_tort1',
                    'CT_wtort_A', 'int_x', 'int_d', 'int_g', 'int_r', 'NOMALIZED_INTERFACE',
                    'jsc', 'jsc_d', 'int_r_int_d', 'int_d_int_g', 'jsc_int_d']
        print(colNames)

        return render_template("output.html", colNames=json.dumps(colNames))
    # return render_template("scatter_plot.html", table=[df.to_html(header="true")], tabledata=tabledata)
    return render_template("output.html")


@app.route("/data.json")
def data():
    jsonfile = initial.returnResponse()
    colNames = ['case_name', 'source', 'ABS_wf_D', 'STAT_CC_D', 'STAT_CC_A',
                'STAT_CC_D_An', 'STAT_CC_A_Ca', 'STAT_n', 'STAT_n_D', 'STAT_n_A',
                'ABS_f_D', 'CT_f_conn_D', 'CT_f_conn_D_An', 'CT_f_conn_A_Ca',
                'DISS_wf10_D', 'DISS_f10_D', 'DISS_f2_D', 'DISS_prob_reach_I', 'STAT_e',
                'CT_e_conn', 'CT_f_e_conn', 'CT_e_D_An', 'CT_e_A_Ca', 'CT_n_D_adj_An',
                'CT_f_D_tort1', 'CT_wtort_D', 'CT_n_A_adj_Ca', 'CT_f_A_tort1',
                'CT_wtort_A', 'int_x', 'int_d', 'int_g', 'int_r', 'NOMALIZED_INTERFACE',
                'jsc', 'jsc_d', 'int_r_int_d', 'int_d_int_g', 'jsc_int_d']
    return render_template("jsondata.html", jsonData=json.dumps(jsonfile), colNames=colNames)


@app.route("/plot")
def plot():
    jsonfile = initial.returnResponse()
    cols = ['case_name', 'source', 'ABS_wf_D', 'STAT_CC_D', 'STAT_CC_A',
            'STAT_CC_D_An', 'STAT_CC_A_Ca', 'STAT_n', 'STAT_n_D', 'STAT_n_A',
            'ABS_f_D', 'CT_f_conn_D', 'CT_f_conn_D_An', 'CT_f_conn_A_Ca',
            'DISS_wf10_D', 'DISS_f10_D', 'DISS_f2_D', 'DISS_prob_reach_I', 'STAT_e',
            'CT_e_conn', 'CT_f_e_conn', 'CT_e_D_An', 'CT_e_A_Ca', 'CT_n_D_adj_An',
            'CT_f_D_tort1', 'CT_wtort_D', 'CT_n_A_adj_Ca', 'CT_f_A_tort1',
            'CT_wtort_A', 'int_x', 'int_d', 'int_g', 'int_r', 'NORMALIZED_INTERFACE',
            'jsc', 'jsc_d', 'int_r_int_d', 'int_d_int_g', 'jsc_int_d']

    return render_template("scatter_plot.html", jsonData=jsonfile, colNames=cols)
    # table.makeTable.getCache([])
    # tables= table.makeTable.outputTable()
    #             # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # tabledata = json.dumps(table.makeTable.getBoolData())
    # print(tabledata)
    # cols = tables.columns.tolist()
    # colNames = json.dumps(cols)
    # cache1 = json.dumps('no filters entered yet')
    # return render_template("output.html", table=[tables.to_html(header="true")], tabledata=tabledata, colNames=colNames, cache=cache1)


@app.route("/table", methods=["GET"])
def table():
    global cache
    global df
    tabledata = {}
    # if request.method=="POST":
    #     data = request.json
    #     cache = data
    #     print("DID A NEW ONE COME THROUGH OR NAH?????????????????????")
    #     print(data)
    #     print("~~~~~~~~~~~~~~~~~~~~GOT POST~~~~~~~~~~~~~~~~~~~~~~~``")
    #     print(cache["filters"])
    #     initial.getCache(cache["filters"])
    #     tables = initial.outputTable()
    #     df = tables
    #     insideTable = tables
    #     print(df)
    #     tabledata = json.dumps(initial.getBoolData())
    #     return render_template("index.html", table=[df.to_html(header="true")], tabledata=tabledata)
    if request.method == "GET":
        # have filters in the URL that GET can access
        # request.args.GET
        print("~~~~~~~~~~~~~~~GOT GET~~~~~~~~~~~~~~~~~~~~~")
        # print(request.args)
        # data = request.args
        # filters = []
        # for i in data:
        #     stringy = i + "," + data[i]
        #     filters.append(stringy)
        print("from inside ")
        print(cache["filters"])
        initial.getCache(cache["filters"])
        tables = initial.outputTable()
        df = tables
        print(f"tables {df}")
        tabledata = json.dumps(initial.getBoolData())
        print(tabledata)
        # return render_template("scatter_plot.html", table=[df.to_html(header="true")], tabledata=tabledata)
        return render_template("index.html", table=[df.to_html(header="true")], tabledata=tabledata)
    return render_template("index.html", table=[df.to_html(header="true")], tabledata=tabledata)
    # serve this as iframe???


@app.route("/export", methods=["GET"])  # this is a job for GET, not POST
def export():
    print("export clicekd???")
    df.to_csv("output/datafile.csv")
    return send_file('output/datafile.csv',
                     mimetype='text/csv',
                     attachment_filename='datafile.csv',
                     as_attachment=True)


plot = dash.Dash(__name__, server=app, url_base_pathname='/dash/', external_stylesheets=external_stylesheets)

colNames = ['ABS_wf_D', 'STAT_CC_D', 'STAT_CC_A',
            'STAT_CC_D_An', 'STAT_CC_A_Ca', 'STAT_n', 'STAT_n_D', 'STAT_n_A',
            'ABS_f_D', 'CT_f_conn_D', 'CT_f_conn_D_An', 'CT_f_conn_A_Ca',
            'DISS_wf10_D', 'DISS_f10_D', 'DISS_f2_D', 'DISS_prob_reach_I', 'STAT_e',
            'CT_e_conn', 'CT_f_e_conn', 'CT_e_D_An', 'CT_e_A_Ca', 'CT_n_D_adj_An',
            'CT_f_D_tort1', 'CT_wtort_D', 'CT_n_A_adj_Ca', 'CT_f_A_tort1',
            'CT_wtort_A', 'int_x', 'int_d', 'int_g', 'int_r', 'NOMALIZED_INTERFACE',
            'jsc', 'jsc_d', 'int_r_int_d', 'int_d_int_g', 'jsc_int_d']
plot.layout = html.Div([
    # dcc.Interval(id='dash-table', interval=10000),
    html.Div([
        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in colNames],
                value='int_r'
            ),
            dcc.RadioItems(
                id='xaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ], style={'width': '48%', 'display': 'inline-block'}),

        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in colNames],
                value='STAT_n_A'
            ),
            dcc.RadioItems(
                id='yaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ], style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
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
    print(dff.columns)
    print(f"x: {xaxis_column_name}, y: {yaxis_column_name}")
    return {
        'data': [dict(
            x=dff[xaxis_column_name],
            y=dff[yaxis_column_name],
            text=dff['STAT_n_A'],
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
                # 'type': 'linear'
                'type': 'linear' if xaxis_type == 'Linear' else 'log'
            },
            yaxis={
                'title': yaxis_column_name,
                # 'type': 'linear'
                'type': 'linear' if yaxis_type == 'Linear' else 'log'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }


if __name__ == "__main__":
    # app.run(host="localhost", port=3050, debug=True)
    plot.run_server(host="localhost", port=3050, threaded=True, debug=True)
    # plot.run_server(host="localhost", port=2000, debug=True)
