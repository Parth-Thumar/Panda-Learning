import numpy as np
import pandas as pd

# Series usind read_csv

# subscriber

# print(pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Python\\Pandas 1\\subs.csv'))
# print(type(pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Python\\Pandas 1\\subs.csv')))
# print(pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Python\\Pandas 1\\subs.csv').squeeze("columns"))

# virat kohli

# data = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Python\\Pandas 1\\kohli_ipl.csv',index_col='match_no').squeeze("columns")
# print(data)

# bollywood

data = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Python\\Pandas 1\\bollywood.csv',index_col='movie').squeeze("columns")
print(data)