#import necessary libraries 
import pandas as pd 
import numpy as np 

#loading the dataset 
df  = pd.read_csv("")
print(df.head())
#checking the missing values
print("no of missing values")
print(df.isnull().sum())

