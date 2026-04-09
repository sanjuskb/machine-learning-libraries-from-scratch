import numpy as np
var2 = np.array([1,2,3,4,5,6])
y = np.resize(var2, (3,2))
print(y)
print(np.ravel(y, order="K"))

# ravel same as flatten

# order="K" means:

# Keep existing memory order
# 
# Your array y was created row-wise → so ravel keeps that order.
'''
flatten()	                    ravel()
Always returns a copy	        Returns a view if possible
Slightly                        slower	Faster
Safer	                        Memory-efficient'''