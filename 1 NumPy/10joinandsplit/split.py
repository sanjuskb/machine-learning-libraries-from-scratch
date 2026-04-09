import numpy as np

var = np.array([1, 2, 3, 4, 5, 6])
print(var)

ar = np.array_split(var, 3) #split into 3 parts

print()
print(ar)
print()
print("type:")
print(type(ar)) #it splits the array and keeps it in the list
print()
print(ar[0])
print()

var1 = np.array([[1, 2],
                 [3, 4],
                 [5, 6]])

print(var1)

ar1 = np.array_split(var1, 3)# if axis is not given (default axis=0) here by default axis will be zero that means row index splottong happens for each index of row like row 0 ,row 1,row 2

ar2 = np.array_split(var1, 3, axis=1) #and we are trying to split into 3 parts vertically but only able to split into two parts 
print()
print(ar1)
print()
print(ar2)


'''
Your array
var1 = np.array([[1, 2],
                 [3, 4],
                 [5, 6]])

print(var1)


This array looks like:

[[1 2]
 [3 4]
 [5 6]]

Shape
(3 rows, 2 columns)

1 What does np.array_split() do?

np.array_split() divides an array into smaller sub-arrays

General form:

np.array_split(array, number_of_parts, axis)


If axis is not given:

axis = 0   # default

2 First case: ar1 = np.array_split(var1, 3)
ar1 = np.array_split(var1, 3)


Since axis is NOT given, NumPy uses:

axis = 0  → split along rows

Meaning:

“Split the array into 3 parts row-wise”

Step-by-step split (row-wise)

Original rows:

Row 0 → [1 2]
Row 1 → [3 4]
Row 2 → [5 6]


Splitting into 3 parts gives:

ar1[0] = [[1 2]]
ar1[1] = [[3 4]]
ar1[2] = [[5 6]]


Each part has 1 row.

So ar1 is a list of arrays:

[
 array([[1, 2]]),
 array([[3, 4]]),
 array([[5, 6]])
]

3 Second case: ar2 = np.array_split(var1, 3, axis=1)
ar2 = np.array_split(var1, 3, axis=1)


Here you explicitly said:

axis = 1  → split along columns

Important point ❗

Your array has only 2 columns, but you asked for 3 splits.

NumPy handles this gracefully (this is why array_split exists).

Step-by-step split (column-wise)

Columns:

Column 0 → [1, 3, 5]
Column 1 → [2, 4, 6]


Splitting into 3 parts, NumPy creates:

ar2[0] = [[1], [3], [5]]   # first column
ar2[1] = [[2], [4], [6]]   # second column
ar2[2] = []                # empty array


So result is:

[
 array([[1],
        [3],
        [5]]),

 array([[2],
        [4],
        [6]]),

 array([], shape=(3, 0), dtype=int)
]

4 Why does NumPy allow empty arrays here?

Because:

array_split never throws an error
It always returns the requested number of parts.

This is the key difference between:

split

array_split

5 split vs array_split (VERY IMPORTANT)
Function	When split is uneven
np.split()	❌ Error
np.array_split()	✅ Works (creates uneven / empty arrays)

That's why your code works.
'''