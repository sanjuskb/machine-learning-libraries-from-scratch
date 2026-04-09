import numpy as np

'''
Correct signature of np.eye
np.eye(N, M=None, k=0, dtype=float)

Meaning of each parameter

Parameter	Meaning
N	        number of rows
M	        number of columns (optional)
k	        diagonal index
dtype	    data type
-------------------------------------------------------------------------------------
What does np.eye(3) mean?

np.eye(n) creates an identity matrix of size n x n.

So here:

3 → 3 rows and 3 columns

Result → 3x3 identity matrix

output:
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]

-------------------------------------------------------------------------------------------

Now: what does k mean?

👉 k tells NumPy WHICH diagonal to put 1s on

Think of k as:

“How many steps should I shift the diagonal?”

. k = 0 → main diagonal
np.eye(3, 3, k=0)

[[1 0 0]
 [0 1 0]
 [0 0 1]]


🧠 No shift. Normal diagonal.

. k > 0 → above the main diagonal

Example: k = 1

np.eye(3, 3, k=1)

[[0 1 0]
 [0 0 1]
 [0 0 0]]


What happened?

The diagonal moved one step to the right

Visual idea:

Main diagonal:      Shifted right (k=1):
[1 . .]             [. 1 .]
[. 1 .]     →       [. . 1]
[. . 1]             [. . .]


📌 k = +1 → shift right by 1
📌 k = +2 → shift right by 2

. k < 0 → below the main diagonal

Example: k = -1

np.eye(3, 3, k=-1)

[[0 0 0]
 [1 0 0]
 [0 1 0]]


What happened?

The diagonal moved one step down

Visual idea:

Main diagonal:      Shifted down (k=-1):
[1 . .]             [. . .]
[. 1 .]     →       [1 . .]
[. . 1]             [. 1 .]


📌 k = -1 → shift down by 1
📌 k = -2 → shift down by 2

🧠 Simple mental rule (VERY IMPORTANT)

k = how far the diagonal moves from the main one

k value	Meaning	Direction
0	main diagonal	no move
+1	above diagonal	right
+2	further above	more right
-1	below diagonal	down
-2	further below	more down

-------------------------------------------------------------------------------------


'''
ad=np.eye(3)
print(ad)
print()


ad1=np.eye(3,5)
print(ad1)
print()

# output

# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]]
#------------------------------------------------------------------

ad1=np.eye(5,k=-1)#in each row ones shifts to left
print(ad1)
print()

ad1=np.eye(5,k=1)#in each row ones shift to right
print(ad1)
print()
#-------------------------------------------------------------------
# ad1=np.eye(2,3,5) does not work
# print(ad1) 
'''
np.eye() works ONLY for 2D arrays.
It cannot create 3D (or higher) arrays.

 Why np.eye() is limited to 2D
What np.eye() is meant for

np.eye() creates an identity matrix.

An identity matrix is defined only in 2D:
'''
