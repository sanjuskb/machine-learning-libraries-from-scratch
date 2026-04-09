import numpy as np
'''
What does np.linspace() do?

linspace = linear spacing

It creates evenly spaced numbers between two values.

General form
np.linspace(start, stop, num)


start → first value

stop → last value (included)

num → total number of values you want

Step-by-step explanation of your example
np.linspace(1, 10, num=5)


You are saying:

“Give me 5 numbers, starting from 1, ending at 10, spaced equally.”

How are the numbers calculated?
Step size formula
step = (stop - start) / (num - 1)

'''

#1D
al=np.linspace(1,10,num=6)#it only gives linear 1D array
print(al)
print()

al=np.linspace(1,10,num=6).reshape(2,3) #we use reshape to change the dimension of the array
print(al)
print()

al=np.linspace(1,10,num=30).reshape(2,3,5)
print(al)
