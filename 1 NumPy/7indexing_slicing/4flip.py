import numpy as np
a = np.array([1, 2, 3, 4, 5])
rev = np.flip(a) #in case of 1D it reverse the array
print(rev)
print()
b=np.array([[1, 2, 3, 4, 5],[3,5,6,4,2]])#in case of 2D it flips the rows and reverse the numbers
rev = np.flip(b)
print(rev)
print()
rev = np.flipud(a)
print(rev)
print()
rev = np.flipud(b)
print(rev)
print()
'''flipud Originally meant for 2D (flip up-down)

For 1D, it simply reverses'''
