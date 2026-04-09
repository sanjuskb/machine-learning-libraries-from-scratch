import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

print(np.linalg.matrix_rank(A))

C = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(np.trace(C))

D = np.array([
    [1, 2],
    [2, 4.0001]
])

print(np.linalg.cond(D))
'''
What does np.linalg.cond(D) do?

It computes the condition number of matrix D.

In simple words:

The condition number tells you how sensitive a matrix is to small changes or numerical errors.

Why condition number matters ⚠️

When you use a matrix for:

solving linear equations (Ax = b)

matrix inversion

ML algorithms

numerical optimization

A high condition number means:

Tiny input errors → huge output errors

Computations become unstable

Results may be unreliable

A low condition number means:

Matrix is well-behaved

Computations are stable

What is special about your matrix?
[1      2     ]
[2   4.0001  ]


Notice something important 👀
The second row is almost a multiple of the first row:

Row2 ≈ 2 × Row1


That makes the matrix almost singular (almost non-invertible).

What output means

You’ll get a very large number, something like:

~ 100000 or more


This tells NumPy:

“This matrix is nearly singular and numerically dangerous.”

Mathematical meaning (intuitive, not heavy)

Condition number is roughly:

cond(D) = (largest stretch caused by D) / (smallest stretch caused by D)


If that ratio is huge → small errors explode.

Rule of thumb 🧠
Condition number	Interpretation
≈ 1	Excellent
< 100	Safe
> 10³	Risky
> 10⁸	Very unstable
∞	Singular matrix
'''