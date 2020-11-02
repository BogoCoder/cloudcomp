import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd

df = pd.read_json('https://www.datos.gov.co/resource/2x55-9wxm.json')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

fig = px.box(df, x="estu_nse_individual", y="percentil_global", labels={
                     "estu_nse_individual": "Nivel socioeconómico del estudiante (estu_nse_individual)",
                     "percentil_global": "Percentil global (percentil_global)",
                 }, title="Percentil global según el nivel socioeconómico del estudiante")

app.layout = html.Div(children=[
    html.H1(children='¡Hola! Proyecto 2 por Samuel Pérez'),

    html.Div(children='''
        Usando la base de datos proporcionada por el ICFES en la plataforma gubernamental Datos Abiertos, proporcionamos una visualización tipo box plots del percentil global según el nivel socioeconómico del estudiante.
    '''),

    dcc.Graph(
        id='graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
