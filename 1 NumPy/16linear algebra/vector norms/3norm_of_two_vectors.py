import numpy as np
A = np.array([1, 2])
B = np.array([4, 6])
dist = np.linalg.norm(B - A)
#distance = √((x2-x1)² + (y2-y1)²)
print(dist)