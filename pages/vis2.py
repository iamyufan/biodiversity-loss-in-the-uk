import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
from pages import common

df = pd.read_csv('data/data2.csv')

# Create subplots
fig = make_subplots(rows=2, cols=2, shared_yaxes=True,
                    vertical_spacing=0.12, horizontal_spacing=0.12)

# Add traces for each taxonomic group
fig.add_trace(go.Scatter(x=df['Year'], y=df['Mammals'],
              name='Mammals', line=dict(color='blue')), row=1, col=1)
fig.add_trace(go.Scatter(x=df['Year'], y=df['Butterflies'],
              name='Butterflies', line=dict(color='green')), row=1, col=2)
fig.add_trace(go.Scatter(x=df['Year'], y=df['Birds'],
              name='Birds', line=dict(color='red')), row=2, col=1)
fig.add_trace(go.Scatter(x=df['Year'], y=df['Moths'],
              name='Moths', line=dict(color='orange')), row=2, col=2)

# Add upper and lower bounds
fig.add_trace(go.Scatter(x=df['Year'], y=df['Mammals_Maximum'], name='Upper Bound', line=dict(
    width=0), marker=dict(color="#444"), showlegend=False), row=1, col=1)
fig.add_trace(go.Scatter(x=df['Year'], y=df['Mammals_Minimum'], name='Lower Bound', fill='tonexty',
              fillcolor='rgba(68, 68, 68, 0.3)', line=dict(width=0), marker=dict(color="#444"), showlegend=False), row=1, col=1)
fig.add_trace(go.Scatter(x=df['Year'], y=df['Butterflies_Maximum'], name='Upper Bound', line=dict(
    width=0), marker=dict(color="#444"), showlegend=False), row=1, col=2)
fig.add_trace(go.Scatter(x=df['Year'], y=df['Butterflies_Minimum'], name='Lower Bound', fill='tonexty',
              fillcolor='rgba(68, 68, 68, 0.3)', line=dict(width=0), marker=dict(color="#444"), showlegend=False), row=1, col=2)
fig.add_trace(go.Scatter(x=df['Year'], y=df['Birds_Maximum'], name='Upper Bound', line=dict(
    width=0), marker=dict(color="#444"), showlegend=False), row=2, col=1)
fig.add_trace(go.Scatter(x=df['Year'], y=df['Birds_Minimum'], name='Lower Bound', fill='tonexty',
              fillcolor='rgba(68, 68, 68, 0.3)', line=dict(width=0), marker=dict(color="#444"), showlegend=False), row=2, col=1)
fig.add_trace(go.Scatter(x=df['Year'], y=df['Moths_Maximum'], name='Upper Bound', line=dict(
    width=0), marker=dict(color="#444"), showlegend=False), row=2, col=2)
fig.add_trace(go.Scatter(x=df['Year'], y=df['Moths_Minimum'], name='Lower Bound', fill='tonexty',
              fillcolor='rgba(68, 68, 68, 0.3)', line=dict(width=0), marker=dict(color="#444"), showlegend=False), row=2, col=2)

fig.update_layout(
    title='Relative abundance of different taxonomic groups in the UK (1970 to 2019)',
    yaxis=dict(title='Index (1993=100)'),
    hovermode="x",
    plot_bgcolor='white',  # Set the background color of the plot area
    paper_bgcolor='white',  # Set the background color of the entire figure
    yaxis1=dict(title='Index (1995=100)', gridcolor='lightgray'),
    # yaxis2=dict(title='Index (1976=100)', gridcolor='lightgray'),
    yaxis3=dict(title='Index (1970=100)', gridcolor='lightgray'),
    # yaxis4=dict(title='Index (1970=100)', gridcolor='lightgray'),

    xaxis1=dict(title='Mammals', gridcolor='lightgray'),
    xaxis2=dict(title='Butterflies', gridcolor='lightgray'),
    xaxis3=dict(title='Birds', gridcolor='lightgray'),
    xaxis4=dict(title='Moths', gridcolor='lightgray'),
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
                                      '2. Relative abundance of different taxonomic groups'),
                                    html.P(
                                        '- The line graphs show the smoothed trend (solid line) with its 95% credible interval (shaded area).'
                                    ),
                                  html.P(
                                      '- The priority species do however include a range of taxonomic groups and will respond to the range of environmental pressures that biodiversity policy aims to address.'),
                                  html.P(
                                      '- The moths have undergone the biggest decline with an index value in the final year (2017, as most moth time-series end in 2017) that was only 14% of its value in 1970. Butterflies have also experienced a strong decline, with an index value in 2019 that was 34% of its value in 1976.'
                                  ),
                                  html.P(
                                    '- These are counterbalanced by relative stability in the birds index (100% in 2019 relative to the base year of 1970) and the mammal index, which had a value of 87% in 2019 (relative to a base year of 1995).'
                                  ),
                                  html.Div(style={'margin-top': '20px'}),
                                  html.Div(
                                      children=[
                                          html.Div(className='bottom-nav',
                                                   children=[
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                             '<', id='button-prev', n_clicks=0)
                                                       ], href=common.base_url+'/vis1', style={'margin-right': '2rem'}),
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                              '>', id='button-next', n_clicks=0),
                                                       ], href=common.base_url+'/vis3'),
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
