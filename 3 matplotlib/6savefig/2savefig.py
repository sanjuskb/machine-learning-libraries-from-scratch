import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
plt.xlabel("Time")
plt.ylabel("Distance")
plt.title("Distance vs Time")

plt.savefig("C:\\Users\\sanju\\OneDrive\\Desktop\\ml libraries\\3 matplotlib\\6savefig/distance_plot.pdf",dpi=300)
plt.show()

'''
Docstring for 6savefig.3savefig
Good 👍
Continuing step by step.

---

Topic 6: Savefig
Part 2

We will cover only these 3 sub topics:

1. File formats and when to use them
2. DPI and image quality
3. Saving to a specific folder



1. File formats and when to use them

savefig allows different file formats.

Common ones you will use:

PNG
Best for screenshots, reports, GitHub
Most commonly used

JPG
Smaller size
Not ideal for plots with text

PDF
Best for documents and printing
Keeps vector quality

SVG
Best for web and scaling
Used in professional reports

Example usage:

```python
plt.savefig("plot.png")
plt.savefig("plot.pdf")
```

Same plot, different formats.

---

2. DPI and image quality

DPI means dots per inch.

Higher DPI:
Sharper image
Larger file size

Lower DPI:
Blurrier image
Smaller file size

Default DPI is usually fine,
but for reports you should increase it.

Example:

```python
plt.savefig("plot_high_quality.png", dpi=300)
```

Use cases:
DPI 100 for normal use
DPI 300 for reports and submissions

---

3. Saving to a specific folder

If you want to organize your project,
save plots into a folder.

Example:

```python
plt.savefig("plots/distance_plot.png")
```

Important rules:
The folder must already exist
Otherwise Python will give an error

Typical project structure:
plots folder for images
code folder for Python files

---

Mental summary for savefig

Format decides usage
DPI decides clarity
Path decides organization

---


'''