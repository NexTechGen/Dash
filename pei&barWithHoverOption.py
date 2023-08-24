from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash.exceptions import PreventUpdate
import json

app = Dash(__name__)

data = px.data.tips()
#print(data.columns) # Index(['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size'], dtype='object')

fig = px.pie(data, values='tip', names='day')

app.layout = html.Div([

    html.Div([

        html.Div([
                    dcc.Graph(id='pie', figure=fig)
        ], className='six columns', style={'width': '40%'}),


        html.Div([
                    dcc.Graph(id='bar')
        ], className='six columns', style={'width': '70%'})

    ], className='row', style={'display': 'flex', 'width': '100%', 'height': '100vh'})
])

@app.callback(
    Output('bar', 'figure'),
    Input('pie', 'hoverData')
)
def update(val):

    data = px.data.tips()

    if val is not None:
        day = val['points'][0]['label']
        mask = data['day'] == day

        new_data = data[mask]
        fig1 = px.bar(new_data, x='sex', y='size', color='smoker')

        return fig1

    else:
        raise PreventUpdate



if __name__ == '__main__':
    app.run_server(debug=True, port=8600)