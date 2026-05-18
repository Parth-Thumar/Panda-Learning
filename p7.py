import numpy as np
import pandas as pd

data = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Python\\Pandas 1\\bollywood.csv',index_col='movie').squeeze("columns")

# bollywood kisne kitni movie crate ki wo gwnerate karke dega
# value_counts()

print(data.value_counts())

# sort_values --> inplace

a = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Python\\Pandas 1\\kohli_ipl.csv',index_col='match_no').squeeze("columns")
print(a.sort_values())  # ascending order
print(a.sort_values(ascending=False)) # descending order
print(a.sort_values(ascending=False).head(1).values[0])
# print(a.sort_values(inplace=True))