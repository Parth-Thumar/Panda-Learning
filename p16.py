import numpy as np
import pandas as pd

# Creating DataFrame
# using lists

student = [
    [100, 80, 10],
    [80, 70, 12],
    [100, 50, 8],
    [90, 90 , 9]
]
print(pd.DataFrame(student, columns=['IQ','Marks','Package']))

# using dicts

student_dicts = {
    'IQ' : [100, 80, 100, 90, 0, 0, 0, 0, 0],
    'Marks' : [80, 70, 50, 90, 0, 0],
    'Package' : [10, 12, 8, 9, 0, 0]
}
students = pd.DataFrame(student_dicts)
print(pd.DataFrame(student_dicts))