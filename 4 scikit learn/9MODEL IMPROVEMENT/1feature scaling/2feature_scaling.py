'''
FEATURE SCALING
PART 2: StandardScaler

(numbers → logic → code → what happens internally)

No mixing. No rushing.

1. WHAT StandardScaler DOES (ONE CLEAR LINE)

StandardScaler changes a feature so that:

its mean becomes 0

its spread becomes 1

That’s it.

2. WHY THIS IDEA EXISTS (HUMAN LANGUAGE)

Suppose you have this feature:

distance = [10, 20, 30, 40, 50]


Problems:

values are large

distance-based models will be dominated by this feature

Instead of caring about raw values,
we want to care about:

how far a value is from the average

That is exactly what StandardScaler does.

3. THE CORE IDEA (NO FORMULA YET)

StandardScaler asks this for every value:

Compared to the average,
is this value small, medium, or large?

And it expresses the answer in a standard unit.

4. NUMERIC EXAMPLE (STEP BY STEP)
Original data
distance = [10, 20, 30, 40, 50]

Step 1: Compute the mean
mean = (10 + 20 + 30 + 40 + 50) / 5
mean = 30

Step 2: Compute how spread out the data is

This is called standard deviation.

You do NOT need to memorize the formula.
Just understand what it represents:

average distance of values from the mean

For this data, standard deviation ≈ 14.14

Step 3: Transform each value

StandardScaler converts each value like this:

new_value = (value − mean) / standard_deviation


Let’s do a few manually.

For 10
(10 − 30) / 14.14 ≈ −1.41

For 30
(30 − 30) / 14.14 = 0

For 50
(50 − 30) / 14.14 ≈ +1.41

Final scaled values (approximately)
[-1.41, -0.71, 0, 0.71, 1.41]

5. WHAT THESE NUMBERS MEAN (VERY IMPORTANT)

negative → below average

zero → exactly average

positive → above average

And the size tells how far from average.

So StandardScaler does NOT destroy information.
It re-expresses it.

6. WHAT CHANGED AND WHAT DID NOT

Changed:

numeric scale

units

Not changed:

order of data

relative distances

meaning

'''

import numpy as np
from sklearn.preprocessing import StandardScaler

# Original data
X = np.array([
    [10],
    [20],
    [30],
    [40],
    [50]
])

print("Original data:")
print(X.flatten())

# Create scaler
scaler = StandardScaler()

# Fit and transform
X_scaled = scaler.fit_transform(X)

print("\nScaled data:")
print(X_scaled.flatten())


'''
8. WHAT fit_transform DOES INTERNALLY (IMPORTANT)

This line:

X_scaled = scaler.fit_transform(X)


does two things:

fit

computes mean

computes standard deviation

stores them inside scaler

transform

applies the formula

converts original values to scaled values

9. WHY THIS IS PERFECT FOR MANY MODELS

StandardScaler is ideal when:

data is roughly normally distributed

models use distance or gradients

Examples:

KNN

K-Means

PCA

Logistic Regression

Linear Regression (often)

10. ONE CRITICAL RULE (DO NOT FORGET)

In real ML pipelines:

fit scaler ONLY on training data

transform both train and test data

We will show this clearly with train_test_split later.

ONE-LINE SUMMARY (LOCK THIS IN)

StandardScaler transforms features so that they have mean 0 and standard deviation 1, making all features comparable

-------------------------------------------------------------------------------

In real ML pipelines:

fit scaler ONLY on training data

transform both train and test data

We will show this clearly with train_test_split:



We will answer one question only:

👉 Why do we fit only on training data
👉 and transform both training and test data

1. FIRST, WHAT “FIT” AND “TRANSFORM” REALLY MEAN
fit (learning step)

When you do:

scaler.fit(X)


the scaler learns statistics from the data:

mean

standard deviation (for StandardScaler)

min and max (for MinMaxScaler)

So fit = learning numbers from data

transform (application step)

When you do:

scaler.transform(X)


the scaler uses already learned numbers
to convert values.

So transform = applying the same rule

2. WHY TRAIN AND TEST DATA EXIST (HUMAN LOGIC)

You split data because:

training data = what the model is allowed to learn from

test data = data the model has NEVER seen

Test data simulates future unseen data.

If test data influences training in any way → cheating.

3. THE BIG MISTAKE WE MUST AVOID (THIS IS THE KEY)

If you do this:

scaler.fit(all_data)


then:

test data influences the mean and std

training process indirectly “sees” test data

This is called data leakage.

Data leakage gives fake good performance.

4. SIMPLE NUMERIC EXAMPLE (VERY IMPORTANT)
Suppose this is your full dataset
distance = [10, 20, 30, 1000]


Imagine:

10, 20, 30 are training data

1000 is test data (future unseen case)

WRONG WAY (fit on all data)

Mean of all data:

(10 + 20 + 30 + 1000) / 4 = 265


Now training values are scaled using future information (1000).

This is cheating.

CORRECT WAY (fit only on training data)

Training data:

[10, 20, 30]


Mean:

(10 + 20 + 30) / 3 = 20


Test data (1000) is scaled using training statistics only.

This simulates reality correctly.

5. STEP-BY-STEP CORRECT PIPELINE (LOGIC FIRST)
Step 1: Split data
X_train, X_test = train_test_split(X)


Now:

training data is isolated

test data is untouched

Step 2: Fit scaler ONLY on training data
scaler.fit(X_train)


Scaler learns:

mean of training data

std of training data

Step 3: Transform training data
X_train_scaled = scaler.transform(X_train)


Training data is converted using its own statistics.

Step 4: Transform test data USING SAME SCALER
X_test_scaled = scaler.transform(X_test)


Test data is converted using training statistics, not its own.

This is crucial.

6. WHY WE TRANSFORM TEST DATA AT ALL

You might ask:

Why not leave test data untouched?

Because:

model was trained on scaled values

test data must be in the same scale

otherwise model cannot compare correctly

So:

same scaling rule

same reference

fair evaluation

7. WHAT WOULD GO WRONG OTHERWISE

If you fit scaler separately on test data:

test mean will be different

test scale will be different

model sees inconsistent data

evaluation becomes meaningless

8. ONE REAL-LIFE ANALOGY (VERY SIMPLE)

Imagine measuring height.

You decide:

training data measured in meters

Now test data comes.

If you suddenly measure test data in centimeters:

comparison breaks

model gets confused

Scaling ensures same measurement system.

9. ONE SENTENCE THAT MUST STICK

Fit learns rules from training data only, and transform applies the same rules to both training and test data to avoid data leakage.

10. CHECK YOUR UNDERSTANDING (MENTAL TEST)

Answer this in your head:

Does test data influence scaler parameters? → NO

Do train and test use same scaling rule? → YES

If yes, you got it.

'''