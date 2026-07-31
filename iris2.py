import pandas as pd , numpy as np, matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier 
from sklearn import metrics 

from sklearn.preprocessing import StandardScaler
data = pd.read_csv('iris.csv')
print(data.head())
print()
print(data.info())

# data['species'] = data['species'].replace({'setosa':0,'versicolor':1,'virginica':2})

plt.subplot(221)
plt.scatter(data['sepal_length'],data['species'],s = 10, c = 'green',marker = 'o')

plt.subplot(222)
plt.scatter(data['sepal_width'],data['species'],s = 10, c = 'red',marker = 'd')

plt.subplot(223)
plt.scatter(data['petal_length'],data['species'],s = 10, c = 'blue',marker = '^')
plt.subplot(224)
plt.scatter(data['petal_width'],data['species'],s = 10, c = 'cyan',marker = 'o')

#plt.show()
print(data.info)
Y = data['species']
X = data.drop('species',axis = 1)
Xtrain,Xtest,Ytrain,Ytest = train_test_split(X,Y,test_size = 0.3,random_state=10)
print(Xtrain.shape)
print(Xtrain)
sc = StandardScaler()
# Xtrain = sc.fit_transform(Xtrain)
# Xtest = sc.transform(Xtest)
print(Ytrain)
model = DecisionTreeClassifier(max_depth=5,random_state=1)
model.fit(Xtrain,Ytrain)

prediction = model.predict(Xtest)
acc = metrics.accuracy_score(prediction,Ytest)
print(acc)

#hw

# data = pd.read_csv("iris.csv")

# X = data.drop("species", axis=1)
# Y = data["species"]

# #Scaling the features
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(X)

# print(X_scaled)
# print(Y.head())

#hw
#sol 1
import pandas as pd
import matplotlib.pyplot as plt

#data
data = pd.read_csv("iris.csv")

#2x2 dashboard
plt.figure(figsize=(12,8))

#plot1
plt.subplot(221)

for species in data["species"].unique():
    temp = data[data["species"] == species]

    plt.scatter(
        temp["petal_length"],
        temp["petal_width"],
        label=species
    )

plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.title("Petal Length vs Petal Width")
plt.legend()

#plot2
plt.subplot(222)

for species in data["species"].unique():
    temp = data[data["species"] == species]

    plt.scatter(
        temp["sepal_length"],
        temp["sepal_width"],
        label=species
    )

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Sepal Length vs Sepal Width")
plt.legend()
#plot3
plt.subplot(223)

for species in data["species"].unique():
    temp = data[data["species"] == species]

    plt.hist(
        temp["sepal_width"],
        alpha=0.5,
        label=species
    )

plt.xlabel("Sepal Width")
plt.ylabel("Frequency")
plt.title("Sepal Width Distribution")
plt.legend()


#plot 4
plt.subplot(224)

for species in data["species"].unique():
    temp = data[data["species"] == species]

    plt.hist(
        temp["petal_length"],
        alpha=0.5,
        label=species
    )

plt.xlabel("Petal Length")
plt.ylabel("Frequency")
plt.title("Petal Length Distribution")
plt.legend()

#Co;mmon title
plt.suptitle("Iris Species Visual Analysis Dashboard")


plt.tight_layout()


plt.show()