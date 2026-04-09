'''
K-MEANS

PART 3
ELBOW METHOD (CHOOSING K)

1. THE PROBLEM ELBOW METHOD SOLVES (HUMAN LANGUAGE)

So far, you did this:

You chose K = 2

K-Means grouped the data

But here is the real question:

👉 How do we know K = 2 is correct?
👉 Why not K = 1, 3, 4, or 5?

The Elbow Method exists only to answer this question.

Nothing else.

2. WHAT K-MEANS IS TRYING TO MINIMIZE (CORE IDEA)

K-Means tries to make points inside a cluster close to their mean.

So it measures:

How far are points from their cluster mean?

This total distance is called within-cluster error
(in sklearn it is called inertia).

Human meaning of inertia

Small inertia → points are tightly grouped

Large inertia → points are scattered

Better clustering → lower inertia

3. IMPORTANT TRUTH (THIS MAKES ELBOW NECESSARY)

If you increase K:

clusters become smaller

points get closer to their means

inertia always decreases

So:

👉 inertia will always go down as K goes up
👉 but we don’t want K = number of points

So we look for a smart stopping point.

4. WHAT ELBOW METHOD ACTUALLY DOES

Very simple process:

Try different values of K

Compute inertia for each K

Plot K vs inertia

Look for a point where improvement slows down

That point is called the elbow.

5. SAME DATA AGAIN (NO NEW CONFUSION)

We use the same numbers:

2, 4, 5, 6, 18, 20, 22
'''

import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Data
X = np.array([[2], [4], [5], [6], [18], [20], [22]])

inertia_values = []

# Try K from 1 to 6
for k in range(1, 7):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X)
    inertia_values.append(kmeans.inertia_)

print("Inertia values:", inertia_values)

# Plot
plt.plot(range(1, 7), inertia_values, marker='o')
plt.xlabel("Number of clusters (K)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()


'''
7. WHAT IS HAPPENING INTERNALLY (STEP BY STEP)
Step 1

Loop runs with different K values:

K = 1, 2, 3, 4, 5, 6

Step 2

For each K:

K-Means clusters the data

calculates inertia

inertia is stored

Example output might look like:

K = 1 → inertia = very large
K = 2 → inertia = much smaller
K = 3 → inertia = slightly smaller
K = 4 → inertia = tiny improvement

8. WHAT THE GRAPH MEANS (THIS IS THE KEY)

On the graph:

X-axis → K (number of clusters)

Y-axis → inertia (error)

At first:

inertia drops sharply

Later:

inertia drops slowly

The point where the curve bends is the elbow.

9. WHY THAT POINT IS CHOSEN (LOGIC)

Before elbow:

adding clusters gives big improvement

After elbow:

adding clusters gives little benefit

So elbow = best balance between simplicity and accuracy

10. APPLY THIS TO OUR DATA

For this data:

2, 4, 5, 6, 18, 20, 22


You will see:

big drop from K = 1 to K = 2

small drop after K = 2

So:

👉 K = 2 is the right choice

Which matches what we saw manually.

11. VERY IMPORTANT LIMITATION (HONEST TRUTH)

Elbow method:

does NOT always give a clear elbow

sometimes curve is smooth

In such cases:

domain knowledge matters

try multiple K values

This is normal.

ONE-LINE SUMMARY (LOCK THIS IN)

The Elbow Method helps choose K by finding the point where increasing clusters stops giving significant improvement.
'''