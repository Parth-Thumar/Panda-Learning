# series Methods

import pandas as pd

#  head and tail

# head --> first 5 raw print
# tail --> last 5 raw print

data = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Python\\Pandas 1\\kohli_ipl.csv',index_col='match_no')
# print(data.head())   # head
# print(data.head(6))

# print(data.tail())   # tail
# print(data.tail(10))

# sample --> ramdom no. print
print(data.sample())
print(data.sample(3))