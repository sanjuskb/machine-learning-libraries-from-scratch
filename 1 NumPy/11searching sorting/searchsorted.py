# np.searchsorted() — Finding insertion position
import numpy as np

var1 = np.array([1,2,3,4,9,10])
x1 = np.searchsorted(var1, [5,6,7], side="right")
print(x1)


'''
⚠️ Array must be sorted

What it does

Tells where a value should be inserted

So that array remains sorted

output:
[4 4 4]
Meaning
Values 5, 6, 7 should be inserted at index 4

------------------------------------------------------------------------------------

side="right"

Insert after existing values

"left" inserts before
ex:
[1, 2, 3, 4, 4, 4, 7]

Now we ask:

Where should I insert 4 ?

side="left" (insert BEFORE existing values)
Meaning in plain English

➡️ Insert before the first 4

1 2 3 | 4 4 4 7
        ↑
      index 3

side="right" (insert AFTER existing values)

Meaning in plain English

➡️ Insert after the last 4

1 2 3 4 4 4 | 7
             ↑
           index 6
'''