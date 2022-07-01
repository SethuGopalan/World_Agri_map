from matplotlib.pyplot import figtext
from numpy import equal, isin
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
from dash import Dash, html, dcc
import dash
from dash import Input, Output, dash_table, State
import numpy as np
import pandas as pd
import dash_bootstrap_components as dbc


df = pd.read_csv('Production_Crops_E_Americas.csv')
data = df['Area']
year_df = df[['Y1961', 'Y1962', 'Y1963', 'Y1964', 'Y1965', 'Y1966', 'Y1967', 'Y1968', 'Y1969', 'Y1970', 'Y1971', 'Y1972', 'Y1973', 'Y1974', 'Y1975', 'Y1976', 'Y1977', 'Y1978', 'Y1979', 'Y1980', 'Y1981', 'Y1982', 'Y1983', 'Y1984', 'Y1985', 'Y1986', 'Y1987', 'Y1988', 'Y1989',
              'Y1990', 'Y1991', 'Y1992', 'Y1993', 'Y1994', 'Y1995', 'Y1996', 'Y1997', 'Y1998', 'Y1999', 'Y2000', 'Y2001', 'Y2002', 'Y2003', 'Y2004', 'Y2005', 'Y2006', 'Y2007', 'Y2008', 'Y2009', 'Y2010', 'Y2011', 'Y2012', 'Y2013', 'Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2018', 'Y2019']]
year = year_df.set_axis([1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989,
                         1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019], axis='columns')

app = dash.Dash(external_stylesheets=[dbc.themes.SLATE])

app.layout = dbc.Container([

    dbc.Row([

        dbc.Col([html.H1('Americas Agriculture data')

                 ]),
        dbc.Col([
            dcc.Input(id='my_input', type='text', placeholder='Area or Item'),
            html.Button('Submit', id='input_value', n_clicks=0),

        ])

    ]),
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                id='Agri_table',
                columns=[{'id': i, 'name': i}for i in df.columns],
                data=df.to_dict('records'),
                page_size=12,
            )
        ], width={'size': 12, 'offset': 0}),

        dbc.Col([
            dcc.Slider(
                id='year_slider',
                min=year.columns.min(),
                max=year.columns.max(),
                value=year.columns.min(),

                marks={
                    str(year): str(year)
                    for year in year.columns
                }

            )

        ], width={'size': 12, 'offset': 0}),



        html.Br(),
        html.Br(),
        dbc.Col([
            dcc.Dropdown(
                id='Area_select',
                options=[{'label': a, 'value': a}for a in df['Area'].unique()],
                value='Cuba'

            )
        ], width={'size': 2, 'offset': 0}),
        html.Br(),
        html.Br(),
        dbc.Col([
            dcc.Dropdown(
                id='Item_select',
                options=[{'label': n, 'value': n}for n in df['Item'].unique()],
                value='Bananas'
            )
        ], width={'size': 2, 'offset': 0}),
        dbc.Col([
            dash_table.DataTable(
                id='Item_table',
                columns=[{'id': x, 'name': x}for x in df.columns],
                data=df.to_dict('records'),
                page_size=4,
            )
        ], width={'size': 2, 'offset': 2}),
        dbc.Col([
            html.Div(id='input_data')

        ], width={'size': 4, 'offset': 0}),

        dbc.Col([
            dcc.Graph(id='bar_chart')

        ], width={'size': 6, 'offset': 2}),

    ])



], fluid=True)


@ app.callback(
    Output('Agri_table', 'data'),
    Output('bar_chart', 'figure'),
    [Input('input_value', 'n_clicks')],
    [State('my_input', 'value')]

)
def filter_drop(n_clicks, my_value):
    dff = df.loc[df['Area'] == my_value]
    fig = px.bar(dff, x='Item', y='Unit', hover_data=[
        'Y1961', 'Y1962', 'Y1963', 'Y1964', 'Y1965'])
    return dff.to_dict('records'), fig,


@app.callback(
    Output('Item_table', 'data'),
    Output('input_data', 'children'),
    [Input('year_slider', 'value')],
    [Input('Area_select', 'value')],
    [Input('Item_select', 'value')]



)
def d_value_update(slider_value, Area_value, Item_value, ):
    d_value = df.loc[((year == slider_value) & df['Area'] == Area_value)
                     & (df['Item'] == Item_value)]

    return d_value.to_dict('records'), html.Div('The {} production of {} in the yaer{} is{}'.format(
        Area_value, Item_value, slider_value))


if __name__ == "__main__":
    app.run_server(debug=True)
