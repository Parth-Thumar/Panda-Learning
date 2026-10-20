import numpy as np
import pandas as pd

ipl = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\ipl-matches.csv')
movies = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\movies.csv')
vk = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\kohli_ipl.csv')
subs = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\subs.csv')

# astype method -> change data type
import sys
print(sys.getsizeof(vk))
print(sys.getsizeof(vk.astype('int16')))

# between
print(vk[vk['runs'].between(51,99)].size)

# clip
print(subs.clip(100,200))

# drop_duplicate
temp = pd.Series([1, 1, 2, 2, 3, 3, 4, 4])
print(temp.duplicated().sum())
print(temp.drop_duplicates())
print(temp.drop_duplicates(keep = 'last'))
print(movies.drop_duplicates())
print(vk.duplicated().sum())

temp1 = pd.Series([1, 2, 3, np.nan, 5, 6, np.nan, 8, np.nan, 10])
print(temp1.count())

# isnull
print(temp1.isnull().sum())

# dropna
print(temp1.dropna())

# filna
print(temp1.fillna(0))

# isin
print(vk[vk['runs'].isin([49, 99])])

# apply
print(movies['actors'].apply(lambda x:x.split()[0].uppper()))

print(subs)
print(subs['Subscribers gained'].apply(
    lambda x: 'Good Day' if x > subs['Subscribers gained'].mean() else 'Bad Day'
))

# copy -> how to use copy
new = vk.head(5)
print(new)