#instead of using for loops direct use of functions
import numpy as np

var3 = np.array([[[9, 8, 7, 6],
                  [1, 2, 3, 4]]])

print(var3)
print(var3.ndim)
print()

for i in np.nditer(var3):
    print(i)
'''
Meaning of nditer

nditer = n-dimensional iterator

Where:

n = any number of dimensions
'''