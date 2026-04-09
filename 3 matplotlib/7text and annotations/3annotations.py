import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

plt.plot(x, y)

plt.annotate(
    "Highest point",
    xy=(4, 8)
)

plt.xlabel("Time")
plt.ylabel("Distance")
plt.show()
'''
What is happening here:

The point (4, 8) already exists on the graph
Annotation text is linked to that point

Even without an arrow:
The annotation is logically attached to the point
-------------------------------------------------------------------------------------

Annotation syntax

Annotations are added using plt.annotate.

Basic idea:
You write some text
And you tell matplotlib which point it refers to

Basic syntax looks like this:

plt.annotate("text", xy=(x_value, y_value))


This means:
Write this text
And associate it with this point on the graph
---------------------------------------------------------------------------
Why annotations are powerful in engineering plots

Annotations allow you to explain events.

Examples:
Obstacle detected
Maximum error
Sudden spike
Goal reached

Instead of someone guessing:
You directly tell them what happened.

This is extremely important in:
Drone paths
ML training curves
Debugging plots

Mental summary

Text explains generally
Annotation explains specifically
Annotation always refers to a point
'''