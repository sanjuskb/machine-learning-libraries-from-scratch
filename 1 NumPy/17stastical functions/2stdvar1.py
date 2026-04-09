import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(np.var(a))#same concept it flattens the 2D array and calculates the mean then calculates variance
print()
print(np.var(a,axis=0))
print()
print(np.var(a,axis=1))
print()
print(np.std(a))
print()
print(np.std(a,axis=0))
print()
print(np.std(a,axis=1))