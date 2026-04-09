import numpy as np
a = np.array([1, 2, 3, 4, 5])
rev=np.arange(len(a)-1,-1,-1)
print(a[rev])




'''rev = a[np.arange(len(a)-1, -1, -1)]
Assume:

python
Copy code
a = np.array([1, 2, 3, 4, 5])
1️⃣ First understand len(a)
python
Copy code
len(a) = 5
Indices of a are:

makefile
Copy code
index:  0   1   2   3   4
value:  1   2   3   4   5
2️⃣ Understand np.arange(len(a)-1, -1, -1)
Substitute numbers:

python
Copy code
np.arange(5-1, -1, -1)
np.arange(4, -1, -1)
Meaning of np.arange(start, stop, step)
start = 4
stop = -1 (❗ stop is NOT included)
step = -1

So NumPy generates:

csharp
Copy code
[4, 3, 2, 1, 0]
This is a reversed list of indices.

3️⃣ What does a[ [4,3,2,1,0] ] mean?
This is called fancy indexing.

NumPy reads:

“Give me elements of a at these positions, in this order.”

So:

Index	Value
a[4]	5
a[3]	4
a[2]	3
a[1]	2
a[0]	1

Collected in order:

python
Copy code
[5, 4, 3, 2, 1]
4️⃣ Put it all together
Step-by-step execution
python
Copy code
indices = np.arange(4, -1, -1)
# indices = [4, 3, 2, 1, 0]

rev = a[indices]
# rev = [5, 4, 3, 2, 1]
5️⃣ Why this works (deep idea)
NumPy allows arrays of indices

Order of indices = order of output

Negative step reverses index order

No slicing is used'''