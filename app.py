from dash import Dash, html, dcc
import plotly.graph_objects as go

import pandas as pd


app = Dash(__name__)
# Read data from a csv
z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')

fig = go.Figure(data=[go.Surface(z=z_data.values)])

fig.update_layout(title='Mt Bruno Elevation', autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))

#fig.show()

app.layout = html.Div(children=[
    html.H1(children='Terrain Mapper For Robots', style = {
        'textAlign': 'center',
        'color': '#7FDBFF'
    }),

    html.Div(children='''
        Create different paths
        1. You can see elevation gain through different paths
        2. You can see total distance of different paths
        3. You can change the type of connector between points

    '''),

    dcc.Graph(
        id='Example Terrain Graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)