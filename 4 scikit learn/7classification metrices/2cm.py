import numpy as np
from sklearn.metrics import confusion_matrix

# Actual results (ground truth)
y_test = np.array([1, 0, 1, 0, 1, 0])

# Model predictions
y_pred = np.array([1, 0, 0, 0, 1, 1])

# Create confusion matrix
cm = confusion_matrix(y_test, y_pred)

print("Confusion Matrix:")
print(cm)

'''
2. WHAT THIS DATA MEANS (HUMAN LANGUAGE)

We are checking 6 cases.

Let us write them side by side:

Index	Actual (y_test)	Predicted (y_pred)
0	1 (delayed)	1 (delayed)
1	0 (not delayed)	0 (not delayed)
2	1 (delayed)	0 (not delayed)
3	0 (not delayed)	0 (not delayed)
4	1 (delayed)	1 (delayed)
5	0 (not delayed)	1 (delayed)

This is all the information the confusion matrix uses.

3. WHAT confusion_matrix() DOES INTERNALLY (STEP BY STEP)

Internally, sklearn does something conceptually like this:

Step 1

Create four counters and set them to zero

TN = 0

FP = 0

FN = 0

TP = 0

Step 2

Go through each pair one by one

Case 0

Actual = 1, Predicted = 1
→ True Positive
TP = TP + 1

Case 1

Actual = 0, Predicted = 0
→ True Negative
TN = TN + 1

Case 2

Actual = 1, Predicted = 0
→ False Negative
FN = FN + 1

Case 3

Actual = 0, Predicted = 0
→ True Negative
TN = TN + 1

Case 4

Actual = 1, Predicted = 1
→ True Positive
TP = TP + 1

Case 5

Actual = 0, Predicted = 1
→ False Positive
FP = FP + 1

Step 3

Final counts become

TN = 2

FP = 1

FN = 1

TP = 2

4. HOW THESE NUMBERS ARE ARRANGED INTO A MATRIX

scikit-learn uses this fixed format:

[[TN  FP]
 [FN  TP]]


So values are placed like this:

[[2  1]
 [1  2]]


That is exactly what you see printed.

5. WHAT EACH NUMBER MEANS (VERY CLEAR)
[[2  1]
 [1  2]]

Top-left → 2

Actual 0, Predicted 0
Correct “not delayed” predictions

Top-right → 1

Actual 0, Predicted 1
False alarm (said delayed but was not)

Bottom-left → 1

Actual 1, Predicted 0
Missed delay (dangerous mistake)

Bottom-right → 2

Actual 1, Predicted 1
Correctly detected delay

6. WHY CONFUSION MATRIX IS SO IMPORTANT

Because it does not hide mistakes.

Accuracy just gives one number.
Confusion matrix tells what kind of mistakes happened.

From these four numbers, we later calculate:

Accuracy

Precision

Recall

F1-score

But nothing exists without this table.

7. ONE-SENTENCE CORE TRUTH

A confusion matrix is just a systematic count of how many predictions were right or wrong, broken down by type
'''