import numpy as np

# Iteration over a 1D NumPy array
var = np.array([9, 8, 7, 6, 5, 4])
print(var)
print()

for i in var:
    print(i)

# Iteration over a 2D NumPy array(row wise)
var1 = np.array([[1, 2, 3, 4],
                 [1, 2, 3, 4]])

print(var1)
print()

for j in var1:
    print(j)

# Iteration over a 2D NumPy array(element wise)

var1 = np.array([[1, 2, 3, 4],
                 [1, 2, 3, 4]])

print(var1)
print()

for k in var1:
    for l in k:
       print(l)

# Iteration over a 3D NumPy array using nested loops
var3 = np.array([[[9, 8, 7, 6],
                  [1, 2, 3, 4]]])

print(var3)
print(var3.ndim)
print()

for i in var3:
    for j in i:
        for k in j:
            print(k)
#no.of dimensions is equal to no.of loops


