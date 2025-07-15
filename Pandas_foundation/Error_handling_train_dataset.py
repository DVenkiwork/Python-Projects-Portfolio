# Objective: To check on Error Handline functionality in Pandas using train dataset

import pandas as pd 

df = pd.read_csv('Train.csv')

print("Initial Dataset:")
print(df.info())

print("\n Initial Header Data:")
print(df.head())

print("\n\nMissing values in Dataset before cleanup:")
print(df.isnull)