import matplotlib.pyplot as plt
a=[1,2,3,4,5]
b=[2,4,6,8,10]
c=[3,5,7,9,11]
d=[1,4,2,5,7]
plt.scatter(a,b,color="blue",label="drone1")
plt.scatter(c,d,color="green",label="drone2")
plt.xlabel("x position")
plt.ylabel("y position")
plt.title("drone positions")
plt.legend()
plt.show()
'''
Color in scatter plot and its meaning

Color is used to distinguish different groups or categories.

Example use cases:
Different drones
Different objects
Different clusters
Blue dots and red dots represent different groups.
'''