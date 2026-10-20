import numpy as np
import pandas as pd

students = pd. DataFrame(
    {
    'name': ['nitish', 'ankit', 'rupesh',np.nan, 'mrityunjay',np.nan, 'rishabh',np.nan, 'aditya',np.nan],
    'college':['bit', 'iit', 'vit',np.nan, np.nan, 'vlsi', 'ssit',np.nan, np.nan, 'git'],
    'branch':['eee', 'it','cse',np.nan, 'me','ce','civ','cse','bio',np.nan],
    'cgpa': [6.66,8.25,6.41, np.nan, 5.6,9.0,7.4,10,7.4, np.nan],
    'package': [4,5,6,np.nan, 6,7,8,9, np.nan, np.nan]
    }
)

# isnull(series + dataframe) -> check missing values -> return true
print(students['name'].isnull())
print(students[students['name'].isnull()])

# notnull(series + dataframe) -> check not missing values -> return true
print(students['name'].notnull())
print(students[students['name'].notnull()])

# hasnans(series) -> null value hai ya nahi ye batata hai
print(students['name'].hasnans)

print(students.isnull())
print(students.notnull())

# dropna(series + dataframe) -> how parameter -> works like or
print(students['name'].dropna())
print(students.dropna())
print(students.dropna(how='all'))
print(students.dropna(subset=['name']))
print(students.dropna(subset=['name','college']))

# filna(series + dataframe)
print(students['name'].fillna('Unknown'))
print(students['name'].fillna('Unknown').hasnans)
print(students.fillna(0))
print(students['package'].fillna(students['package'].mean()))

# drop_duplicated(series + dataframe) -> works like and -> duplicated()
marks = pd.DataFrame([
    [100, 80, 10],
    [90, 70, 7],
    [120, 100, 14],
    [80, 70, 14],
    [80, 70, 14]
],columns=['IQ','Marks','Package'])
print(marks.duplicated().sum())
temp = pd.Series([1, 1, 1, 2, 3, 3, 4, 4])
print(temp.drop_duplicates())
print(marks.drop_duplicates())

ipl = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\ipl-matches.csv')

# find the last match played by virat kohli in Delhi
ipl['all_players'] = ipl['Team1Players'] + ipl['Team2Players'] # -> merge column

def did_kohli_play(players_list):
    return 'V Kohli' in players_list

ipl['did_kohli_play'] = ipl['all_players'].apply(did_kohli_play)

print(ipl[(ipl['City'] == 'Delhi') & ipl['did_kohli_play'] == True].drop_duplicates(subset=['City','did_kohli_play'],keep='first'))

# drop(series + dataframe) -> row or column delete
temp = pd.Series([10, 2, 3, 16, 45, 78, 10])
print(temp.drop(index=[0, 6]))

print(students.drop(columns=['branch','cgpa']))
print(students.drop(index=[0,8]))
print(students.set_index('name').drop(index=['nitish','aditya']))

# apply(series + dataframe)
temp1 = pd.Series([10, 20, 30, 40, 50])
def sigmoid(value):
    return 1 / (1 + np.exp(-value))

# print(temp1.apply(sigmoid))
points_df = pd.DataFrame(
    {
        '1st point' : [(3,4), (-6,5), (0,0), (-10,1), (4,5)],
        '2nd point' : [(-3,4), (0,0), (2,2), (10,10), (1,1)]
    }
)
# print(points_df)
def euclidean(row):
    pt_A = row['1st point']
    pt_B = row['2nd point']

    return ((pt_A[0] - pt_B[0])**2 + (pt_A[1] - pt_B[1])**2)**0.5

points_df['distance'] = points_df.apply(euclidean,axis=1)
print(points_df)