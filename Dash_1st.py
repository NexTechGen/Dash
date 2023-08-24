from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Demo Dash')
])


if __name__ == '__main__':
    app.run_server(debug=True, port=8600 )