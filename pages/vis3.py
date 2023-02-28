import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
from pages import common

df = pd.read_csv('data/data3.csv')

# Create subplots
fig = make_subplots(rows=2, cols=2, shared_yaxes=True, vertical_spacing=0.12, horizontal_spacing=0.12)

# Add traces for each taxonomic group
fig.add_trace(go.Scatter(x=df['Year'], y=df['Farmland birds'], name='Farmland birds', line=dict(color='blue')), row=1, col=1)
fig.add_trace(go.Scatter(x=df['Year'], y=df['Woodland birds'], name='Woodland birds', line=dict(color='green')), row=1, col=2)
fig.add_trace(go.Scatter(x=df['Year'], y=df['Water and Wetland birds'], name='Water and Wetland birds', line=dict(color='red')), row=2, col=1)
fig.add_trace(go.Scatter(x=df['Year'], y=df['Seabirds'], name='Seabirds', line=dict(color='orange')), row=2, col=2)

# Add upper and lower bounds
fig.add_trace(go.Scatter(x=df['Year'], y=df['Farmland birds Upper'], name='Upper Bound', line=dict(width=0), marker=dict(color="#444"), showlegend=False), row=1, col=1)
fig.add_trace(go.Scatter(x=df['Year'], y=df['Farmland birds Lower'], name='Lower Bound', fill='tonexty', fillcolor='rgba(68, 68, 68, 0.3)', line=dict(width=0), marker=dict(color="#444"), showlegend=False), row=1, col=1)
fig.add_trace(go.Scatter(x=df['Year'], y=df['Woodland birds Upper'], name='Upper Bound', line=dict(width=0), marker=dict(color="#444"), showlegend=False), row=1, col=2)
fig.add_trace(go.Scatter(x=df['Year'], y=df['Woodland birds Lower'], name='Lower Bound', fill='tonexty', fillcolor='rgba(68, 68, 68, 0.3)', line=dict(width=0), marker=dict(color="#444"), showlegend=False), row=1, col=2)
fig.add_trace(go.Scatter(x=df['Year'], y=df['Water and Wetland birds Upper'], name='Upper Bound', line=dict(width=0), marker=dict(color="#444"), showlegend=False), row=2, col=1)
fig.add_trace(go.Scatter(x=df['Year'], y=df['Water and Wetland birds Lower'], name='Lower Bound', fill='tonexty', fillcolor='rgba(68, 68, 68, 0.3)', line=dict(width=0), marker=dict(color="#444"), showlegend=False), row=2, col=1)
fig.add_trace(go.Scatter(x=df['Year'], y=df['Seabirds Upper'], name='Upper Bound', line=dict(width=0), marker=dict(color="#444"), showlegend=False), row=2, col=2)
fig.add_trace(go.Scatter(x=df['Year'], y=df['Seabirds Lower'], name='Lower Bound', fill='tonexty', fillcolor='rgba(68, 68, 68, 0.3)', line=dict(width=0), marker=dict(color="#444"), showlegend=False), row=2, col=2)

fig.update_layout(
    title='Relative abundance of wild birds by habitat in the UK (1970 to 2019)',
    yaxis=dict(title='Index (1993=100)'),
    hovermode="x",
    plot_bgcolor='white',  # Set the background color of the plot area
    paper_bgcolor='white',  # Set the background color of the entire figure
    yaxis1=dict(title='Index (1970=100)', gridcolor='lightgray'),
    # yaxis2=dict(title='Index (1970=100)', gridcolor='lightgray'),
    yaxis3=dict(title='Index (1975=100)', gridcolor='lightgray'),
    # yaxis4=dict(title='Index (1986=100)', gridcolor='lightgray'),
    
    xaxis1=dict(title='Farmland birds', gridcolor='lightgray'),
    xaxis2=dict(title='Woodland birds', gridcolor='lightgray'),
    xaxis3=dict(title='Water and Wetland birds', gridcolor='lightgray'),
    xaxis4=dict(title='Seabirds', gridcolor='lightgray'),
    height=800,
    width=800,
    # Set the subplots to be arranged vertically
    # with a shared x-axis and independent y-axes
    # for each subplot
    grid=dict(rows=4, columns=1, pattern='independent'),
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
                                      '3. Case studies: wild birds'),
                                  html.P(
                                      '- Within the index, 28% of the 130 wild bird species increased, 39% showed little change and 29% declined between 1970 and 2018.'),
                                  html.P(
                                      '- The main patterns and drivers of change are best considered by looking at the indices of species grouped by habitat in the figure.'),
                                  html.Div(style={'margin-top': '20px'}),
                                  html.Div(
                                      children=[
                                          html.Div(className='bottom-nav',
                                                   children=[
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                             '<', id='button-prev', n_clicks=0)
                                                       ], href=common.base_url+'/vis2', style={'margin-right': '2rem'}),
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                              '>', id='button-next', n_clicks=0),
                                                       ], href=common.base_url+'/vis4'),
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
