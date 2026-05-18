import numpy as np
import pandas as pd

runs = [101, 135, 65, 100, 120, 76, 117, 88]
print(pd.Series(runs))

# custom index 
mark = [97, 97, 86]
subject = ['Maths', 'Chemistry', 'Physics']
print(pd.Series(mark, index=subject))

# setting a name 

print(pd.Series(mark, index = subject, name = 'Parth na marks'))
