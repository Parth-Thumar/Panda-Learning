import numpy as np
import pandas as pd

data = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Python\\Pandas 1\\kohli_ipl.csv',index_col='match_no').squeeze("columns")

# Boolean Indexing on Series.
# find no. of 50's and 100's scored by virat kohli

print(data[data >= 50])
print(data[data >= 100])

print(data[data >= 50].size)

# find no. of ducks
print(data[data == 0].size)

# count no. of day when I had more than 200 subs a day
subs = (pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Python\\Pandas 1\\subs.csv').squeeze("columns"))
print(subs[subs >= 200].size)

# find actors who have done more than 20 movies
act = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Python\\Pandas 1\\bollywood.csv',index_col='movie').squeeze("columns")
num_movies = act.value_counts()
print(num_movies[num_movies >= 20])