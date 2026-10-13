import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Plotting graphs on Series.

data = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Python\\Pandas 1\\kohli_ipl.csv',index_col='match_no').squeeze("columns")
# data.plot()
# plt.show()

acts = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Python\\Pandas 1\\bollywood.csv',index_col='movie').squeeze("columns")
acts.value_counts().head(20).plot(kind='pie')
plt.show()