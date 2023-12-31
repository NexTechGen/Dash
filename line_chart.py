from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas","Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

# plotly express for line chart
fig = px.line(df, x="Fruit", y="Amount", color="City")


app.layout = html.Div([
    html.H1("Welcome to Ruzait's Dashboard"),
    html.H3('Demo Dash'),
    dcc.Graph(id='ex-graph', figure=fig)
])


if __name__ == '__main__':
    app.run_server(debug=True, port=8600)