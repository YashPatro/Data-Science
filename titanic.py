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
# data.iloc[0:3,3] = 'Yash Patro'
print(data)
# data.to_csv('newTitanic.csv')

#18/06/26

#creating a new column 

data['test'] = data['Pclass']*2
dataRenamed = data.rename(
    columns= {
        'Pclass':'PassengerClass',
        'Sibsp':'Siblings'

    } 
)
print(dataRenamed.info())

#performing mathematicall operator on multiple columns
print(data['Age'].mean())
print()
print(data[['Age','Fare']].mean(0))

print()

print(data.agg({
    'Age':['min','max','median'],
    'Fare':['min','max','median']
    

}))

#gourp by data categorically 

print(data[['Sex','Age']].groupby('Sex').mean())

print(data.groupby('Sex')['Age'].mean())

#to get the mean ticket price for each gender and the cabin class combination

print(data.groupby(['Sex','Pclass'])['Fare'].mean())

#counting rows in each category
print(data)
print(data['Name'].value_counts())

print(data.groupby('Pclass')['Pclass'].count())
print(data.groupby('Sex')['Pclass'].count())

print(data.sort_values(by = ['Pclass','Age'],ascending=False))

#hw
 
t = pd.read_csv("newTitanic.csv")

t["NameLowercase"] = t["Name"].str.lower()
t["Surname"] = t["Name"].str.split(",").str.get(0)
t["Sex_short"] = t["Sex"].replace({"male": "M", "female": "F"})

print("Mean Fare by Sex and Pclass")
print(t.groupby(["Sex", "Pclass"])["Fare"].mean())

print("Mean Age by Sex")
print(t.groupby("Sex")["Age"].mean())

print("Median Age by Sex")
print(t.groupby("Sex")["Age"].median())

print("Passengers Age 20 to 40")
print(t[(t["Age"] >= 20) & (t["Age"] <= 40)][["Name", "Fare"]])

print("Fare Greater Than 100")
print(t[t["Fare"] > 100][["PassengerId", "Name", "Pclass"]])

print("Survived and 3rd Class")
print(t[(t["Survived"] == 1) & (t["Pclass"] == 3)]["Name"])

t.loc[0:4, "Name"] = "Test Passenger"

t.loc[10:15, "Fare"] = 999

print("Modified Rows")
print(t.loc[0:15, ["Name", "Fare"]])

t["FarePerPerson"] = t["Fare"] / (t["SibSp"] + 1)

t["AgeGroup"] = "Adult"
t.loc[t["Age"] < 12, "AgeGroup"] = "Child"
t.loc[(t["Age"] >= 12) & (t["Age"] <= 18), "AgeGroup"] = "Teen"

print("Age Group Counts")
print(t["AgeGroup"].value_counts())

print(t[["Name", "FarePerPerson", "AgeGroup"]].head())