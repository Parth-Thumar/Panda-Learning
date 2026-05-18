# create series feom dict

import numpy as np
import pandas as pd
# Dictionary
mark = {
    'math' : 44,
    'english' : 35,
    'science' : 46,
    'physics' : 33
}
print(pd.Series(mark))