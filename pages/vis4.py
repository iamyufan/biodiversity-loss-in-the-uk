import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
from pages import common

df = pd.read_csv('data/data4.csv')

fig = go.Figure([
    go.Scatter(x=df['Year'], y=df['All'],
               name='All farmland birds', line=dict(color='blue')),
    go.Scatter(x=df['Year'], y=df['Generalist'],
               name='Generalists', line=dict(color='green')),
    go.Scatter(x=df['Year'], y=df['Specialist'],
               name='Specialists', line=dict(color='red'))
])

fig.update_layout(
    title='Relative abundance of generalist and specialist farmland birds in the UK (1970 to 2019)',
    yaxis=dict(title='Index (1970=100)', gridcolor='lightgray'),
    hovermode="x",
    plot_bgcolor='white',  # Set the background color of the plot area
    paper_bgcolor='white',  # Set the background color of the entire figure
    height=600,
    width=800,
    xaxis=dict(gridcolor='lightgray')   # Set the grid color of the x-axis
)


app = dash.Dash(__name__)

layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                     html.Div(className='four columns div-user-controls figure-description',
                              children=[
                                  html.H1(
                                      'Current Status'),
                                  html.H2(
                                      '4. Species breakdown: farmland bird'),
                                  html.P(
                                      '- The long-term decline of the farmland bird indicator in the UK has been driven mainly by the decline of those species that are restricted to, or highly dependent on, farmland habitats (the ‘specialists’).'),
                                  html.P(
                                      '- The smoothed trend shows a significant decline of 70% for specialists and a non-significant decline of 17% for generalists.'
                                  ),
                                  html.P(
                                      '- Changes in farming practices, such as the loss of mixed farming systems, the move from spring to autumn sowing of cereal crops, and increased pesticide use, have been demonstrated to have had adverse impacts on farmland birds such as skylark and grey partridge'),
                                  html.Div(style={'margin-top': '20px'}),
                                  html.Div(
                                      children=[
                                          html.Div(className='bottom-nav',
                                                   children=[
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                             '<', id='button-prev', n_clicks=0)
                                                       ], href=common.base_url+'/vis3', style={'margin-right': '2rem'}),
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                              '>', id='button-next', n_clicks=0),
                                                       ], href=common.base_url+'/vis5'),
                                                   ]
                                                   )
                                      ]),
                              ]
                              ),
                     html.Div(className='eight columns div-for-charts bg-white figure-right',
                              children=[
                                  dcc.Graph(
                                      id='example-graph',
                                      figure=fig
                                  )
                              ])
                 ])
    ]
)
