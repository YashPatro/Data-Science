import pandas as pd 
data = pd.read_csv('titanic.csv')
print(data.info())
#gettong the particular column out of condition
adultnames = data.loc[data['Age'] < 18,'Name']
print(adultnames)
pdata = data.loc[data['Pclass'] == 1,'Name']
print(pdata)

#slicing same as numpy 2d slicing
print(data.iloc[9:25,2:6])
data.iloc[0:3,3] = 'Yash Patro'
print(data)
data.to_csv('newTitanic.csv')
