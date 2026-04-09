import numpy as np

# 1d array
az=np.zeros(5) #contains all elements as zero
print(az)


# 2d array
az1=np.zeros((3,4)) #3 rows ,4 colomns
print()
print(az1)
print(az1.dtype) #checks the datatype of array

print()

#3D
az=np.zeros((2,3,4)) #contains all elements as zero
print(az)


'''
output
[0. 0. 0. 0. 0.] for az
The dot (.) means the number is a floating-point number, not an integer.

By default, NumPy creates float arrays.

Internally, this is:

array([0., 0., 0., 0., 0.], dtype=float64)

Why does NumPy use floats by default?

Because NumPy is designed mainly for:

scientific computing

math

ML / AI

linear algebra

Most of these need decimal precision, so:
default dtype = float64


'''