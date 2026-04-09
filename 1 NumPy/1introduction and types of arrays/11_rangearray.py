import numpy as np


# Valid forms are:
# np.arange(stop)
# np.arange(start, stop)
# np.arange(start, stop, step)

#1D
ar=np.arange(4)
print(ar)
print()
# [0 1 2 3]

#2D
arr = np.arange(15).reshape(3,5) #values from 0 to 14 are stored in matrix
print(arr)
print()
#2D
arr = np.arange(5,20).reshape(3,5) #values from 5 to 19 are stored in matrix
print(arr)
print()
#2D
arr = np.arange(5,35,2).reshape(3,5) #values from 5 to 35 (skipping one value) are stored in matrix
print(arr)
print()
#3D
arr = np.arange(5,35).reshape(2,3,5) #values from 5 to 34 are stored in matrix
print(arr)
print()

# print(np.arange((3,5))) cant do this because
'''
print(np.arange((3,5)))
Why this does NOT work ❌
🔑 Key rule about np.arange
np.arange() expects numbers, not a shape.

Valid forms are:

np.arange(stop)
np.arange(start, stop)
np.arange(start, stop, step)
Examples:


np.arange(5)        # 0 1 2 3 4
np.arange(3, 5)     # 3 4
np.arange(0, 10, 2) # 0 2 4 6 8
What (3,5) actually is

(3,5)
This is a tuple, and in NumPy it usually means:

“I am describing a SHAPE, not values.”

So when you do:


np.arange((3,5))
NumPy thinks:

“You're asking me to count from 0 to (3,5)”

But:

(3,5) is not a number

it's a pair of numbers (tuple)

👉 NumPy cannot count to a tuple, so it throws an error.

The correct way to think (VERY IMPORTANT)
arange → creates VALUES

(3,5) → describes SHAPE

These are two different concepts.

✅ Correct way to get a (3,5) array using arange
You must do it in two steps:


arr = np.arange(15).reshape(3,5)
print(arr)
Why 15?

Copy code
3 x 5 = 15
Output:


[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]

arr = np.arange(15).reshape(3,5)
1 What np.arange(15) REALLY creates
 
np.arange(15)
This creates a 1D array in memory:


Index →  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
Value →  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
Shape

(15,)
Memory reality (important)
All 15 numbers are stored contiguously

One after another in memory

No rows, no columns yet — just a flat line

2 What reshape(3,5) is allowed to do
🔑 First internal check (CRITICAL)
NumPy checks:


old_size == new_size ?
15 == (3 x 5) ?
✔ YES
If this fails → ❌ ERROR

How reshape maps 1D → 2D (row-major order)

NumPy uses C-order (row-major) by default.

That means:

Fill rows left to right, then go to next row

Let's map it manually 👇

Original 1D memory
0  1  2  3  4  5  6  7  8  9 10 11 12 13 14

Now reshape into (3,5)
Row 0 → first 5 elements
[0 1 2 3 4]

Row 1 → next 5 elements
[5 6 7 8 9]

Row 2 → next 5 elements
[10 11 12 13 14]

Final structure
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]

 
 For arr.reshape(3,5)

Shape → (3, 5)

Strides → (5 * itemsize, 1 * itemsize)

Meaning:

To move one row down, jump 5 elements

To move one column right, jump 1 element

So NumPy calculates:

element[i, j] = base_address + (i*5 + j*1)


🔥 This is why reshape is FAST — no data movement.

element[i, j] = base_address + (i*5 + j*1)

Let's decode it word by word.

🔹 base_address

👉 Address of the first element (0)

🔹 Why i * 5 ?

Each row has 5 elements.

So:

Row 0 starts at element 0

Row 1 starts at element 5

Row 2 starts at element 10

That's why:

row_jump = 5


So moving down one row means:

jump 5 elements

🔹 Why j * 1 ?

Inside a row:

Each column is next element

So moving right = jump 1 element

What are “strides” REALLY?

Forget the word — think jump size.

Movement	Jump size
Down 1 row	jump 5 elements
Right 1 column	jump 1 element

NumPy just stores these jump values instead of copying data.

That's it.
'''


