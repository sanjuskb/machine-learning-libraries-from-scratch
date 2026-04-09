# Iteration with index + value using np.ndenumerate()
import numpy as np

var3 = np.array([[[9, 8, 7, 6],
                  [1, 2, 3, 4]]])

print(var3)
print(var3.ndim)
print()

for index, value in np.ndenumerate(var3):
    print(index, value)

    '''
    What is np.ndenumerate?

np.ndenumerate = n-dimensional enumerate

Why was enumerate created?

Without enumerate, people used to do this 👇

arr = ['a', 'b', 'c']

i = 0
for value in arr:
    print(i, value)
    i += 1


This is:

messy ❌

error-prone ❌

So Python introduced enumerate ✅

3️⃣ Basic example of enumerate
arr = ['a', 'b', 'c']

for index, value in enumerate(arr):
    print(index, value)

Output:
0 a
1 b
2 c


✔ clean
✔ readable
✔ safe
    '''
