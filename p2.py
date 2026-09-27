import numpy as np
import pandas as pd

ipl = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\ipl-matches.csv')
movies = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\movies.csv')

# shape
print(movies.shape)
print(ipl.shape)

# dtype
print(movies.dtypes)

# index
print(movies.index)
print(ipl.index)

# columns
print(movies.columns)
print(ipl.columns)

# values
print(ipl.values)

# head and tail
print(ipl.head(2)) # --> first 5
print(ipl.tail()) # --> last 5

# simple -random data
print(ipl.sample(5))

# info
print(ipl.info())

# describe
print(movies.describe())
print(ipl.describe())

# isnull
print(movies.isnull().sum())

# duplicate
print(movies.duplicated().sum())
