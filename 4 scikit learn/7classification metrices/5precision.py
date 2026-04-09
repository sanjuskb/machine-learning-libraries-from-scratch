
'''
Docstring for 7classification metrices.5precision

PRECISION

(ONLY THIS TOPIC)

1. WHAT PRECISION MEANS (HUMAN LANGUAGE)

Precision answers this question:

When the model says “YES”, how often is it actually correct?

It does not care about all predictions.
It cares only about positive predictions.

2. WHY PRECISION EXISTS (INTUITION)

Imagine this situation:

Your model predicts:
“Delivery is delayed”

But many of those predictions are wrong.

That means:

unnecessary alerts

wasted resources

false alarms

Precision tells you how trustworthy a YES prediction is.

3. PRECISION FORMULA (REFERENCE ONLY)

Precision = True Positives / (True Positives + False Positives)

Meaning:
Correct YES predictions
divided by
all YES predictions

'''

import numpy as np
from sklearn.metrics import precision_score

# Actual values
y_test = np.array([1, 0, 1, 0, 1, 0])

# Predicted values
y_pred = np.array([1, 0, 0, 0, 1, 1])

# Calculate precision
precision = precision_score(y_test, y_pred)

print("Precision:", precision)
'''

5. WHAT HAPPENS INTERNALLY (STEP BY STEP)

The function precision_score does this internally.

Step 1

Identify all cases where model predicted 1 (YES)

From y_pred:

Index:     0  1  2  3  4  5
Predicted: 1  0  0  0  1  1


YES predictions at indices:

0

4

5

Total YES predictions = 3

Step 2

Check how many of these were actually correct

Look at y_test at those indices:

Index 0 → actual = 1 → correct YES

Index 4 → actual = 1 → correct YES

Index 5 → actual = 0 → wrong YES

So:

True Positives = 2
False Positives = 1

Step 3

Apply formula

Precision = TP / (TP + FP)
Precision = 2 / (2 + 1)
Precision = 2 / 3
Precision = 0.6666

So output is:

Precision: 0.6666666666666666

6. HOW THIS CONNECTS TO CONFUSION MATRIX

From confusion matrix:

TP = 2

FP = 1

Precision = TP / (TP + FP)
Precision = 2 / 3

Same result.

7. IMPORTANT REAL-WORLD MEANING

High precision means:

model rarely gives false alarms

YES predictions are reliable

Low precision means:

model says YES too often

many YES predictions are wrong

8. ONE-LINE SUMMARY (LOCK THIS)

Precision measures how many predicted positive cases were actually positive
'''