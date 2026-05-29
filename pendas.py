import pandas as pd

p = pd.Series([10,20,30,40,50,60])

print(p)

data = {
    'names':['yash','george','david'],
    'age':[15,13,12],
    'score':[90,92,81]


    }
df = pd.DataFrame(data)
print(df)
print(df.columns)

print(df.dtypes)
data = pd.read_csv('heart.csv')
print(data.head())
print(data.tail())
print(data.info())
print(data.describe())
print(data[['chol','age']])
