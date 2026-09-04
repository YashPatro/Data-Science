import pandas as pd 
import plotly.graph_objects as go 

timeSeries = pd.read_csv('WHO-COVID-19-global-data (1).csv')

timeSeries.columns = ['DateReported','Country_code','Country','WHO_region','New_cases','Cumulative_cases','New_deaths','Cumulative_deaths']

print(timeSeries.info())
#typecasting is chnaging the type of data 
timeSeries['DateReported'] = pd.to_datetime(timeSeries['DateReported'])
print(timeSeries.info())

timeSeries_dates = timeSeries.groupby('DateReported').sum()
print(timeSeries_dates)

fig = go.Figure()

fig.add_trace(go.Scatter(x = timeSeries_dates.index,y = timeSeries_dates['Cumulative_cases'],fill = 'tonexty',line_color = 'blue'))

fig.update_layout(title = 'Cumulative_cases Worldwide')

fig.write_html('fig.html',auto_open = True)


