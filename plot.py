# # -*- coding: utf-8 -*-
#
# # Run this app with `python app.py` and
# # visit http://127.0.0.1:8050/ in your web browser.
#
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

#
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#
# server = flask.Flask(__name__)
# plot = dash.Dash(__name__, server=server, url_base_pathname='/get/', external_stylesheets=external_stylesheets)
# cache = {}
# #
# # url = 'http://localhost:5000/vizier-db/api/v1/projects/bd52b624/datasets/6d1950e574d04349adeb60f41ec21d50/csv'
# # resp = requests.get(url)
# #
# # with open('data1.csv','w') as f:
# #     writer = csv.writer(f)
# #     for line in resp.iter_lines():
# #         writer.writerow(line.decode('utf-8').split(','))
#
# @server.route('/get', methods=['POST', 'GET'])
# def get():
#     if request.method == 'POST':
#         #clicking add and remove will save this input
#         data = request.json
#         global cache
#         cache = data
#         print("from post!")
#         print(cache)
#         return json.dumps(cache)
#     if request.method == 'GET':
#         #clicking add and remove will save this input
#         data = request.json
#         print("from get!")
#         print(data)
#         return plot.index()
#     return plot.index()
#
# def outputDF():
#     json_response = table.makeTable.returnResponse()
#     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
#     cols = []
#     rows = []
#     #col names:
#     counter = -1
#     for col in json_response['schema']:
#         cols.append(col['name'])
#     for row in json_response['data']:
#         counter+=1
#         rows.append(row)
#     dataTable = pd.DataFrame(rows, columns=cols)
#     return dataTable
#     #learn to process variable sql queries
#     #then query the da
#
# df = outputDF()
# print("~~[[[[]]]]~~~~~")
# print(df)
# print("~~~~~~~~")
#
# available_indicators = df
#
#
# plot.layout = html.Div([
#     html.Div([
#
#         html.Div([
#             dcc.Dropdown(
#                 id='xaxis-column',
#                 options=[{'label': i, 'value': i} for i in available_indicators],
#                 value='JSC'
#             ),
#             dcc.RadioItems(
#                 id='xaxis-type',
#                 options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
#                 value='Linear',
#                 labelStyle={'display': 'inline-block'}
#             )
#         ],
#         style={'width': '48%', 'display': 'inline-block'}),
#
#         html.Div([
#             dcc.Dropdown(
#                 id='yaxis-column',
#                 options=[{'label': i, 'value': i} for i in available_indicators],
#                 value='STAT_N_D'
#             ),
#             dcc.RadioItems(
#                 id='yaxis-type',
#                 options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
#                 value='Linear',
#                 labelStyle={'display': 'inline-block'}
#             )
#         ],style={'width': '48%', 'float': 'right', 'display': 'inline-block'})
#     ]),
#
#     dcc.Graph(id='indicator-graphic'),
#
# ])
#
#
# @plot.callback(
#     Output('indicator-graphic', 'figure'),
#     [Input('xaxis-column', 'value'),
#      Input('yaxis-column', 'value'),
#      Input('xaxis-type', 'value'),
#      Input('yaxis-type', 'value')])
# def update_graph(xaxis_column_name, yaxis_column_name,
#                  xaxis_type, yaxis_type):
#     dff = df
#     return {
#         'data': [dict(
#             x=dff[xaxis_column_name],
#             y=dff[yaxis_column_name],
#             text=dff['STAT_N_D'] ,
#             mode='markers',
#             marker={
#                 'size': 15,
#                 'opacity': 0.5,
#                 'line': {'width': 0.5, 'color': 'white'}
#             }
#         )],
#         'layout': dict(
#             xaxis={
#                 'title': xaxis_column_name,
#                 'type': 'linear' if xaxis_type == 'Linear' else 'log'
#             },
#             yaxis={
#                 'title': yaxis_column_name,
#                 'type': 'linear' if yaxis_type == 'Linear' else 'log'
#             },
#             margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
#             hovermode='closest'
#         )
#     }
#
#
# if __name__ == '__main__':
#     server.run(host="localhost", port=8050, debug=True)
