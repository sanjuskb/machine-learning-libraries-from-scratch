'''
Shape is:
(1, 3, 4)


Meaning:

1 block (or depth)

3 rows

4 columns


2D array example
b = [
     [1,2,3,4],
     [1,2,3,4],
     [2,3,4,5]
    ]

in case of 2d arrays we dont have depth


Shape:

(3, 4)


Looks like:

[ 1  2  3  4 ]
[ 1  2  3  4 ]
[ 2  3  4  5 ]

3D array example (your case)

Shape:

(1, 3, 4)


Looks like:

Block 1:
[ 1  2  3  4 ]
[ 1  2  3  4 ]
[ 2  3  4  5 ]


➡️ Same matrix, but wrapped inside an extra dimension

p2 = np.array([
    [
        [1,2,3,4],
        [1,2,3,4],
        [2,3,4,5]
    ],
    [
        [1,2,3,4],
        [1,2,3,4],
        [2,3,4,5]
    ]
])

print(p2)
print(p2.shape)
'''
