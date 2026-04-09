import numpy as np
ae=np.empty(5)
print(ae)

'''
Why zeros appeared in your case

Possible reasons:

Python reused memory that was previously filled with zeros

OS gave fresh memory pages (often zeroed for safety)

Small array → higher chance of clean memory

Next time, it may show random values

'''
print()

#2D
print(np.empty((3,4)))
print()

#3D
print(np.empty((4,3,4)))