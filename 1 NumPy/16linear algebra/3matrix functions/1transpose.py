import numpy as np

var = np.matrix([[1,2,3],
                 [4,5,6]])

print(var)
print()

print(np.transpose(var))
print()

print(var.T) #shortcut of transpose
print()

print(np.swapaxes(var, 0, 1)) #swaps two axes


'''
So are they the same?

 YES for 2D arrays

Because:

axis 0 = rows

axis 1 = columns

swapping them = transpose

❗ But NOT always same

For 3D or higher arrays, they are different tools:

Function	Meaning
transpose	Reorders all axes
swapaxes	Swaps only two axes
'''