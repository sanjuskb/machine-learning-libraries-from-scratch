'''
Docstring for 7text and annotations.1theory

Good 👍
Moving forward to the **next core topic**.

---

Topic 7: Text and Annotations
Part 1

We will cover only these 3 sub topics:

1. What text and annotations are
2. Difference between text and annotation
3. Basic text syntax



---

1. What are text and annotations

Text and annotations are used to **write information directly on the graph**.

They help you:
Explain what is happening
Highlight important points
Guide the viewer’s attention

Without text:
Graph shows data
But meaning may be unclear

With text:
Graph explains itself

---

2. Difference between text and annotation

Text:
Just writes words at a fixed position

Annotation:
Writes text AND points to something specific

So:
Text is passive
Annotation is directional

Use text when:
You want to label a region

Use annotation when:
You want to point to a point or event

---

3. Basic text syntax

Text is added using plt.text

Example:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

plt.plot(x, y)

plt.text(2, 5, "Mid point")

plt.xlabel("Time")
plt.ylabel("Distance")

plt.show()
```

What this means:
Text "Mid point" is written
at x equals 2
and y equals 5

It does NOT point to anything.
It just sits there.

---

Mental model

Text is like writing a note on the graph
Annotation is like drawing an arrow to something

---



'''