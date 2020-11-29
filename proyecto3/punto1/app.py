import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

df = pd.read_json('https://www.datos.gov.co/resource/2x55-9wxm.json')

available_indicators = ['percentil_global', 'punt_global', 'mod_razona_cuantitat_punt']

app.layout = html.Div([
    html.Div(children=[
    html.H1(children='¡Hola! Proyecto 3 por Samuel Pérez'),

    html.Div(children='''
        Usando la base de datos proporcionada por el ICFES en la plataforma gubernamental Datos Abiertos, proporcionamos visualización tipo box plot de la variable que usted escoja según el nivel socioeconómico del estudiante. A continuación, elija una variable para el eje y:
    ''')]),

    html.Div([

        html.Div([
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='percentil_global'
            )
        ],
        style={'width': '48%', 'display': 'inline-block'})
    ]),

    dcc.Graph(id='indicator-graphic')
])

@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('yaxis-column', 'value')])

def update_graph(yaxis_column_name):

    if yaxis_column_name == None:
        yaxis_column_name = 'percentil_global'

    fig = px.box(df, x="estu_nse_individual",
                     y=yaxis_column_name,
                     labels={
                     "estu_nse_individual": "Nivel socioeconómico del estudiante (estu_nse_individual)"
                    })

    fig.update_layout(title= yaxis_column_name+" según el nivel socioeconómico del estudiante (estu_nse_individual)", hovermode='closest')

    fig.update_yaxes(title=yaxis_column_name) 

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
