#import necessary libraries 
import pandas as pd 
import numpy as np 

#loading the dataset 
df  = pd.read_csv("indian_employ_data_cleaned_formatting.csv")
print(df.head())
#checking the missing values
print("no of missing values")
print(df.isnull().sum())
print("add")

