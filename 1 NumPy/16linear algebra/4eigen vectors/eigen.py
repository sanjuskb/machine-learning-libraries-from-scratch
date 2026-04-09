'''
Let's take the simplest matrix:
import numpy as np

A = np.array([[2, 0],
              [0, 1]])

This matrix:
stretches x-direction
keeps y-direction same

Now ask NumPy:
values, vectors = np.linalg.eig(A)

print(values)
print(vectors)
Output (conceptually):


Eigenvalues: [2. 1.]
Eigenvectors:
[[1. 0.]
 [0. 1.]]
Step 3: How to READ this output (important)
🔹 Eigenvalues
[2. 1.]
Means:
one direction stretches 2x
another direction stretches 1x
🔹 Eigenvectors
[[1. 0.]
 [0. 1.]]
This means:
Eigenvector 1 → [1, 0] → x-axis
Eigenvector 2 → [0, 1] → y-axis
So NumPy is telling:
“These directions remain straight.”
Step 4: Why vectors are shown as columns
This part confuses many people.
vectors =
[[1, 0],
 [0, 1]]
Read it column-wise, not row-wise.
So:
First eigenvector → [1, 0]
Second eigenvector → [0, 1]
👉 Each column = one eigenvector

--------------------------------------------------------------------------------------

Very important rule (lock this)

A x eigenvector = eigenvalue x same eigenvector

NumPy simply finds:
which vectors satisfy this
and returns them

 When should YOU use eigen in NumPy?
For now, remember:
Use np.linalg.eig() only on square matrices
Output:
first → eigenvalues
second → eigenvectors (columns)

-----------------------------------------------------------------------------

Your line
values, vectors = np.linalg.eig(A)


You're asking:

“We used two variables on the left and one function call on the right — why doesn’t this cause an error?”

🔑 Core idea (VERY IMPORTANT)

np.linalg.eig(A) returns TWO things packed together as a tuple.

Python allows you to unpack multiple returned values into multiple variables.

This is called tuple unpacking (or multiple assignment).

1: What np.linalg.eig(A) actually returns

Internally, NumPy does something like this:

return (eigenvalues, eigenvectors)


So:

np.linalg.eig(A)


returns a tuple:

(
  array([...]),   # eigenvalues
  array([...])    # eigenvectors
)

2: How Python assigns them (step by step)
values, vectors = (eigenvalues, eigenvectors)


Python matches positionally:

values ← first element

vectors ← second element

✔ No error
✔ Clean and safe

3: Why Python allows this (design reason)

Python is designed to support functions that naturally return multiple results.

Examples:

a, b = 10, 20
x, y = (5, 6)


This is built into the language, not NumPy magic.
'''