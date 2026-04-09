import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.xlim(1, 5)
plt.ylim(0, 12)

plt.xlabel("Time")
plt.ylabel("Distance")

plt.show()
#-------------------------------------------------------------------------

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.xticks([1, 2, 3, 4, 5])
plt.yticks([0, 2, 4, 6, 8, 10])

plt.xlabel("Time")
plt.ylabel("Distance")

plt.show()
'''
Axis ticks

Ticks are the numbers shown on the axis.

By default, matplotlib decides tick positions.
Sometimes they are not meaningful.

You can control ticks to improve readability.




Logic:
You choose exact points where numbers appear.
This avoids confusing or unnecessary ticks.

Axis labels clarity

Axis labels must describe the meaning of data.
Not variable names.
Not vague words.

Bad label:
x
y

Good label:
Time
Distance

Clear labels allow anyone to understand the graph
without asking questions.

Keeping axes consistent across plots

When comparing plots, axes must use the same scale.

If one plot uses a bigger scale,
comparison becomes misleading.

Example logic:
Two drones distance comparison
Both must use same y axis range

That is why axis limits and ticks
should be consistent when comparing plots.

Mental summary for axis control

Limits control range
Ticks control markings
Labels control meaning
Consistency controls fairness

'''