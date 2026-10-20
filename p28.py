import numpy as np
import pandas as pd

ipl = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\ipl-matches.csv')
movies = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\imdb-top-1000.csv')

genres = movies.groupby('Genre')

# Applying builtin aggregation functions on groupby objects
print(genres.sum(numeric_only=True))
print(genres.min())
print(genres.mean(numeric_only=True))
print(genres.std(numeric_only=True))

# find the top 3 genres by total earning
print(movies.groupby('Genre').sum(numeric_only=True)['Gross'].sort_values(ascending=False).head(3)) # -> more time run
print(movies.groupby('Genre')['Gross'].sum(numeric_only=True).sort_values(ascending=False).head(3)) # -> less time run

# find the game with highest avg IMDB rating
print(movies.groupby('Genre')['IMDB_Rating'].mean(numeric_only=True).sort_values(ascending=False).head(1))

# find director with most popularity
print(movies.groupby('Director')['No_of_Votes'].sum(numeric_only=True).sort_values(ascending=False).head(1))

# find the highest rated movie of each genre
print(movies.groupby('Genre')['IMDB_Rating'].max(numeric_only=True))

# find number of movies done by each actor
# print(movies['Star1'].value_counts())
print(movies.groupby('Star1')['Series_Title'].count().sort_values(ascending=False))

# Groupby Attributes and Methods
# find total number of groups -> len
# find items in each group ->size
# first()/last() -> nth item
# get_group -> vs filtering
# groups
# describe
# sample
# nunique

print(len(movies.groupby('Genre')))
print(movies['Genre'].nunique())
print(movies.groupby('Genre').size())
print(movies['Genre'].value_counts())

print(genres.first())
print(genres.last())
print(genres.nth(7))

print(genres.get_group('Horror'))
print(genres.groups)
print(genres.describe())
print(genres.sample(2,replace=True))
print(genres.nunique())

# agg method
# passing dict
print(genres.agg(
    {
        'Runtime':'mean',
        'IMDB_Rating':'mean',
        'No_of_Votes':'sum',
        'Gross':'sum',
        'Metascore':'min'
    }
))

# looping on groups
# find the highest rated movie of each genre
df = pd.DataFrame(columns=movies.columns)
print(df)
for group,data in genres:
    # print(type(group))
    # print(type(data))
    df = pd.concat([df, data[data['IMDB_Rating'] == data['IMDB_Rating'].max()]])
print(df)

# split (apply) combine
# apply -> builtin function
print(genres.apply(max))

# findnumber of movies starting with A for each group
def foo(group):
    return group['Series_Title'].str.startswith('A').sum()
print(genres.apply(foo))

# find ranking of each movie in the ggroup according to IMDB score
def rank_movie(group):
    group['genre_rank'] = group['IMDB_Rating'].rank(ascending=False)
    return group
print(genres.apply(rank_movie))

# find normalix=zation IMDB group wise
def normal(group):
    group['norm_rating'] = (group['IMDB_Rating'] - group['IMDB_Rating'].min()) / (group['IMDB_Rating'].max() - group['IMDB_Rating'].min())
    return group
print(genres.apply(normal))

# group by multiple cols , size, get_group
duo = movies.groupby(['Director','Star1'])
# size
print(duo.size())
# get_group
# Debug: find the correct spelling/casing
print(duo.get_group(('Zoya Akhtar', 'Hrithik Roshan')))

# Once you know the exact values, use them here, e.g.:
print(duo.get_group(('Aamir Khan', 'Amole Gupte')))

# find the most earning actor->director combo
print(duo['Gross'].sum().sort_values(ascending=False))

# find best(in-terms of metascore(avg)) actor->gener combo
print(movies.groupby(['Star1', 'Genre'])['Metascore'].mean().reset_index().sort_values('Metascore',ascending=False))

# agg on multiple groupby
print(duo.agg(['min', 'max', 'mean']))

ipl1 = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\deliveries (1).csv')
# find the top 10 batsman in terms of runs
print(ipl.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10))

# find the batsman with max no of sixes
six = ipl1[ipl1['batsman_runs'] == 6]
print(six.groupby('batsman')['batsman'].count().sort_values(ascending=False).head(1))

# find batsman with most number of 4's and 6's in last 5 over
temp_df = ipl1[ipl1['over'] > 15]
temp_df = temp_df[(temp_df['batsman_runs'] == 4) | (temp_df['batsman_runs'] == 6)]
print(temp_df.groupby('batsman')['batsman'].count().sort_values(ascending=False))

# find V Kohli's record against all teams
temp_df = ipl1[ipl1['batsman'] == 'V Kohli']
print(temp_df.groupby('bowling_team')['batsman_runs'].sum())

# create a function that can return the highest score of any batsman
temp_df = ipl1[ipl1['batsman'] == 'V Kohli']
print(temp_df.groupby('match_id')['batsman_runs'].sum().sort_values(ascending=False).head(1).values[0])

def highest(batsman):
    temp_df = ipl1[ipl1['batsman'] == batsman]
    return temp_df.groupby('match_id')['batsman_runs'].sum().sort_values(ascending=False).head(1).values[0]

print(highest('V Kohli'))