import numpy as np

#1D array
var = np.array([1, 2, 3, 4])
var1 = np.array([9, 8, 7, 6])
ar = np.concatenate((var, var1))
print(ar)
print()


#2D array
vr = np.array([[1, 2],
               [3, 4]])

vr1 = np.array([[9, 8],
                [7, 6]])


print(vr)
print()

print(vr1)
print()
ar_new = np.concatenate((vr, vr1), axis=1)
# axis is one it means merge horizontally

print(ar_new)

#in concantenate function no new dimension is created just joining of elements 
#in stack function  new dimension is created  


