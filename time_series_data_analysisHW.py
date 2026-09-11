import pandas as pd 
import plotly.graph_objects as go 

timeSeries = pd.read_csv('WHO-COVID-19-global-data (1).csv')

timeSeries.columns = ['DateReported','Country_code','Country','WHO_region','New_cases','Cumulative_cases','New_deaths','Cumulative_deaths']

timeSeries['DateReported'] = pd.to_datetime(timeSeries['DateReported'])

timeSeries_dates = timeSeries.groupby('DateReported').sum(numeric_only=True)

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=timeSeries_dates.index, 
    y=timeSeries_dates['Cumulative_cases'], 
    mode='lines', 
    name='Cumulative Cases', 
    line=dict(color='blue')
))

fig.add_trace(go.Scatter(
    x=timeSeries_dates.index, 
    y=timeSeries_dates['Cumulative_deaths'], 
    mode='lines', 
    name='Cumulative Deaths', 
    line=dict(color='red')
))

fig.add_trace(go.Scatter(
    x=timeSeries_dates.index, 
    y=timeSeries_dates['New_cases'], 
    mode='lines', 
    name='Daily New Cases', 
    line=dict(color='orange')
))

fig.add_trace(go.Scatter(
    x=timeSeries_dates.index, 
    y=timeSeries_dates['New_deaths'], 
    mode='lines', 
    name='Daily New Deaths', 
    line=dict(color='purple')
))

fig.update_layout(
    title='Worldwide COVID-19 Time-Series Analysis', 
    xaxis_title='Date', 
    yaxis_title='Count',
    template='plotly_white'
)

fig.write_html('covid_timeseries_dashboard.html', auto_open=True)