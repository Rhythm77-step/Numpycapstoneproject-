#import necessary libraries 
import pandas as pd 
import numpy as np 

#loading the dataset 
df  = pd.read_csv("indian_employee_data_exact_v2.csv")
print(df.head())
#checking the missing values
print("no of missing values")
print(df.isnull().sum())
print("add")

