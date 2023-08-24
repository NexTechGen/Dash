from dash import Dash, html, dcc, Output, Input
import pandas as pd
import plotly.express as px

app = Dash(__name__)


app.layout = html.Div([
    html.H1("Welcome to Ruzait's Dashboard"),

    # Slider
    html.Div([
        dcc.Slider(0, 20, 2, value=10, id="my-slider") # start:0   stop:20   step:5 defauld:10
    ], style={
        'width': '400px'
    }),

    # DropDown
    html.Div([
        dcc.Dropdown(["SF", "Montreal"], 'SF', id="my-drop") # options  default
    ], style={
        'width': '400px'
    }),

    dcc.Graph(id='my-graph')
])

@app.callback(
    Output('my-graph', 'figure'),
    Input('my-drop', 'value')
)
def update(val):    # user Change valu in val form /|Input('my-drop', 'value')|\
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    mask = df['City'] == val

    fig = px.bar(df[mask], x='Fruit', y="Amount")

    return fig  # fig is going to /|Output('my-graph', 'figure')|\

if __name__ == '__main__':
    app.run_server(debug=True, port=8600)