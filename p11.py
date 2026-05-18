import numpy as np
import pandas as pd

# How to fatch items out of a series using indexing, fancing...
# slicing -> ek sath multiple items fetch karna

data = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Python\\Pandas 1\\kohli_ipl.csv',index_col='match_no').squeeze("columns")
print(data[5:16])

# negative slicing
print(data[-5:])

movie = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Python\\Pandas 1\\bollywood.csv',index_col='movie').squeeze("columns")
print(movie[::2])

# fancy indexing
print(data[[1,2,3,4,5]])

# indexing with labels -> fancy indexing
print(movie['Uri: The Surgical Strike'])