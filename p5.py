import numpy as np
import pandas as pd

ipl = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\ipl-matches.csv')
movies = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\movies.csv')

# find all the final winners:
mask = ipl['MatchNumber'] == 'Final'
new_df = ipl[mask]
print(new_df[['Season','WinningTeam']])

# same
print(ipl[ipl['MatchNumber'] == 'Final'][['Season','WinningTeam']])

# how many super over finishes have occred
print(ipl[ipl['SuperOver'] == 'Y'].shape[0])

# how many matches has csk won in kolkata
print(ipl[(ipl['City'] == 'Kolkata') & (ipl['WinningTeam'] == 'Chennai Super Kings')].shape[0])

# toss winner is match winner in percentage
print((ipl[ipl['TossWinner'] == ipl['WinningTeam']].shape[0] / ipl.shape[0]) * 100)

# movies with rating higher than 8 and votes > 10000
print(movies[(movies['imdb_rating'] > 8) &(movies['imdb_votes'] > 10000)].shape[0])

# Action moveis with rating higher than 7.5
mask1 = movies['genres'].str.split('|').apply(lambda x:'Action' in x)
mask2 = movies['imdb_rating'] > 7.5
print(movies[mask1 & mask2])
