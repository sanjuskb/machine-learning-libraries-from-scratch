import numpy as np

A = np.array([[2, 1],
              [1, 1]])

B = np.array([5, 3])#it is nothing but..

# 2x + y = 5
# x + y = 3

x = np.linalg.solve(A, B)
print(x)

'''np.linalg.solve() (Solving Linear Equations)

This is NEW and important, especially for ML & simulations.


---

1: What problem does it solve?

It solves equations like:

2x + y = 5
x + y = 3

This is called a system of linear equations.


---

2: How NumPy represents this

Equation system becomes:

A · x = B

Where:

A = [[2, 1],
     [1, 1]]

B = [5, 3]


---

3: NumPy Code

import numpy as np

A = np.array([[2, 1],
              [1, 1]])

B = np.array([5, 3])

x = np.linalg.solve(A, B)
print(x)

Output

[2. 1.]

Meaning:

x = 2
y = 1


---

4: Why this matters (brief)

Used in:

Machine Learning (linear regression)

Physics simulations

Robotics motion equations

Optimization problems



---

5: Important rules (no theory, just facts)

A must be square (n×n)

det(A) ≠ 0

Faster & safer than inverse


❌ DON’T DO THIS:

np.linalg.inv(A) @ B

✅ DO THIS:

np.linalg.solve(A, B)


---

6: Shapes reminder

A shape	B shape	Works

(n,n)	(n,)	✅
(n,n)	(n,1)	✅
non-square	❌	❌



---

✔️ Status

No overlap with previous topics
New concept completed

Say NEXT
I’ll immediately move to the next remaining NumPy topic (rank / trace / condition number).'''