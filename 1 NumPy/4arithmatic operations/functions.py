import numpy as np

# 1D array
var = np.array([4, 4, 1, 4, 5, 3, 2])

print("min : ", np.min(var), np.argmin(var))
print()
print("max : ", np.max(var), np.argmax(var))
print()
print("sqrt : ", np.sqrt(var))
print()

# 2D array

var1 = np.array([[2, 1, 3], [9, 5, 6]])

print(np.min(var1, axis=0))
print()
print(np.min(var1, axis=1))
print()

'''
Visually:

Column 0	Column 1	Column 2
2	            1	       3
9	            5	       6

 What does axis=0 mean here?

🔑 axis = 0 → operate DOWN the rows (column-wise)

So NumPy does this:

“For each column, find the minimum value.”


'''

var2 = np.array([1, 2, 3])

print(np.sin(var2))
print()
print(np.cos(var2))
print()
print(np.cumsum(var2))
print()
'''
Cumulative sum
np.cumsum(var2)


Step by step:

1

1 + 2 = 3

3 + 3 = 6
---------------------------------------------------------------------------------------------

NumPy calculates sin() in radians, NOT degrees

So when you see:

np.sin(1)


It means:

sin(1 radian)
❌ not sin(1°)

What is a radian? (simple meaning)

A radian is another way to measure angles.

360° = 2π radians

180° = π radians

1 radian ≈ 57.3°

So:

1 radian ≈ 57.3 degrees

'''