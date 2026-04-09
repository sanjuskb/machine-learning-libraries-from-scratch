import numpy as np

c = np.array([
    [1, 2, 3, 4],
    [3, 2, 4, 6],
    [1, 6, 3, 5]
])

print(np.diagonal(c))


'''
The main diagonal is where:

row index == column index


So the diagonal elements are:

c[0,0] = 1

c[1,1] = 2

c[2,2] = 3

👉 Diagonal = [1, 2, 3]

✅ BEST and simplest way (use NumPy)
print(np.diagonal(c))


Output:

[1 2 3]
'''