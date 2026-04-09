import numpy as np
# 1D
var = np.array([1,2,3,4])
var1 = np.array([1,2,3,4])
print(var@var1) #1*1+2*2+3*3+4*4
print()

#2D
var = np.array([[1,2],
                [4,5]])
var1 = np.array([[1,2],
                 [4,3]])
c=var@var1
print(c)

# @ = multiply & sum corresponding rows and columns
# @ is the matrix multiplication operator
# # A @ B
# np.matmul(A, B)
# np.dot(A, B)

