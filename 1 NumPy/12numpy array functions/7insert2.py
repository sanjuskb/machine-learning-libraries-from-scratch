import numpy as np

#2d
var1 = np.array([[1,2,3],
                 [1,2,3]])

v1 = np.insert(var1, 2, [22,23,24], axis=0) #adding 2nd row
print(v1)

v1 = np.insert(var1, 2, [22,23], axis=1)#adding a column at 2nd index position of column
print(v1)


'''row\col	0	1	2
    0	    1	2	3
    1	    4	5	6

Row index → axis 0

Column index → axis 1

Step 2: What does axis=0 ACTUALLY mean?
axis = 0

👉 row index changes
👉 NumPy moves down rows

So operations happen row-wise

That’s why:

axis=0 → works on rows

inserting along axis=0 → adds a row

sum(axis=0) → sums column-wise

💡 Even though movement is vertical, the thing being added/processed is a ROW'''