# tab switch body content

from dashboard.index import app
from dashboard.layout.welcome import welcome
from dashboard.layout.interactive import interactive
from dash.dependencies import Input, Output


@app.callback(Output("tabs-example-content", "children"), Input("app-tabs", "value"))
def callback2(tab):
    if tab == "welcome-tab":
        return welcome
    elif tab == "interactive-tab":
        return interactive