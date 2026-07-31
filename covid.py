import numpy as np, matplotlib.pyplot as plt 
import pandas as pd


import plotly 
import plotly.express as px
import plotly.graph_objects as go 
from plotly.subplots import make_subplots 


data = pd.read_csv('covid_data.csv')
print(data.info())

data = data[['Province_State','Country_Region','Last_Update','Lat','Long_','Confirmed','Recovered','Deaths','Active']]

print(data)

data.columns = ('State','Country','LastUpdate','Lat','Long','Confirmed','Recovered','Deaths','Active')

print(data)
data['State'].fillna(value = '',inplace=True)

#top 10 most affected countries

topAff = pd.DataFrame(data.groupby('Country')['Confirmed'].sum().nlargest(10).sort_values(ascending=False))
fig = px.scatter(topAff,x=topAff.index,y = 'Confirmed',size='Confirmed',size_max=100,color = topAff.index,title = 'Confirmed Cases: Top 10 Countries')

fig.write_html('fig.html',auto_open = True)
