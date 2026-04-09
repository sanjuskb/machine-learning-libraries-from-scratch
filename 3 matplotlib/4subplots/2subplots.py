import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [2, 4, 6, 8]
y2 = [1, 3, 5, 7]

plt.subplot( 1,2, 1)
plt.plot(x, y1)
plt.title("Plot 1")
# plt.subplot(1,2,1) it means plotting the two lines on single graph
plt.subplot( 1,2, 2)
plt.plot(x, y2,color="red")
plt.title("Plot 2")
plt.show()
