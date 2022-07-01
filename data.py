from numpy import equal, isin
import plotly.express as px
import plotly.graph_objects as go
from plotly.offline import plot
from dash import Dash, html, dcc
import dash
from dash import Input, Output, dash_table
import numpy as np
import pandas as pd
import dash_bootstrap_components as dbc
import names

df = pd.read_csv('Production_Crops_E_Americas.csv')

# df = pd.read_csv('Production_Crops_E_Americas.csv',usecols=['Area','Element','Unit',]).rename(
#     columns={
#         'Area':'Country',
#         'Element':'Areacultivated',
#         'Unit':'Cultivated'
#     }
# ).set_index('Country')

# print (df['Area'])

# print(df['Area'][0])
# print(df[['Item'][0],df['Area'][0]])
# print(df.loc[[df['Area']],df['Item']])

# dff=df[[df['Area'],df['Item'],df['Unit']]]
# print(dff)
# print(df[['Area','Item','Element','Unit','Y1961']])
# print(df.loc['Area[0]','Item','Element'])

year_df = df[['Y1961', 'Y1962', 'Y1963', 'Y1964', 'Y1965', 'Y1966', 'Y1967', 'Y1968', 'Y1969', 'Y1970', 'Y1971', 'Y1972', 'Y1973', 'Y1974', 'Y1975', 'Y1976', 'Y1977', 'Y1978', 'Y1979', 'Y1980', 'Y1981', 'Y1982', 'Y1983', 'Y1984', 'Y1985', 'Y1986', 'Y1987', 'Y1988', 'Y1989',
              'Y1990', 'Y1991', 'Y1992', 'Y1993', 'Y1994', 'Y1995', 'Y1996', 'Y1997', 'Y1998', 'Y1999', 'Y2000', 'Y2001', 'Y2002', 'Y2003', 'Y2004', 'Y2005', 'Y2006', 'Y2007', 'Y2008', 'Y2009', 'Y2010', 'Y2011', 'Y2012', 'Y2013', 'Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2018', 'Y2019']]
year = year_df.set_axis([1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989,
                         1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019], axis='columns')

# year=year_df.set_axis(year_new,axis='columns',inplace=True)
# print(year.all)
name=names.get_full_name()
new_names=[x for x in names.get_full_name() if 'P' in x]

print(new_names)
