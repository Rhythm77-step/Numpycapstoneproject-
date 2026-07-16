#import necessary libraries 
import pandas as pd 
import numpy as np 

#loading the dataset 
df  = pd.read_csv("")
print(df.head())
#checking the missing values
print("no of missing values")
print(df.isnull().sum())

df["Salary"].fillna(df["Salary"].mean(),inplace = True)
df["Performance Rating"].fillna(df["Performance Rating"].median(),inplace = True)

df.replace([np.inf,-np.inf],np.nan),inplace = True)
df.fillna(df.mean(),inplace = True)
#remove duplicate records 
df.drop_duplicates(inplace = True)
#remove negative salaries
df["Salary"] = np.where(df["Salary"]<0,df["Salary"].mean(),df["Salary"])
Salary_mean = df["Salary"].mean()
Salary_std = df["Salary"].std()
lower_bound = (Salary_mean - Salary_std*3)
upper_bound = (Salary_mean + Salary_std*3)
#removing salaries which are too high or too low
df = df[df["Salary"] <= lower_bound & df["Salary"]>=upper_bound]
#saving the cleaned dataset 
df.to_csv("cleaned dataset.csv",index = False)
print("Data cleaning completed!,successfully saved your file")









