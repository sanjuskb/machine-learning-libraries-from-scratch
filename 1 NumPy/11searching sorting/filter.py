# Filter Array
import numpy as np

var_3 = np.array(["a","s","d","f"])
f = [True, False, False, True]

new_a = var_3[f]
print(new_a)

'''
Each True → keep element

Each False → remove element

This is called Boolean Masking


Used heavily in:
Data Science

Machine Learning

Filtering datasets
'''