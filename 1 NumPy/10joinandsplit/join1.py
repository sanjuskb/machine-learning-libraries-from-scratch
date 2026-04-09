import numpy as np

var_1 = np.array([1, 2, 3, 4])
var_2 = np.array([9, 8, 7, 6])

a_new  = np.stack((var_1, var_2), axis=0)#axis is zero it means print vertical
a_new1 = np.hstack((var_1, var_2))   # row
a_new2 = np.vstack((var_1, var_2))   # columns
a_new3 = np.dstack((var_1, var_2))   # height

# a_new2 = np.vstack((var_1, var_2))  and a_new  = np.stack((var_1, var_2), axis=0)  both are same

print(a_new)
print()

print(a_new1)
print()

print(a_new2)
print()

print(a_new3)

'''
np.stack() → adds a NEW dimension
a_new = np.stack((var_1, var_2), axis=0)

What stack does

Combines arrays

Creates a new axis (new dimension)

Result
[[1 2 3 4]
 [9 8 7 6]]

Shape
(2, 4)


👉 Think of this as putting one array below the other
👉 Two rows, four columns

🔹 Step 4: np.hstack() → horizontal stacking (row-wise)
a_new1 = np.hstack((var_1, var_2))

What happens

Joins arrays side by side

No new dimension created

Result
[1 2 3 4 9 8 7 6]

Shape
(8,)


👉 Just one long 1-D array

🔹 Step 5: np.vstack() → vertical stacking (column-wise)
a_new2 = np.vstack((var_1, var_2))

What happens

Stacks arrays one below the other

Converts 1-D arrays into 2-D rows

Result
[[1 2 3 4]
 [9 8 7 6]]

Shape
(2, 4)


👉 Very similar output to stack(axis=0)
👉 Difference: vstack is specialized for vertical stacking

🔹 Step 6: np.dstack() → depth stacking (3-D)
a_new3 = np.dstack((var_1, var_2))

This is the MOST confusing one — so read carefully

dstack creates a 3-D array

It stacks along the depth (third axis)

Result
[[[1 9]
  [2 8]
  [3 7]
  [4 6]]]

Shape
(1, 4, 2)


👉 Meaning:

1 block

4 rows

2 columns (depth)

🔹 Final Summary Table (VERY IMPORTANT)
Function	Dimension Result	Shape	Meaning
stack(axis=0)	2-D	(2, 4)	New dimension added
hstack()	1-D	(8,)	Join side by side
vstack()	2-D	(2, 4)	Stack vertically
dstack()	3-D	(1, 4, 2)	Stack in depth
'''