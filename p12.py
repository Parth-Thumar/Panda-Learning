import numpy as np
import pandas as pd

# editing series

data = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Python\\Pandas 1\\kohli_ipl.csv',index_col='match_no').squeeze("columns")

# using indexing
mark = [97, 97, 86]
subject = ['Maths', 'Chemistry', 'Physics']
data = pd.Series(mark, index=subject)
data['Maths'] = 100
print(data)

# what if an index does not exist
data['Hindi'] = 73
print(data)

# slicing
runs = [101, 135, 65, 100, 120, 76, 117, 88]
run = pd.Series(runs)
run[2:4] = [104,81]
print(run)

# fancy indexing
run[[0,3,4]] = [154,145,139]
print(run)

# using index label
movie = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Python\\Pandas 1\\bollywood.csv',index_col='movie').squeeze("columns")
movie['Awara Paagal Deewana'] = 'Parth Thumar'
print(movie)