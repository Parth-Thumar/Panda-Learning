import numpy as np
import pandas as pd

ipl = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\ipl-matches.csv')
movies = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\movies.csv')

student_dicts = {
    'Name' : ['nitish','ankit','rishabh','amit','rupesh','raj'],
    'IQ' : [100, 80, 100, 90, 0, 0],
    'Marks' : [80, 70, 50, 90, 0, 0],
    'Package' : [10, 12, 8, 9, 0, 0]
}
students = pd.DataFrame(student_dicts,columns=['Name','IQ','Marks','Package'])
print(student_dicts.set_index('Name'))

# selecting rows from a DataFrame
# iloc - searching using index positions
# loc - searching using index labels

# single row --> series
print(movies.iloc[0])

# multiple row --> DataFrame
print(movies.iloc[5:15:2])

# fancy indexing
print(movies.iloc[[0, 4, 5]])

# loc
print(students.loc['nitish'])