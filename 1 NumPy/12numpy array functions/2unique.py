import numpy as np

var1 = np.array([1,2,3,4,2,5,2,6,2,7])

x = np.unique(
    var1,
    return_index=True,
    return_counts=True
)

print(x)