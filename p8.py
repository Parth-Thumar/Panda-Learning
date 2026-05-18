import numpy as np
import pandas as pd

data = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Python\\Pandas 1\\bollywood.csv',index_col='movie').squeeze("columns")
print(data)
# start with a to z
print(data.sort_index(inplace=True))
print(data)
print(data.sort_index(ascending=False,inplace=True))
# firts start z to a