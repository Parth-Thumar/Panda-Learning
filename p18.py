import numpy as np
import pandas as pd

# Math methods
ipl = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\ipl-matches.csv')
movies = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\movies.csv')

# print(movies.sum())
student_dicts = {
    'IQ' : [100, 80, 100, 90, 0, 0],
    'Marks' : [80, 70, 50, 90, 0, 0],
    'Package' : [10, 12, 8, 9, 0, 0]
}
students = pd.DataFrame(student_dicts,columns=['IQ','Marks','Package'])
print(students.sum(axis=1)) # row vise sum
print(students.sum()) # column vise sum
print(students.mean())
print(students.min())
print(students.max())
print(students.median())
print(students.var())

# single colm
print(type(movies['title_x']))

print(ipl['Venue'])

# multiple colm
print(movies[['year_of_release','actors','title_x']])

print(ipl[['Team1','Team2','WinningTeam']])