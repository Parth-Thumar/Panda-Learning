import numpy as np
import pandas as pd

# Sereies maths methods
# 1. count --> print total no.

data = pd.read_csv('C:\\Users\\parth\\OneDrive\\Desktop\\Python\\Pandas 1\\kohli_ipl.csv',index_col='match_no').squeeze("columns")
print(data.count())

# 2. sums

print(data.sum())

# 3. product

print(data.product())

# 4. mean -> meidan -> mode -> std -> var

print(data.mean()) # avg type score
print(data.median()) # score of median
print(data.mode())  # sabse zyada bar in data
print(data.std())
print(data.var())

# 5. min/max

print(data.min()) # show min score
print(data.max()) # show max score

# 6. describe

print(data.describe()) # all methods print