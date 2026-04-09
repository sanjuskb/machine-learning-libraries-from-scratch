
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Create data
X = np.array([[10], [20], [30], [40], [50], [60]])

print("Original data:")
print(X.flatten())

# Step 1: split data
X_train, X_test = train_test_split(X, test_size=0.33, random_state=42)

print("\nTraining data:")
print(X_train.flatten())

print("\nTest data:")
print(X_test.flatten())

# Step 2: create scaler
scaler = StandardScaler()

# Step 3: fit scaler ONLY on training data
scaler.fit(X_train)

# Step 4: transform training data
X_train_scaled = scaler.transform(X_train)

# Step 5: transform test data using SAME scaler
X_test_scaled = scaler.transform(X_test)

print("\nScaled training data:")
print(X_train_scaled.flatten())

print("\nScaled test data:")
print(X_test_scaled.flatten())


'''
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