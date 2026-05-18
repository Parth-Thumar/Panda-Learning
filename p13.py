import numpy as np
import pandas as pd

# series with python funtionalities

subs = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Python\\Pandas 1\\subs.csv').squeeze("columns")
# print(len(subs))
# print(type(subs))
# print(dir(subs))
# print(sorted(subs))
# print(min(subs))
# print(max(subs))

# type conversion

mark = [97, 97, 86]
subject = ['Maths', 'Chemistry', 'Physics']
data = pd.Series(mark, index=subject)
print(list(data))
print(dict(data))

# membership operator -> if chech movie is here in file true or false
# only work in index value not work on values
movie = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Python\\Pandas 1\\bollywood.csv',index_col='movie').squeeze("columns")
print('Evening Shadows' in movie)
print('Parth Thumar' in movie)

# looping

# for i in movie.index: # only movie to print actor name or .index to print movie name
#     print(i)

# operator arithmetic(Broadcasting)

mark = [97, 97, 86]
subject = ['Maths', 'Chemistry', 'Physics']
data = pd.Series(mark, index=subject)
print(100 - data)

# relational operator

data = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Python\\Pandas 1\\kohli_ipl.csv',index_col='match_no').squeeze("columns")
print(10 <= data)