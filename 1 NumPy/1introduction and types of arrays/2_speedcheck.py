import numpy as np
import time
start = time.time()
result = [j**4 for j in range(1,9)]
end = time.time()

print(end - start)
#we have %timeit function to check time directly in ipython or jupiter

start = time.time()
result = np.arange(1,9)**4
end = time.time()

print(end - start)

'''
For VERY SMALL data (1 to 8):

NumPy has overhead

creating array

allocating memory

That overhead > actual computation

So:
Python list looks faster for tiny inputs


in real ML / data science:

arrays are huge (lakhs, millions)

NumPy shines there 

in the above code  test size was too small to show the advantage.

 Simple takeaway (remember this)

 Small data → Python may be faster
 Large data → NumPy is much faster
 NumPy = speed + math + ML foundation
'''
