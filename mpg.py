#hw
import numpy
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go 
from plotly.subplots import make_subplots 



df = pd.read_csv('MPG.csv')
df = df.dropna(subset = ['horsepower']).copy()
print(df.info())
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        'Horsepower vs MPG',
        'Weight Distribution',
        'Acceleration vs MPG',
        'Overview'
    )
)

fig1 = px.scatter(df, x='horsepower', y='mpg', color='origin', hover_data=['name', 'model_year'])
# print(fig1.data)
# for trace in fig1.data:
#     fig.add_trace(trace, row=1, col=1)

fig1.update_traces()
fig1.update_layout(height=800, width=1000, title_text='Horsepower vs MPG', template='plotly_white')

fig2 = px.histogram(df, x='weight')
# for trace in fig2.data:
#     fig.add_trace(trace, row=1, col=2)
fig2.update_traces()
fig2.update_layout(height=800, width=1000, title_text='Horsepower vs MPG', template='plotly_white')


fig3 = px.scatter(df, x='acceleration', y='mpg', size='horsepower', hover_data=['name', 'model_year'])
# for trace in fig3.data:
#     fig.add_trace(trace, row=2, col=1)
fig3.update_traces()
fig3.update_layout(height=800, width=1000, title_text='Horsepower vs MPG', template='plotly_white')



fig.update_layout(height=800, width=1000, title_text='Automobile Performance Dashboard', template='plotly_white')
fig.show()
