import numpy as np

var = np.array([1, 2, 3, 4])

co = var.copy()

var[1] = 40

print("var : ", var)
print("copy : ", co)


x = np.array([9, 8, 7, 6, 5])

vi = x.view()

x[1] = 40

print("x : ", x)
print("view : ", vi)

'''
🔑 Output 
var :  [ 1 40  3  4]
copy : [1 2 3 4]

x :  [ 9 40  7  6  5]
view : [ 9 40  7  6  5]

🧠 Major Difference: copy() vs view()
 copy() → Independent data
co = var.copy()


Creates a new array

Stored in different memory

Changes in original do NOT affect copy

Think of it like:

Making a photocopy of a paper

You can write on the original, the photocopy stays the same.

 view() → Shared data (same memory)
vi = x.view()


Does NOT create new data

Points to the same memory

Changes in original DO affect the view

Think of it like:

Two people looking at the same paper from different angles

If one person writes on it, the other sees it.
'''
