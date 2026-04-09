import numpy as np

var  = np.matrix([[1,2],[1,2]])
var2 = np.matrix([[1,2],[1,2]])

print(var)
print(type(var))
print()

print("addition:",var+var2)
print()
print(var * var2)
print()
print(var.dot(var2))
print()


#array
print("array")
var  = np.array([[1,2],
                 [1,2]])
var2 = np.array([[1,2],
                 [1,2]])

print(var)
print(type(var))
print()
print("addition:",var+var2)
print()
print(var * var2)

'''
adddition will be same in both matrix and array but multiplication will be different

array multiplies adjacent elements

A * B   ❌  element-wise
A @ B   ✅  matrix multiplication

np.array + @ operator
Matrix multiplication

vector x matrix
v = np.array([1, 2])
M = np.array([[2, 0],
              [0, 3]])

              
v @ M
v @ M = [ (1*2 + 2*0), (1*0 + 2*3) ]
       = [2, 6]

Case 2: What happens with v * M ❓ (your doubt)
Now this is NOT matrix multiplication
This is element-wise multiplication with broadcasting
Let's understand how NumPy thinks.
Step 1: Shapes


v → shape (2,)
M → shape (2, 2)
They are not the same shape, so NumPy tries broadcasting.
Step 2: Broadcasting rule (VERY IMPORTANT)
When shapes differ:
NumPy stretches the smaller array
WITHOUT copying data
To match the larger shape
So vector v becomes:


v = [1, 2]

broadcasted as:
[[1, 2],
 [1, 2]]
(Repeated for each row)
Step 3: Element-wise multiplication
Now NumPy multiplies element by element:


M = [[2, 0],
     [0, 3]]

v = [[1, 2],
     [1, 2]]
Multiply:


[[2*1, 0*2],
 [0*1, 3*2]]

= [[2, 0],
   [0, 6]]
'''