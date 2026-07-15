#import necessary libraries 
import pandas as pd 
import numpy as np 

#loading the dataset 
df  = pd.read_csv("dirty_employee_dataset_1200.csv")
print(df.head())
#checking the missing values
print("no of missing values")
print(df.isnull().sum())
print("add")

