"""
Actual contents of app
"""
from dashboard.index import app
from dashboard.layout.callbacks import callback1
from dash import dcc
from dash import html

header = html.Header(
    children = [
        html.H1("Welcome to Terrain Mapper")
    ]
)

tabs = dcc.Tabs(
    id = "app-tabs",
    value = "welcome",
    children = [
        dcc.Tab(label="Home", value = "welcome-tab"),
        dcc.Tab(label = "Interactive Page", value = "interactive-tab")
    ]
)

body_content = html.Div(
    id = "tabs-example-content",
    className = "main-panel"
)

app.layout = html.Div(
    children = [
        header,
        tabs,
        body_content
    ]
)
    