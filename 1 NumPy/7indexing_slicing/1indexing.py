import numpy as np

var = np.array([9, 8, 7, 6])
#               0  1  2  3
#              -4 -3 -2 -1

print(var[1])
print(var[-3])
#8


var1 = np.array([[9, 8, 7], [4, 5, 6]])

print(var1)
print(var1.ndim)
print()

print(var1[0, 1]) #8

print()

var2 = np.array([[[1, 2], [6, 7]]])

print(var2)
print(var2.ndim)
print()

print(var2[0, 1, 1]) #7

c=np.array([[1,2,3,4],[3,2,4,6],[1,6,3,5]])
print(c[1]) #printing the row with index 1
print(c[:,1])#printing the column with index 1
