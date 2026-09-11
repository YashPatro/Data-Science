import pandas as pd
import numpy as np


salary_data = pd.read_csv('adults.csv')

print(salary_data.head())
print(salary_data.info())
salary_data.columns = ['Age','Class','Sum_Weight','Education','Edu_Num','Marital_status','Occupation','Relationship','Race','Gender','Capital_gain','Capital_loss','Hrs/week','Native_country','Income']
# salary_data['Country']
# salary_data.rename(columns = ())
# print(salary_data.isnull().sum())
print(salary_data.isin(['?']).sum())
salary_data['Native_country'] = salary_data['Native_country'].replace('?',np.nan)
salary_data['Class'] = salary_data['Class'].replace('?',np.nan)
salary_data['Occupation'] = salary_data['Occupation'].replace('?',np.nan)
salary_data.dropna(how = 'any',inplace = True)
#drop the unused collumn 
salary_data.drop(['Sum_Weight','Edu_Num','Marital_status','Capital_gain','Capital_loss','Native_country','Hrs/week'],axis = 1,inplace = True)

for i in salary_data.columns:
        print('---%s---'% i)
        print(salary_data[i].value_counts())



