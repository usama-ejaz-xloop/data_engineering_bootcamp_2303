import dash
import numpy as np
import plotly.express as px
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__)

x_array = np.linspace(0, 10)
y_array = x_array**2


def generate_graph():
    fig = px.line(x=x_array, y=y_array)
    graphs = dcc.Graph(id="Data graph", figure=fig)
    return graphs


app.layout = html.Div(
    children=[
        html.H1(children="Simple dashboard"),
        html.P(children="Content of the page"),
        html.Div(children=generate_graph()),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
