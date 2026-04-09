'''
Docstring for 6CLASSIFICATION.1Logistic Regression.5feature_scaling
KNN

PART 5
FEATURE SCALING
WHY KNN BREAKS WITHOUT IT

SUBTOPIC

WHY FEATURE SCALING IS NOT OPTIONAL IN KNN

1. MACHINE LEARNING TERMINOLOGY EXPLANATION

KNN uses distance to decide neighbors.

Distance is computed using feature values directly.

If features are on different scales,
the feature with larger numeric values dominates the distance.

This causes the model to:

ignore important features

make incorrect neighbor choices

Feature scaling fixes this by:

bringing all features to a similar numeric range

2. HUMAN UNDERSTANDING EXPLANATION

Think of distance like comparing people using two things:

height in centimeters

weight in kilograms

Height values are around 150 to 180
Weight values are around 50 to 80

Now imagine comparing:

height in centimeters

salary in rupees

Salary could be 30000, 50000, 100000

Salary numbers are huge.

So when you measure “distance”:

salary dominates

height becomes almost useless

That is exactly what happens in KNN without scaling.

3. REAL DATA EXAMPLE (VERY IMPORTANT)

Suppose we now have two features.

Distance (km)
Battery (%)

And target is delayed.

Training data

Distance Battery Delayed
5 90 0
10 80 0
20 40 1
30 20 1

4. TEST INPUT

Distance = 18
Battery = 50

We want to find nearest neighbors.

5. DISTANCE CALCULATION WITHOUT SCALING (PROBLEM)

Let us compute distance using both features.

Distance formula (simplified):

difference in distance
difference in battery

Compare with first training point (5, 90)

Distance difference = |18 − 5| = 13
Battery difference = |50 − 90| = 40

Battery difference is much larger.

Compare with second training point (10, 80)

Distance difference = 8
Battery difference = 30

Again battery dominates.

What happens logically

Even if distance is very close,
battery difference dominates the distance calculation.

So KNN decisions are mostly based on battery,
even if distance is more important.

This is WRONG behavior.

6. WHAT FEATURE SCALING DOES (CORE IDEA)

Feature scaling changes numbers so that:

distance feature

battery feature

are on similar numeric ranges

So neither dominates unfairly.

Scaling does NOT change:

relationships

order

meaning

It only changes units.

7. STANDARD SCALING (MOST COMMON)
Machine learning explanation

StandardScaler transforms data using:

scaled_value = (value − mean) / standard_deviation

After scaling:

mean becomes 0

values are around −1 to +1

Human explanation

Standard scaling answers this:

“How far is this value from average?”

Instead of using raw numbers,
we use relative position.

This makes features comparable.

8. NUMERIC EXAMPLE OF SCALING

Battery values:
90, 80, 40, 20

Mean ≈ 57.5

Battery = 90

Scaled battery = (90 − 57.5) / std
This becomes a small number like 1.2

Battery = 20

Scaled battery becomes −1.3

Now battery values are comparable to distance values.

9. KNN AFTER SCALING (WHAT CHANGES)

After scaling:

distance and battery both influence distance

nearest neighbors make sense

model decisions improve drastically

This is why scaling is mandatory for KNN.
'''