import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
from pages import common

df = pd.read_csv('data/data8.csv')

x_values = df['Year'].tolist()

fig = go.Figure(data=[
    go.Bar(name='Percentage unknown', x=x_values, y=df['Percentage unknown'].tolist(), marker_color='#d62728'),
    go.Bar(name='Percentage above FMSY', x=x_values, y=df['Percentage above FMSY'].tolist(), marker_color='#ff7f0e'),
    go.Bar(name='Percentage in FMSY range', x=x_values, y=df['Percentage in FMSY range'].tolist(), marker_color='#1f77b4'),
    go.Bar(name='Percentage less than or equal to FMSY', x=x_values, y=df['Percentage less than or equal to FMSY'].tolist(), marker_color='#2ca02c'),
])

fig.update_layout(
    barmode='stack',
    title='Percentage of fish stocks in different categories',
    yaxis=dict(title='Percentage', gridcolor='lightgray'),
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
                                      '4. Overexploitation'),
                                  html.P(
                                      '- The figures shows the change of the percentage pressure of marine fish stocks of UK interest exploited with respect to FMSY (fishing maximum sustainable yield)'),
                                  html.P(
                                      '- Among the 57 marine stocks fished in an acceptable mortality range, stocks exploited at or below the maximum sustainable yield (FMSY), increased from 9% in 1990 to 51% in 2019 (Figure 20).'
                                  ),
                                  html.Div(style={'margin-top': '20px'}),
                                  html.Div(
                                      children=[
                                          html.Div(className='bottom-nav',
                                                   children=[
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                             '<', id='button-prev', n_clicks=0)
                                                       ], href=common.base_url+'/vis7', style={'margin-right': '2rem'}),
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                              '>', id='button-next', n_clicks=0),
                                                       ], href=common.base_url+'/end'),
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
