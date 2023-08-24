from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

app = Dash(__name__)

data = pd.read_csv(r"iris.csv")
data.columns =['sepal_length', 'sepal_width', 'petal_length','petal_width', 'species']
lis = list(data.columns)
lis.remove("species")

app.layout = html.Div([
    html.H1("Welcome to Rusaid's Dashboard"),

    dbc.Row([
        dbc.Col([
            html.Div([
                dcc.Dropdown(lis, lis[0], id='mydrop')
            ], style={
                'width':'400px'
            })
        ]),
        dbc.Col([
            html.Div([
                dcc.Dropdown(lis, lis[1], id='mydrop1')
            ], style={
                'width':'400px',
                'margin-left':'300px'
            })
        ])
    ],style={
        'display':'flex'
    }),

    dcc.Graph(id='my-graph')
])

@app.callback(Output('my-graph', 'figure'),
              [
                Input('mydrop', 'value'),    # val1
                Input('mydrop1', 'value')    # val2
              ]
)
def update(val1, val2):
    df = pd.read_csv(r"iris.csv")
    df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

    fig = px.scatter(df, x=val1, y=val2, color="species")

    return fig

if __name__ == '__main__':
    app.run_server(debug=True, port=8600)