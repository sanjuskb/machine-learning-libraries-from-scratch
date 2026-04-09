import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

plt.plot(x, y)

plt.text(2, 5, "Mid point")
'''
What this means:
Text "Mid point" is written
at x equals 2
and y equals 5
'''

plt.xlabel("Time")
plt.ylabel("Distance")

plt.show()