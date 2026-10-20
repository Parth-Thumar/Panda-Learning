import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# sort_values(series and dataframe) -> acsending -> na_position -> inplace -> multiple cols
x = pd.Series([12, 14, 1, 56, 89])
print(x.sort_values(ascending=False))

movies = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\movies.csv')
print(movies.sort_values('title_x',ascending=False))

students = pd. DataFrame(
    {
    'name': ['nitish', 'ankit', 'rupesh',np.nan, 'mrityunjay',np.nan, 'rishabh',np.nan, 'aditya',np.nan],
    'college':['bit', 'iit', 'vit',np.nan, np.nan, 'vlsi', 'ssit',np.nan, np.nan, 'git'],
    'branch':['eee', 'it','cse',np.nan, 'me','ce','civ','cse','bio',np.nan],
    'cgpa': [6.66,8.25,6.41, np.nan, 5.6,9.0,7.4,10,7.4, np.nan],
    'package': [4,5,6,np.nan, 6,7,8,9, np.nan, np.nan]
    }
)
print(students.sort_values('name',na_position='first',ascending=False,inplace=True))
print(students)

print(movies.sort_values(['year_of_release','title_x'],ascending=[True,False]))