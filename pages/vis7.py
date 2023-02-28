import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
from pages import common

df = pd.read_csv('data/data7.csv')

fig = go.Figure([
    go.Scatter(x=df['Interval'], y=df['Level 4'],
               name='Level 4', line=dict(color='#1f77b4')),
    go.Scatter(x=df['Interval'], y=df['Level 3']+df['Level 4'],
               name='Level 3', line=dict(color='#d62728')),
    go.Scatter(x=df['Interval'], y=df['Level 2']+df['Level 3']+df['Level 4'],
               name='Level 2', line=dict(color='#ff7f0e')),
    go.Scatter(x=df['Interval'], y=df['Level 1']+df['Level 2']+df['Level 3']+df['Level 4'],
               name='Level 1', line=dict(color='#e377c2')),
])

fig.update_layout(
    title='Number of non-native species in marine areas at Great Britain (1960 to 1969 and 2010 to 2019)',
    yaxis=dict(title='# of species', gridcolor='lightgray'),
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
                                      'Potential Factors'),
                                  html.H2(
                                      '3. Invasive Species'),
                                  html.P(
                                      '- The figure shows the number of non-native species in freshwater established in or along 10% of land area'),
                                  html.P(
                                      '- Level 1 – not/scarcely established, Level 2 – established but still generally absent or most occasional, Level 3 – established and frequent in part of the territory and Level 4 –widespread.'
                                  ),
                                  html.Div(style={'margin-top': '20px'}),
                                  html.Div(
                                      children=[
                                          html.Div(className='bottom-nav',
                                                   children=[
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                             '<', id='button-prev', n_clicks=0)
                                                       ], href=common.base_url+'/vis6', style={'margin-right': '2rem'}),
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                              '>', id='button-next', n_clicks=0),
                                                       ], href=common.base_url+'/vis8'),
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
