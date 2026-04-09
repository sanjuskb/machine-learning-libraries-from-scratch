import numpy as np

var2 = np.array([1,2,3,4,5,6])
y = np.resize(var2, (3,2))
print(y)
print()
y = np.resize(var2, (3,3)) #even though 9 elements are not present it creates duplicates of elements to complete the matrix
print(y)


'''
using np.resize
var2 = np.array([1,2,3,4,5,6])
y = np.resize(var2, (3,2))
print(y)

What happens internally?

np.resize is forgiving

It forces the array into the given shape

If needed, it will:

repeat elements

or truncate elements

In your case:

Original elements = 6

Target shape = 3 × 2 = 6

So no repetition/truncation is needed.

Result:

[[1 2]
 [3 4]
 [5 6]]

Code 2️⃣ using reshape
y = [2,3,4,5,4,8]
x = np.array(y)
new = x.reshape(3,2)

What happens internally?

reshape is strict

It never changes data

It only reinterprets existing memory

Here:

Total elements = 6

Target shape = 3 × 2 = 6

So reshape is allowed.

Result:

[[2 3]
 [4 5]
 [4 8]]


Core difference (THIS IS THE KEY)

Aspect	               np.resize	                  reshape

Changes data?	✅    Can repeat or cut	            ❌ Never
Requires size match?	❌ No	                    ✅ Yes
Safe for logic?	      ⚠️ Dangerous	                 ✅ Safe
Common in ML	      ❌ Rare	                    ✅ Very common
'''