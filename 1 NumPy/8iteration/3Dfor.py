import numpy as np

var3 = np.array([[[9, 8, 7, 6],
                  [1, 2, 3, 4]],
                 [[3, 5, 3, 2],
                  [8 ,4 ,2 ,9]] ])

print(var3)
print(var3.ndim)
print()

#prints sub matrices in 3D
for i in var3:
    print(i)
    print()

#prints all rows 
for i in var3:
    for j in i:
        print(j)
        print()

#prints all elements
for i in var3:
    for j in i:
        for k in j:
            print(k)
            print()