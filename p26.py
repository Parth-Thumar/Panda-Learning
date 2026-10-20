import numpy as np
import pandas as pd

ipl = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\ipl-matches.csv')

# rank(series)
batsman = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\batsman_runs_ipl.csv')
batsman['bating_rank'] = batsman['batsman_run'].rank(ascending=False)
print(batsman.sort_values('bating_rank'))

# sort_index(series and dataframe)
marks = {
    'maths' : 67,
    'english' : 57,
    'science' : 89,
    'hindi' : 100
}
marks_series = pd.Series(marks)
print(marks_series.sort_index(ascending=False))

movies = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\movies.csv')
print(movies.sort_index(ascending=False))

# set_index(dataframe) -> inplace
print(batsman.set_index('batter',inplace=True))
print(batsman)

# reset_index(series + dataframe) -> drop parameter
print(batsman.reset_index(inplace=True))
print(batsman)

# how to replace existing index without loosing
print(batsman.reset_index().set_index('bating_rank'))

# series to datafrme using reset_index
print(marks_series.reset_index())

# rename
print(movies.set_index('title_x',inplace=True))
print(movies.rename(columns={'imdb_id':'imdb', 'poster_path':'link'},inplace=True))
print(movies.rename(index={'Uri: The Surgical Strike':'URI','Battalion 609':'Battalion'},inplace=True))
print(movies)

# unique(series)
temp = pd.Series([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, np.nan, np.nan])
print(temp.unique())
print(temp.nunique())
print(ipl['Season'].unique().shape[0]) # other use len(ipl['Season'].unique())
