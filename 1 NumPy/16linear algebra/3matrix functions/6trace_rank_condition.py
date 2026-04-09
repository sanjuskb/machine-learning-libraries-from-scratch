'''



---

1️⃣ np.linalg.rank() — Matrix Rank

What is rank (simple meaning)?

👉 Rank = number of independent rows or columns

Independent means:

One row is not a combination of another row.



---

Example 1: Full rank matrix

import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

np.linalg.rank(A)

Output: 2

✔ Both rows are independent
✔ Rank = 2


---

Example 2: Dependent rows

B = np.array([
    [1, 2],
    [2, 4]
])

np.linalg.rank(B)

Output: 1

Why?

Second row = 2 × first row

No new information

So rank drops



---

Why rank matters (ML intuition)

Rank tells how much information is actually present

Low rank → redundant features

Full rank → good data


Used in:

Linear regression

Feature selection

Dimensionality reduction



---

2️⃣ np.trace() — Sum of Diagonal

What does trace do?

👉 Trace = sum of diagonal elements

Diagonal = top-left → bottom-right


---

Example

C = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

np.trace(C)

Calculation:

1 + 5 + 9 = 15

Output: 15


---

Why trace exists

Trace often represents:

Total self-effect

Sum of variances (in covariance matrix)

Important in statistics & ML theory


You won’t manually use it much, but you must recognize it.


---

3️⃣ np.linalg.cond() — Condition Number (Concept Only)

This is conceptual, not something you’ll code daily.


---

What is condition number?

👉 It measures how sensitive a matrix is to small errors

Small condition number → stable

Large condition number → unstable



---

Example

D = np.array([
    [1, 2],
    [2, 4.0001]
])

np.linalg.cond(D)

You’ll get a very large number

Why?

Rows are almost dependent

Small change → huge output error



---

Real-world meaning

Imagine:

Two measurements almost identical

Slight noise → wrong prediction


So:

High condition number = dangerous matrix

Low condition number = safe matrix


Used internally in:

Solvers

Optimization

ML libraries (you rarely call it directly)



---

🔚 SUMMARY (LOCK THIS IN)

Function	Purpose

rank()	How much independent information
trace()	Sum of diagonal
cond()	Stability of matrix


✔ You are DONE with NumPy Linear Algebra
✔ Nothing important left here


'''