'''
Labels for x and y axis

Until now, you saw a line but you do not know what it represents.

A graph without labels is meaningless.

x label tells what the x values represent
y label tells what the y values represent

Example meaning:
x can be time
y can be distance

Code example:

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel("Time")
plt.ylabel("Distance")
plt.show()


Now anyone seeing the graph knows:
x axis is Time
y axis is Distance

Title of a plot

Title tells what the entire graph is about.

Without title:
Viewer sees a graph but does not know the purpose.

With title:
Viewer immediately understands the idea.

Example:

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel("Time")
plt.ylabel("Distance")
plt.title("Distance vs Time")
plt.show()


Now the graph clearly says:
This plot shows Distance changing with Time.

Why labels and title are important

For ML:
You plot loss vs epochs
Without labels you do not know which axis is loss

For drones:
You plot position vs time
Without labels you cannot explain movement

Engineers always write plots so that:
Another person can understand without explanation.

This is professional plotting.

'''