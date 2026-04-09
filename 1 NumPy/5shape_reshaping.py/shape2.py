import numpy as np
#2D array
# a=[[1,2,3,4]]
# a=[[1,2,3,4],[1,2,3,4]]
# a=[[1,2,3,4],[1,2,3,4],[1,2,3]] no.0f elements in all the lists should be same
a=[[1,2,3,4],[1,2,3,4],[1,2,3,4]] #Each inner list = one row --> 3 rows 4 coloumns
b=np.array(a)
print(b)
print(b.ndim)
print()
print(b.shape)
