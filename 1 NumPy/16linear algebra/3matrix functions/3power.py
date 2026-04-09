import numpy as np

var4 = np.matrix([[1,2],[3,4]])
print(var4)
print()

print(np.linalg.matrix_power(var4, 2))
print()

print(np.linalg.matrix_power(var4, 0))
print()

print(np.linalg.matrix_power(var4, -2))
print()

'''
Case 1: power = 2
A2=AxA

Case 2: power = 0
A0=I
power = -2
A-2=(A-1(A inverse))2
'''