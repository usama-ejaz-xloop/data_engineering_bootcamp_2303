import dash
import pandas as pd
import plotly.express as px
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__)

df = pd.read_csv("Iris.csv")

column1 = "SepalLengthCm"
column2 = "SepalWidthCm"

app.layout = html.Div(
    children=[
        html.H1(children="Simple dashboard"),
        html.P(children="Content of the page"),
        dcc.Dropdown(
            id="graph_input",
            options=[column1, column2],
            value=[],
        ),
        html.Div(id="graphs"),
    ]
)


# This is a decorator – you can Google what it is.
@app.callback(
    dash.dependencies.Output("graphs", "children"),
    [dash.dependencies.Input("graph_input", "value")],
)
def generate_graph(data_column):
    fig = px.scatter(x=df.index, y=df.loc[:, data_column])
    graphs = dcc.Graph(id="Data graph", figure=fig)
    return graphs


if __name__ == "__main__":
    app.run_server(debug=True)
