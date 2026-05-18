# Series Attributes

import numpy as np
import pandas as pd

mark = [97, 97, 86]
subject = ['Maths', 'Chemistry', 'Physics']
mark_s = pd.Series(mark, index= subject, name = 'Parth na marks')

# size
print(mark_s.size)

# dtype
print(mark_s.dtype)

# name
print(mark_s.name)

# is_unique
print(mark_s.is_unique)

# index
print(mark_s.index)

# value
print(mark_s.values)