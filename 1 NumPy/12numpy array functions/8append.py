'''
np.append() does NOT modify the original array
It creates a NEW array (just like insert).

'''
import numpy as np
var = np.array([1, 2, 3, 4])
x = np.append(var, 6.5)
x1 = np.append(var, 6)
print(x) # floating numbers can be accesed as float is appended entire numbers in the output will be float

print(x1) # integer 6 is appended so output will be in int

#2d
var1 = np.array([[1,2,3],
                 [1,2,3]])
v1 = np.append(var1, [[45,44,23]], axis=0) #appends a new row at the end ,,,, [[45,44,23]]->one row 3 columns
v2 = np.append(var1, [[45],[44]], axis=1) #appends a new column at the end,,,[[45],[44]]->2 rows 1 column
print(v1)
print(v2)

'''
Why np.insert() and np.append() feel different

insert	Any index	
append	Only end	

👉 append = always at end
👉 insert = anywhere
'''
