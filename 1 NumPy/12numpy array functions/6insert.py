import numpy as np

var = np.array([1, 2, 3, 4])
print(var)

# np.insert(array, index, value)

v = np.insert(var, 2, 5)
print(v)
# v = np.insert(var, (2,5), 6.5) shows error . no index 5

v = np.insert(var, (2,4), 6.5)  # 6.5 is inserted as 6.no floating numbers can be inserted
print(v)
