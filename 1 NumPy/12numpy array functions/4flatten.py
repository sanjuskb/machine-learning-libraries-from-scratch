import numpy as np
var2 = np.array([1,2,3,4,5,6])
y = np.resize(var2, (3,2))
print(y)
print()
print(y.flatten())
print(y.flatten(order="F"))

# flatten() always returns a 1D copy

# It reads elements row by row (C-order) by default.

# order="F" means Fortran order → read column first