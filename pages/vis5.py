import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from pages import common

df = pd.read_csv('data/data5.csv')
# convert the hectares column to float
df['hectares'] = df['hectares'].apply(
    lambda x: float(x.strip().replace(',', '')))

# Define nodes and links
nodes = pd.unique(df['1990 habitat']).tolist()
nodes += [node+"_t" for node in nodes]

# Give each node an index in the dataframe
node_indices = {node: i for i, node in enumerate(nodes)}
df['1990 habitat index'] = df['1990 habitat'].apply(lambda x: node_indices[x])
df['2019 habitat index'] = df['2019 habitat'].apply(
    lambda x: node_indices[x+"_t"])

# colors for each node
colors = ['#1f77b4', '#d62728', '#ff7f0e',
          '#2ca02c', '#e377c2', '#7f7f7f', '#17becf'] * 2

# Define links
link_source = df['1990 habitat index'].tolist()
link_target = df['2019 habitat index'].tolist()
link_value = df['hectares'].tolist()
link_color = df['1990 habitat'].apply(
    lambda x: colors[node_indices[x]]).tolist()

# Colors for each link (the lighter color as the corresponding source node)
link_color = [colors[i] for i in link_source]
# make it lighter
link_color = [
    f'rgba{str(tuple([int(c[1:3], 16), int(c[3:5], 16), int(c[5:7], 16), 0.3]))}' for c in link_color]

# Create Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=pd.unique(df['1990 habitat']).tolist() +
        pd.unique(df['1990 habitat']).tolist(),
        color=colors
    ),
    link=dict(
        source=link_source,
        target=link_target,
        value=link_value,
        color=link_color
    ))])

fig.update_layout(
    title='The change in land use in the UK between 1990 and 2019',
    hovermode="x",
    plot_bgcolor='white',  # Set the background color of the plot area
    paper_bgcolor='white',  # Set the background color of the entire figure
    height=800,
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
                                      '1. Habitat Loss'),
                                  html.P(
                                      '- The Sankey diagram shows the change in land use in the UK between 1990 and 2019. The width of the links represents the area of land that has changed from one habitat type to another.'),
                                  html.P(
                                      '- Enclosed farmland covered 13,426,415 hectares of land area in the UK in 1990; by 2019 this area had decreased by around 5% to 12,694,693 hectares. Over the same period, urban areas increased from 1,418,964 hectares by around 30% to 1,843,901 hectares. Woodland habitats grew by 29%, from 2,540,272 hectares in 1990 to 3,268,707 hectares in 2019.'
                                  ),
                                  html.Div(style={'margin-top': '20px'}),
                                  html.Div(
                                      children=[
                                          html.Div(className='bottom-nav',
                                                   children=[
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                             '<', id='button-prev', n_clicks=0)
                                                       ], href=common.base_url+'/vis4', style={'margin-right': '2rem'}),
                                                       html.A(id='', className='', children=[
                                                           html.Button(
                                                              '>', id='button-next', n_clicks=0),
                                                       ], href=common.base_url+'/vis6'),
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
