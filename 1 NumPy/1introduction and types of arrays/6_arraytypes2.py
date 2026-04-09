import numpy as np

#3D array
p=np.array([[[1,2,3,4],[1,2,3,4],[2,3,4,5]]])
print(p)
print(p.ndim)


p2 = np.array([
    [
        [1,2,3],
        [1,2,3],
        [2,3,4]
    ],
    [
        [1,2,3],
        [1,2,3],
        [2,3,4]
    ],
    [   [1,2,3],
        [1,2,3],
        [2,3,4]
    ]
])

#it is like a rubics cube with 3 layers

print(p2)
print(p2.shape)
print(p2.ndim)

#n dimensional array
q=np.array([1,2,3,4],ndmin=20)
print(q)
print(q.ndim)