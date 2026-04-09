'''

1. What is savefig

savefig means:
Save the plot as an image file.

Instead of just seeing the graph on screen,
you store it on disk as a file.

This file can be:
Used in reports
Shared with others
Uploaded to GitHub
Inserted into documents

---

2. Why saving plots is important

In real work:
You do not recreate plots every time.

You generate once,
then reuse many times.

Saving plots is important for:
Assignments
Projects
Internship submissions
Debugging results

If you only use show:
Graph disappears after closing.

savefig makes it permanent.

---

3. Basic savefig syntax

Very simple rule:

savefig must be called
BEFORE show

Example code:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel("Time")
plt.ylabel("Distance")
plt.title("Distance vs Time")

plt.savefig("distance_plot.png")
plt.show()
```

What happens:
A file named distance_plot.png is created
in the same folder as your Python file.

---

Mental rule to remember

Create plot
Save plot
Show plot

---


'''
