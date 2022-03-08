"""
Defines instance of dash app
"""


from dash import Dash
import dash_bootstrap_components as dbc


# next item is to add functionality to delete points and also display points on graph that correspond to point on
# 2d plot, also when you hover over points they turn different colors

stylesheet = [dbc.themes.BOOTSTRAP, "./assets/style.css"]
app = Dash(__name__, external_stylesheets=stylesheet)
app.title = "Terrain Mapper"