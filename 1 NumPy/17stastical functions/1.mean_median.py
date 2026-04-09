import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(np.mean(a))
print()
print(np.mean(a,axis=0)) #mean along column
print()
print(np.mean(a,axis=1))#mean along rows
print()
print(np.median(a)) #middle value after sorting
print()
print(np.median(a,axis=0)) #middle value after sorting column wise
print()
print(np.median(a,axis=1)) #middle value after sorting rowise
print()
