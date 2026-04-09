'''
PCA

PART 3
CODE + WHAT IS HAPPENING INTERNALLY

1. THE SAME DATA AGAIN (NO NEW CONFUSION)

We reuse the 2D data you already understood:

(distance , time)

(1 , 2)
(2 , 4)
(3 , 6)
(4 , 8)
(5 , 10)


Distance and time grow together.
So PCA should reduce 2 features → 1 feature.
'''

import numpy as np
from sklearn.decomposition import PCA

# Original data (2 features)
X = np.array([
    [1, 2],
    [2, 4],
    [3, 6],
    [4, 8],
    [5, 10]
])

print("Original data:")
print(X)

# Create PCA object (reduce to 1 dimension)
pca = PCA(n_components=1)

# Apply PCA
X_reduced = pca.fit_transform(X)

print("\nData after PCA (1D):")
print(X_reduced)
print("\nExplained variance ratio:")
print(pca.explained_variance_ratio_)

'''
3. WHY DATA IS WRITTEN LIKE THIS
X = [
 [1, 2],
 [2, 4],
 [3, 6],
 [4, 8],
 [5, 10]
]


Meaning:

• each row = one data point
• first column = distance
• second column = time

So:
• 5 data points
• 2 features

4. WHAT THIS LINE MEANS
pca = PCA(n_components=1)


You are telling sklearn:

“I want to compress my data
from 2 features down to 1 feature.”

Nothing is computed yet.

5. WHAT fit_transform(X) DOES (THIS IS THE CORE)
X_reduced = pca.fit_transform(X)


This line does two things internally.

STEP 1 — fit (LEARNING THE DIRECTION)

PCA looks at the data and asks:

• In which direction does the data vary the most?

For your data, it finds:

• distance and time increase together
• main variation is along the diagonal direction

This direction becomes the principal component.

STEP 2 — transform (PROJECTING DATA)

Now PCA does this:

• it projects every 2D point
• onto the single principal direction

So each point becomes one number.

6. WHAT OUTPUT LOOKS LIKE (IMPORTANT)

Example output (values may differ slightly):

Data after PCA (1D):
[[-3.162]
 [-1.581]
 [ 0.000]
 [ 1.581]
 [ 3.162]]


Do NOT panic about numbers.

7. WHAT THESE NUMBERS MEAN (HUMAN LANGUAGE)

Originally:

(1,2) (2,4) (3,6) (4,8) (5,10)


After PCA:

[-3.16, -1.58, 0, 1.58, 3.16]


Meaning:

• ordering is preserved
• relative distances are preserved
• information is preserved

But now:
• only 1 feature instead of 2

8. VERY IMPORTANT CHECK (ORDER PRESERVATION)

Before PCA:

1 < 2 < 3 < 4 < 5


After PCA:

-3.16 < -1.58 < 0 < 1.58 < 3.16


Same ordering.

So PCA did not distort the structure.

9. WHAT PCA REMOVED

PCA removed:

• the direction with very little variation
• redundancy between distance and time

That direction contained almost no new information.

10. CHECK HOW MUCH INFORMATION WAS KEPT

Add this code:

print("\nExplained variance ratio:")
print(pca.explained_variance_ratio_)


Output will be close to:

[1.0]


Meaning:

• almost 100 percent information kept
• nothing important lost

11. IMPORTANT RULE (LOCK THIS IN)

• PCA changes feature space
• PCA does NOT change number of data points
• PCA does NOT use labels
• PCA is used BEFORE ML models

12. CONNECT BACK TO YOUR ROADMAP

You now completed:

LAYER 4
• K-Means clustering
• Elbow method
• PCA (concept + numbers + code)
----------------------------------------------------------------------------------------------------

Your output was:

[[-4.47213595]
 [-2.23606798]
 [ 0.        ]
 [ 2.23606798]
 [ 4.47213595]]


We will decode this completely.

1. WHAT THESE NUMBERS ARE (BIG PICTURE)

Each number is the new 1D coordinate of an original 2D point after PCA.

Originally your data was:

(distance, time)

(1, 2)
(2, 4)
(3, 6)
(4, 8)
(5, 10)


After PCA:

each point is no longer written as (distance, time)

each point is written as one number

that number tells where the point lies along the main direction of the data

So PCA did not predict anything.
It only re-expressed the same data in a smarter way.

2. WHY THESE NUMBERS ARE POSITIVE, NEGATIVE, AND ZERO

This is very important.

PCA creates a new axis (a new number line).

On that axis:

the center of the data becomes 0

points on one side become negative

points on the other side become positive

So:

(3, 6) → 0


because it is the middle of your data.

Everything else is measured relative to this center.

3. STEP 1 INTERNALLY: CENTERING THE DATA

Before PCA does anything, it centers the data.

Compute the mean of each column

Mean distance:

(1 + 2 + 3 + 4 + 5) / 5 = 3


Mean time:

(2 + 4 + 6 + 8 + 10) / 5 = 6


So the data center is:

(3, 6)

Subtract the mean from every point

This shifts the data so that the center is at (0, 0).

(1,2)  → (-2, -4)
(2,4)  → (-1, -2)
(3,6)  → ( 0,  0)
(4,8)  → ( 1,  2)
(5,10) → ( 2,  4)


This step is mandatory in PCA.

4. STEP 2 INTERNALLY: FINDING THE MAIN DIRECTION

Now PCA asks:

In which direction does the data spread the most?

Looking at these centered points:

(-2,-4), (-1,-2), (0,0), (1,2), (2,4)


You can clearly see:

when x increases by 1

y increases by 2

So the main direction is roughly:

(1, 2)


That direction becomes the principal component direction.

PCA then normalizes it (makes its length = 1):

principal_direction ≈ (0.447, 0.894)


You do NOT need to memorize this.
Just know PCA finds this direction automatically.

5. STEP 3 INTERNALLY: PROJECTING POINTS ONTO THAT DIRECTION

Now comes the key step.

Each centered point is projected onto the principal direction.

Think of it like this (human logic):

“How far has this point moved along the main direction of the data?”

That distance becomes the new PCA value.

Example: point (1,2)

Centered version:

(-2, -4)


Projection length (simplified idea):

distance_along_direction ≈ length of (-2, -4)


Length:

sqrt( (-2)^2 + (-4)^2 )
= sqrt(4 + 16)
= sqrt(20)
≈ 4.472


Since it lies before the center, PCA gives it a negative sign:

-4.472


That is your first number.

Example: point (2,4)

Centered:

(-1, -2)


Length:

sqrt(1 + 4) = sqrt(5) ≈ 2.236


Again before the center:

-2.236

Middle point (3,6)

Centered:

(0,0)


Projection:

0

Point (4,8)

Centered:

(1,2)


Length:

sqrt(1 + 4) = 2.236


After the center:

+2.236

Point (5,10)

Centered:

(2,4)


Length:

sqrt(4 + 16) = sqrt(20) ≈ 4.472


After the center:

+4.472

6. PUTTING IT ALL TOGETHER

That is why your output is:

[[-4.47213595]
 [-2.23606798]
 [ 0.        ]
 [ 2.23606798]
 [ 4.47213595]]


Each number means:

how far this data point lies along the most important direction of the data

7. VERY IMPORTANT CLARITY (THIS IS KEY)

These numbers:

are NOT predictions

are NOT distances in original units

are coordinates in a new feature space

preserve ordering and relative spacing

That is why:

(1,2) < (2,4) < (3,6) < (4,8) < (5,10)


becomes:

-4.47 < -2.23 < 0 < 2.23 < 4.47


Same structure, fewer dimensions.

8. ONE FINAL SENTENCE (LOCK THIS IN)

Each PCA number tells how far a data point lies along the main direction of variation after centering the data.
'''