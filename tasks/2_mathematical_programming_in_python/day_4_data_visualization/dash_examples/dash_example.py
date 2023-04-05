import dash
import dash_html_components as html

app = dash.Dash(__name__)


app.layout = html.Div(
    children=[
        html.H1(children="Simple dashboard"),
        html.P(children="Content of the page"),
    ]
)

if __name__ == "__main__":
    app.run_server(port=8889, debug=True)
