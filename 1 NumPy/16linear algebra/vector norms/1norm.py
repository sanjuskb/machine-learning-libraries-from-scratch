import numpy as np
v=np.array([3,4])
print(np.linalg.norm(v)) #gives magnitude of the vector

v1=np.array([[3,4,2],[1,4,6]])
print(np.linalg.norm(v1))
print(np.linalg.norm(v1,axis=0))#column
print(np.linalg.norm(v1,axis=1))#row

unitvector=v/np.linalg.norm(v) #the magnitude of the output vector will be 1
print(unitvector) 
'''
What is a norm?
👉 Norm = length of the arrow
Like measuring the length of a stick.
For [3,4], the length is:


√(3² + 4²) = √25 = 5
So:

np.linalg.norm([3,4])
gives:

5

PART 3: What are these ord values?
Different ways to measure “length”.
1: ord=2 → Euclidean distance (NORMAL length)

np.linalg.norm(v, ord=2)
Meaning:
Straight-line distance
(the one you learn in school)
Used in:
ML
AI
Physics
Robotics
✅ This is the default and MOST IMPORTANT
2: ord=1 → Manhattan distance

np.linalg.norm(v, ord=1)
Formula:


|3| + |4| = 7
Analogy: 🚕 Like moving only right or up, no diagonal
Used in:
Some ML optimization problems
3: ord = np.inf → Maximum value

np.linalg.norm(v, ord=np.inf)
Result:


max(|3|, |4|) = 4
Meaning:
Only care about the largest component
Used:
Rarely
Some constraint problems

---------------------------------------------------------------------------------
Normalizing a Vector (MOST IMPORTANT)
What does “normalize” mean?
👉 Make the vector length = 1,
👉 but direction stays same
Example
v = np.array([3, 4])
Length:

np.linalg.norm(v) = 5
Now divide every value by 5:

v_unit = v / 5
So:
v_unit = [3/5, 4/5] = [0.6, 0.8]
Check its length:

np.linalg.norm(v_unit)
Result:

1.0
✔ Length = 1
✔ Direction = same (still pointing where [3,4] was)

------------------------------------------------------------------------------------

Norm of a 2D array (matrix) — DEFAULT behavior

A = np.array([[1, 2],
              [3, 4]])

np.linalg.norm(A)
👉 NumPy uses Frobenius norm
👉 It behaves as if all elements are considered together
Calculation:


√(1² + 2² + 3² + 4²)
⚠️ Important:
NumPy does NOT literally flatten
It mathematically treats all elements together
So conceptually it feels like flattening, but internally it’s a matrix norm, not a vector norm.
 Case 3: Norm along rows or columns (NO flattening)
You control this using axis
🔹 Row-wise norm

np.linalg.norm(A, axis=1)
Each row treated as a vector:


Row 1 → √(1² + 2²)
Row 2 → √(3² + 4²)
🔹 Column-wise norm

np.linalg.norm(A, axis=0)
'''