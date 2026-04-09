# np.where() — Finding positions that satisfy a condition

import numpy as np

var = np.array([4,2,3,4,2,5,2,5,6,7])
x = np.where(var % 2 == 0)
print(x)

'''
var % 2 == 0 → checks even numbers

np.where() returns indexes where condition is True
'''