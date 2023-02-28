import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
from pages import common

df = pd.read_csv('data/data6.csv')

fig = go.Figure([
    go.Scatter(x=df['year'], y=df['nh3'], name='Ammonia', line=dict(color='#1f77b4')),
    go.Scatter(x=df['year'], y=df['nox'], name='Nitrogen Oxides', line=dict(color='#d62728')),
    go.Scatter(x=df['year'], y=df['voc'], name='NMVOCs', line=dict(color='#ff7f0e')),
    go.Scatter(x=df['year'], y=df['pm10'], name='PM10', line=dict(color='#2ca02c')),
    go.Scatter(x=df['year'], y=df['pm25'], name='PM2.5', line=dict(color='#e377c2')),
    go.Scatter(x=df['year'], y=df['so2'], name='Sulfur Dioxide', line=dict(color='#7f7f7f')),
])

fig.update_layout(
    title='Annual emissions of air pollutants',
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
                                      'Potential Factors'),
                                  html.H2(
                                      '2. Pollution'),
                                  html.P(
                                      '- The index line shows the level of annual emissions if they had remained constant since the beginning of the time series.'),
                                  html.P(
                                      '- For sulphur dioxide and nitrogen oxides, emissions have continued to fall in line with the long-term trend with much of the reduction as a result of the decreasing dependence on coal for energy generation.'),
                                    html.P(
                                        '- Emissions of nitrogen oxides and non-methane volatile organic compounds from road transport also decreased by 51 per cent and 66 per cent respectively between 2011 and 2021. This is largely as a result of tighter emissions standards being introduced for petrol and diesel cars.'),
                                    html.P(
                                        '- For particulate matter, decreases in emissions from many sources have been partially offset by increases in emissions from domestic combustion.'),
                                  html.Div(style={'margin-top': '20px'}),
                                  html.Div(
                                      children=[
                                          html.Div(className='bottom-nav',
                                                   children=[
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                             '<', id='button-prev', n_clicks=0)
                                                       ], href=common.base_url+'/vis5', style={'margin-right': '2rem'}),
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                              '>', id='button-next', n_clicks=0),
                                                       ], href=common.base_url+'/vis7'),
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
