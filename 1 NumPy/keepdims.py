import numpy as np

a=np.array([[1,2,3],
            [4,5,6]])
print(np.sum(a,axis=1)) #we get 1D but to keep the dimension same as 2D

print()
print(np.sum(a,axis=1,keepdims=True))
