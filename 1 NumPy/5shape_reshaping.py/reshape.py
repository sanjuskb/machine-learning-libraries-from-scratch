import numpy as np
y=[2,3,4,5,4,8]
x=np.array(y)
print(x)
print()
print(x.ndim)

new=x.reshape(3,2) #1D array is changing into 2D
print(new)
print()
print(new.ndim)

# new1=x.reshape(3,3) #we have 6 elements but we are storing 9 elements it shows error
# new=x.reshape(2,2) it is also not possible


