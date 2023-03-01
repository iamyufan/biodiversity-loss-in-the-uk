import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from pages import common

df = pd.read_csv('data/data1.csv')

fig = go.Figure([
    go.Scatter(
        name='Index value',
        x=df['Year'],
        y=df['Index value'],
        mode='lines',
        line=dict(color='rgb(31, 119, 180)'),
    ),
    go.Scatter(
        name='Upper Bound',
        x=df['Year'],
        y=df['Maximum'],
        mode='lines',
        marker=dict(color="#444"),
        line=dict(width=0),
        showlegend=False
    ),
    go.Scatter(
        name='Lower Bound',
        x=df['Year'],
        y=df['Minimum'],
        marker=dict(color="#444"),
        line=dict(width=0),
        mode='lines',
        fillcolor='rgba(68, 68, 68, 0.3)',
        fill='tonexty',
        showlegend=False
    )
])

fig.update_layout(
    width=800,
    height=600,
    yaxis_title='Index (1970=100)',
    title='Relative abundance of priority species in the UK (1970 to 2019)',
    hovermode="x",
    plot_bgcolor='white',   # Set the background color of the plot area
    paper_bgcolor='white',  # Set the background color of the entire figure
    yaxis=dict(gridcolor='lightgray'),  # Set the grid color of the y-axis
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
                                      '1. Relative abundance of priority specie'),
                                  html.P(
                                      '- The line graph shows the smoothed trend (solid line) with its 95% credible interval (shaded area).'),
                                  html.P(
                                      '- There are 2,890 species on the official lists of priority species published for each UK country (Natural Environmental and Rural Communities Act 2006 – Section 41 (England), Environment (Wales) Act 2016 section 7, Northern Ireland Priority Species List, Scottish Biodiversity List)'),
                                  html.P(
                                      '- Actions to conserve them are included within the respective countries’ biodiversity or environment strategies.'),
                                  html.P(
                                      '- By 2019, the index of relative abundance of priority species in the UK had declined to 39% of its base-line value in 1970.'),
                                  html.P(
                                      '- Check out our implementation of this diagram in Virtual Reality (VR):'),
                                  html.A('Demo on YouTube', href='https://youtu.be/heh5uxV7a14', style={'font-size': '1.5rem', 'padding-left': '2rem', 'font-weight': '700'}),
                                  html.Div(style={'margin-top': '20px'}),
                                  html.Div(
                                      children=[
                                          html.Div(className='bottom-nav',
                                                   children=[
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                             '<', id='button-prev', n_clicks=0)
                                                       ], href=common.base_url+'/', style={'margin-right': '2rem'}),
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                              '>', id='button-next', n_clicks=0),
                                                       ], href=common.base_url+'/vis2'),
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
