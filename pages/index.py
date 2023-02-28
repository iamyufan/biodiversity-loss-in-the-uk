from pydoc import classname
from dash import dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px
from pages import common
from pages.common import nav


layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                     html.Div(className='ten columns div-user-controls',
                              children=[
                                  html.H1('ENVIR 101 Team Project',
                                          className='index-subtitle'),
                                  html.H1('A Glance into Biodiversity Loss in the UK', style={
                                        'background-color': '#7de3e5', 'max-width': '100%'}, className='index-title'),
                                  html.H1('Creative Element Part I: Data Visualization', style={},
                                          className='index-subtitle'),
                              ]
                              ),
                     html.Div(className='four columns div-user-controls index-author-container',
                              children=[
                                  html.P('Authors: ', className='index-author',
                                         style={'margin-bottom': '5px', 'font-weight': 'bold'}),
                                  html.P('Yufan Zhang',
                                         className='index-author'),
                                  html.P('Aleksandra Stryjska',
                                         className='index-author'),
                                  html.P('Yutong Ren',
                                         className='index-author'),
                                  html.P('Jinxuan Zhang',
                                         className='index-author'),
                              ]
                              ),
                     html.Div(className='nine columns div-user-controls', children=[
                         html.P("As part of our course project for ENVIR 101 at Duke Kunshan University, we have created this website that showcases several visualizations on the current state of biodiversity loss in the UK, as well as some potential causes behind it. Biodiversity loss is an increasingly pressing issue that has wide-ranging impacts on ecosystems, economies, and societies worldwide. Through the use of interactive data visualizations, this website aims to raise awareness about the scale and urgency of this issue, and to help viewers better understand the complex interactions between different factors that contribute to biodiversity loss.", className='index-description')
                     ]),
                 ]),
        html.Div(className='two columns', children=[
            nav,
        ]),
        html.Div(id='', className='', children=[
            html.Img(src=common.base_url+'/assets/poster.jpg',
                     className='poster-img'),
        ])
    ]
)
