import numpy as np

#1d
var = np.array([12,4,76,24])
print(var)
print()

v = np.delete(var, 2) #element at index 2 will be deleted
print(v)
print()

#2d
var = np.array([[12,4,76],[21,42,61]])
print(var)
print()

v = np.delete(var, 2,axis=1)
print(v)
