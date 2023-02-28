from pydoc import classname
from dash import dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px
from pages import common
from pages.common import nav

links = [
    {'name': 'GNCC Status of UK priority species – Relative abundance',
        'url': 'https://jncc.gov.uk/our-work/ukbi-c4a-species-abundance/'},
    {'name': 'England biodiversity indicators',
        'url': 'https://www.gov.uk/government/statistics/england-biodiversity-indicators'},
    {'name': 'UK Wild Bird Populations Report',
        'url': 'https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1039187/UK_Wild_birds_1970-2020_FINAL.pdf'},
    {'name': 'Biodiversity and wildlife statistics',
        'url': 'https://www.gov.uk/government/collections/biodiversity-and-wildlife-statistics'},
    {'name': 'Habitat extent and condition, natural capital, UK',
        'url': 'https://www.ons.gov.uk/economy/environmentalaccounts/bulletins/habitatextentandconditionnaturalcapitaluk/2022#woodland'},
    {'name': 'Emissions of air pollutants in the UK',
        'url': 'https://www.gov.uk/government/statistics/emissions-of-air-pollutants/emissions-of-air-pollutants-in-the-uk-summary'},
]

# Create a list of hyperlinks
link_list = html.Ul([
    html.Li(
        html.A(link['name'], href=link['url'])
    ) for link in links
])


layout = html.Div(
    children=[
        html.Div(className='row',
                 children=[
                     html.Div(className='ten columns div-user-controls',
                              children=[
                                  html.H1('A Glance into Biodiversity Loss in the UK', style={
                                          "padding-left": "7rem"}),
                                  html.H1('ENVIR 101, 2023 Spring Term, Duke Kunshan University', style={
                                          "padding-left": "7rem", "font-size": "2rem"}),
                                  html.H1('Instructor: Prof. Ding Ma', style={
                                          "padding-left": "7rem", "font-size": "2rem"}),
                                  html.H1('Presented by the UK Team: Yufan Zhang, Aleksandra Stryjska, Yutong Ren, Jinxuan Zhang', style={
                                          "padding-left": "7rem", "font-size": "2rem"}),

                              ]
                              ),
                     html.Div(className='five columns div-user-controls', children=[
                         html.H2('Data Sources & References'),
                         link_list,
                     ]),
                     html.Div(className='five columns div-user-controls', children=[
                         html.H2('Contacts:'),
                         html.A('yufanbruce@outlook.com', href='yufanbruce@outlook.com', style={"padding-left": "1rem", 'font-size': '2rem'}),
                     ]),
                 ]),
        html.Div(className='two columns', children=[
            html.Div(
                children=[
                    html.Div(className='bottom-nav',
                             children=[
                                 html.A(id='', className='', children=[
                                     html.Button(
                                         '<', id='button-prev', n_clicks=0)
                                 ], href=common.base_url+'/vis8', style={'margin-right': '2rem'}),
                                 html.A(id='', className='', children=[
                                     html.Button(
                                         '⇤', id='button-next', n_clicks=0),
                                 ], href=common.base_url+'/'),
                             ]
                             )
                ]
            )
        ]),
        html.Div(id='', className='', children=[
            html.Img(src=common.base_url+'/assets/poster.jpg',
                     className='poster-img'),
        ])
    ]
)
