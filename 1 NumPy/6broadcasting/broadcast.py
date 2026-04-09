import numpy as np

var1 = np.array([1, 2, 3])
print(var1.shape)
print()
print(var1)
print()

var2 = np.array([[1], [2], [3]]) #in any one of the array there should be 1 in shape
print(var2.shape)
print()
print(var2)
print()

'''
1 2 3     1 1 1
1 2 3  +  2 2 2 
1 2 3     3 3 3
'''
print(var1 + var2)
