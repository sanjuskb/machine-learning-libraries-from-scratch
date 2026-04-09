import numpy as np
#1D array
var = np.array([9, 8, 7, 6, 5, 4, 3])
       # index: 0  1  2  3  4  5  6

print(var)
print()

print("8 to 5 : ", var[1:5])      #[8 7 6 5]
print()
print("8 to End : ", var[1:])     #[8 7 6 5 4 3]
print()
print("start to 5 : ", var[:5])   #[9 8 7 6 5]
print()
print("stop : ", var[1:5:2])      #[8 6]
print()
print(var[::1])
print()
print(var[::-1])
print()

#2D array

var1 = np.array([
    [1, 2, 3, 4, 5],
    [9, 8, 7, 6, 5],
    [11, 12, 13, 14, 15]
])

print(var1)
print()

print("8 to 5 : ", var1[1, 1:])
print()