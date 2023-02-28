
from dash import Dash, html, dcc, Input, Output, callback
from pages import index, vis1, vis2, vis3, vis4, vis5, vis6, vis7, vis8, common, end
import pandas as pd

app = Dash(__name__, suppress_callback_exceptions=True, url_base_pathname=common.base_url+'/')

app.title = "UK's Biodiversity Loss"

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
])

@callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    pathname = pathname[len(common.base_url):]
    if pathname == '/':
        return index.layout
    elif pathname == '/vis1':
        return vis1.layout
    elif pathname == '/vis2':
        return vis2.layout
    elif pathname == '/vis3':
        return vis3.layout
    elif pathname == '/vis4':
        return vis4.layout
    elif pathname == '/vis5':
        return vis5.layout
    elif pathname == '/vis6':
        return vis6.layout
    elif pathname == '/vis7':
        return vis7.layout
    elif pathname == '/vis8':
        return vis8.layout
    elif pathname == '/end':
        return end.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run(debug=True, port=8050)
