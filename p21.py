import numpy as np
import pandas as pd

ipl = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\ipl-matches.csv')
movies = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\movies.csv')

# how to Add New Cols
movies['Country'] = 'India'
# print(movies)

# from existing ones
print(movies['actors'].str.split('|').apply(lambda x:x[0]))

