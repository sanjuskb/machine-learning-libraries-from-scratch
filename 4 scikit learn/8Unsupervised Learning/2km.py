'''
K-MEANS

PART 2
CODE + WHAT IS HAPPENING INTERNALLY

We will cluster this data:

2, 4, 5, 6, 18, 20, 22


We choose:

K = 2

1. COMPLETE CODE (RUN AS IT IS)
'''
import numpy as np
from sklearn.cluster import KMeans

# Data (must be 2D for sklearn)
X = np.array([[2], [4], [5], [6], [18], [20], [22]])

# Create KMeans object
kmeans = KMeans(n_clusters=2, random_state=42)

# Fit the model
kmeans.fit(X)

# Get cluster labels
labels = kmeans.labels_

# Get cluster centers
centers = kmeans.cluster_centers_

print("Data points:")
print(X.flatten())

print("\nCluster labels for each point:")
print(labels)

print("\nCluster centers:")
print(centers.flatten())

'''
2. WHY DATA IS WRITTEN LIKE [[2], [4], ...]
What you wrote logically:
2, 4, 5, 6, 18, 20, 22

What sklearn expects:
[[2],
 [4],
 [5],
 [6],
 [18],
 [20],
 [22]]


Reason:

• Each row = one data point
• Each column = one feature

Here:
• 7 data points
• 1 feature

That’s all.

3. WHAT THIS LINE DOES
kmeans = KMeans(n_clusters=2, random_state=42)

Internally meaning

You are telling sklearn:

• create a K-Means algorithm
• divide data into 2 groups
• random_state just fixes randomness

Nothing is calculated yet.

4. WHAT fit(X) REALLY DOES (THIS IS THE CORE)
kmeans.fit(X)


Internally, THIS EXACT LOGIC happens:

STEP 1 — INITIALIZE TWO MEANS (RANDOMLY)

Example (not fixed, but similar):

mean_1 = 4
mean_2 = 20


These are just starting guesses.

STEP 2 — ASSIGN EACH POINT TO NEAREST MEAN

Distance calculation (absolute difference):

Point	dist to 4	dist to 20	Assigned group
2	2	18	group 1
4	0	16	group 1
5	1	15	group 1
6	2	14	group 1
18	14	2	group 2
20	16	0	group 2
22	18	2	group 2

So groups become:

Group 1: 2, 4, 5, 6
Group 2: 18, 20, 22

STEP 3 — UPDATE MEANS (THIS IS “MEANS”)

Group 1 mean:

(2 + 4 + 5 + 6) / 4 = 4.25


Group 2 mean:

(18 + 20 + 22) / 3 = 20


Means updated.

STEP 4 — REPEAT AGAIN

Now K-Means again checks:

• do any points change group if we use new means?

Answer:
• NO

So algorithm stops.

This is called convergence.

5. WHAT labels_ MEANS
labels = kmeans.labels_


Example output:

[0 0 0 0 1 1 1]

Meaning (VERY IMPORTANT)

Each number corresponds to a data point.

2   → cluster 0
4   → cluster 0
5   → cluster 0
6   → cluster 0
18  → cluster 1
20  → cluster 1
22  → cluster 1


Cluster numbers:
• have NO meaning
• just identifiers

6. WHAT cluster_centers_ MEANS
centers = kmeans.cluster_centers_


Example output:

[ 4.25 20. ]


Meaning:

• cluster 0 average ≈ 4.25
• cluster 1 average ≈ 20

These are the final means.

7. WHAT DID WE ACHIEVE (NO THEORY)

Input:

2, 4, 5, 6, 18, 20, 22


Output:

Cluster 0 → small numbers
Cluster 1 → large numbers


Computer discovered this without being told what small or large means.

8. VERY IMPORTANT THINGS TO LOCK IN

• K-Means does NOT predict
• K-Means does NOT use labels
• K-Means only groups by similarity
• You must choose K
• Scaling matters because distance matters

ONE SENTENCE THAT SHOULD NOW MAKE SENSE

K-Means repeatedly assigns data points to the nearest group average and updates those averages until the groups stop changing.

'''