import numpy as np
a=np.random.rand(20)
print(a)
b=np.round(a,2) #gives the float values upto 2 decimals
print(b)
b[b<0.5]=0 # replacing the elements that are less  than zero.5 with zero
print(b)