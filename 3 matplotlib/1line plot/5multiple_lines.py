import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[2,4,6,8,10]
z=[3,5,7,9,11]
plt.plot(x,y,color="blue",label="drone1")
plt.plot(x,z,color="yellow",label="drone2")
plt.xlabel("time")
plt.ylabel("distance")

plt.legend()
plt.show()
'''
Multiple lines in one plot

Sometimes one line is not enough.

Example cases:
Compare two drones
Compare training and validation loss
Compare expected vs actual values

You can draw more than one line on the same graph.
-------------------------------------------------------------------
Line colors and meaning

Colors help you distinguish lines.

By default matplotlib chooses colors automatically.
But you can set them when meaning matters.
---------------------------------------------------------------------
Use colors only when:
They represent different systems or models.

Do not use too many colors.
Clarity is more important than beauty.
------------------------------------------------------------------------
Legend and why it is needed

When multiple lines exist:
Viewer must know which line is which.

Legend explains that.

Legend tells:
Blue line is Drone A
Orange line is Drone B

This is mandatory in professional plots.
'''