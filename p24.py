import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# IMPORTANT Functions

# value_count(series and DataFrame)
a = pd.Series([1,1,1,2,3,3])
# print(a.value_counts()) # in series
marks = pd.DataFrame([
    [100, 80, 10],
    [90, 70, 7],
    [120, 100, 14],
    [80, 70, 14],
    [80, 70, 14]
],columns=['IQ','Marks','Package'])
# print(marks.value_counts())

ipl = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Backend\\Python\\Pandas 2\\ipl-matches.csv')

# find which player has won most potm -> in finals and qualifiers
print(ipl[~ipl['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts())

# Toss decision plot
print(ipl['TossDecision'].value_counts().plot(kind='pie'))
plt.show()

# how many matches each team has played
print((ipl['Team1'].value_counts() + ipl['Team2'].value_counts()).sort_values(ascending=False))