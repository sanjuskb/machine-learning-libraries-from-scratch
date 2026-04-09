import numpy as np
y=[1,2,3,4,5,4,8,9,10,11,12,6]
x=np.array(y)
print(x)
print()
print(x.ndim)
new=x.reshape(2,3,2) # 2 sets of 3x 2 matrices

'''
[[[ 1  2]
  [ 3  4]
  [ 5  4]]

 [[ 8  9]
  [10 11]
  [12  6]]]
'''
print(new)
print()
print(new.ndim)

print()

one=new.reshape(-1) #convereting back into 1D
print(one)
print()
print(one.ndim)