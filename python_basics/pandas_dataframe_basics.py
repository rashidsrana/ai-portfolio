
# # Dataframes in Pandas


# - A dataframe in pandas is a 2D structure like table with rows and columns.
# - It is very popular in Data Science for analyzing Datasets.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'name':['alex','brianna'], 'city':['Caledon','Milton'], 'age':[78,45]}
print(data)

df = pd.DataFrame(data)
print(df)

print(df['name'])
print(df[['name','city']])

print(df.loc[:, "age"])
print(df.iloc[:, 0])
print(df.loc[:, ["name","age"]])

# Add salary column
df['salary'] = [50000, 55000]
print(df)

# Add new row (index 2)
df.loc[2] = ['Nic', 'Toronto', 66, 56000]
print(df)

# Update a single cell (row 0, column 'age')
df.at[0, "age"] = 80
print(df)

# SAFE row drop (ignore missing rows)
df = df.drop([0, 3], errors='ignore')
print(df)

# Show shape
print(df.shape)

# Statistics
print(df['age'].mean())
print(df['age'].median())
print(df['age'].sum())
