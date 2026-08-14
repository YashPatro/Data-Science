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

data = pd.read_csv('covid_data.csv')
print(data.info())

data = data[['Province_State','Country_Region','Last_Update','Lat','Long_','Confirmed','Recovered','Deaths','Active']]

#Rename 
data.columns = ('State','Country','LastUpdate','Lat','Long','Confirmed','Recovered','Deaths','Active')

#Handle missing states
data['State'].fillna(value = '', inplace=True)

# 1.Top 10 Most Affected 
topAff = pd.DataFrame(data.groupby('Country')['Confirmed'].sum().nlargest(10).sort_values(ascending=False))
fig_confirmed = px.scatter(topAff, x=topAff.index, y='Confirmed', size='Confirmed', size_max=100, color=topAff.index, title='Confirmed Cases: Top 10 Countries')
fig_confirmed.write_html('fig_confirmed.html', auto_open=False)

# 2.Top 10 Countries by Deaths 
topDeaths = pd.DataFrame(data.groupby('Country')['Deaths'].sum().nlargest(10).sort_values(ascending=False))
fig_deaths = px.scatter(topDeaths, x=topDeaths.index, y='Deaths', size='Deaths', size_max=100, color=topDeaths.index, title='Deaths: Top 10 Countries')
fig_deaths.write_html('fig_deaths.html', auto_open=True)

# 3.Top 10 Countries by Recovered Cases
topRecovered = pd.DataFrame(data.groupby('Country')['Recovered'].sum().nlargest(10).sort_values(ascending=False))
fig_recovered = px.scatter(topRecovered, x=topRecovered.index, y='Recovered', size='Recovered', size_max=100, color=topRecovered.index, title='Recovered Cases: Top 10 Countries')
fig_recovered.write_html('fig_recovered.html', auto_open=True)

#analysis 

#usa analysis 

topStateUS = data['Country'] == 'US' 
print(topStateUS)
topStateUS = data[topStateUS].nlargest(5,'Confirmed')
print(topStateUS)

#india
topStateI = data['Country'] == 'India' 
print(topStateI)
topStateI = data[topStateI].nlargest(5,'Confirmed')
print(topStateI)

#brazil
topStateB = data['Country'] == 'Brazil' 
print(topStateB)
topStateB = data[topStateB].nlargest(5,'Confirmed')
print(topStateB)

#russia
topStateR = data['Country'] == 'Russia' 
print(topStateR)
topStateR = data[topStateR].nlargest(5,'Confirmed')
print(topStateR)

#us grapg


fig = go.Figure(data = [
    go.Bar(name = 'Confirmed Cases',x = topStateUS['Confirmed'],y= topStateUS['Confirmed'],orientation = 'h'),
    go.Bar(name = 'Death Cases',x = topStateUS['Deaths'],y= topStateUS['Deaths'],orientation = 'h')

])
fig.update_layout(title = 'Most Affect States in US',height = 600)
fig.write_html('MAUSdata.html',auto_open = True)

fig5 = go.Figure(data = [
    go.Bar(name = 'Confirmed Cases',x = topStateI['State'],y= topStateI['Confirmed'],orientation = 'h'),
    go.Bar(name = 'Death cases in India',x = topStateI['State'],y= topStateI['Deaths'],orientation = 'h'),
    go.Bar(name = 'Recovered cases in India',x = topStateI['State'],y= topStateI['Recovered'],orientation = 'h')

])
fig5.update_layout(title = 'Most Affect States in India',height = 600)
fig5.write_html('MAIdata.html',auto_open = True)
