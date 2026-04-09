'''
Docstring for 7classification metrices.confusion_matrix

Classification Metrics.
I will cover ALL the topics you listed, but in the right logical order, because these metrics depend on each other.

Order (very important):

Confusion Matrix

Accuracy

Precision

Recall

F1-score

I will do for each metric:

machine learning meaning

human meaning

numeric example using real data

step by step calculation

No images in the middle. No shortcuts.

CLASSIFICATION METRICS

PART 1
CONFUSION MATRIX (FOUNDATION OF EVERYTHING)

1. WHAT IS A CONFUSION MATRIX
Machine learning explanation

A confusion matrix is a table that compares:

actual class (ground truth)

predicted class (model output)

It shows:

how many predictions were correct

how many were wrong

what type of mistake was made

For binary classification, it is a 2 × 2 table.

Human understanding explanation

Think of a confusion matrix as a report card for a classifier.

It does not just say:
“you got 80 percent”

It tells you:

how many YES you got right

how many NO you got wrong

what kind of mistakes you made

This is much more informative.

2. THE FOUR IMPORTANT TERMS (VERY IMPORTANT)

In binary classification we have four outcomes.

Let us define the problem clearly first.

Our example problem

Class meanings:

1 → delayed

0 → not delayed

CASE 1: True Positive (TP)

Actual = 1
Predicted = 1

Meaning:
Delivery was delayed
Model predicted delayed

This is a correct positive decision.

CASE 2: True Negative (TN)

Actual = 0
Predicted = 0

Meaning:
Delivery was not delayed
Model predicted not delayed

This is a correct negative decision.

CASE 3: False Positive (FP)

Actual = 0
Predicted = 1

Meaning:
Delivery was NOT delayed
Model predicted delayed

This is a false alarm.

CASE 4: False Negative (FN)

Actual = 1
Predicted = 0

Meaning:
Delivery WAS delayed
Model predicted not delayed

This is a missed detection.

3. CONFUSION MATRIX TABLE (CONCRETE)

Suppose we have 10 deliveries.

Actual vs Predicted results:

Actual: 1 1 1 1 0 0 0 0 0 0
Predicted: 1 1 0 0 1 0 0 0 1 0

Now count:

TP = 2
TN = 4
FP = 2
FN = 2

Confusion matrix looks like:

                Predicted
               1        0
Actual 1      TP=2     FN=2
Actual 0      FP=2     TN=4


This table is the confusion matrix.

Everything else comes from this.

4. WHY CONFUSION MATRIX IS SO IMPORTANT
Machine learning reason

Accuracy alone hides information.

Two models can have same accuracy
but very different mistake behavior.

Confusion matrix shows:

what kind of errors matter

where the model fails

Human reason

In real life:

false alarm might be acceptable

missing a real problem might be disastrous

Confusion matrix lets you see this difference.
'''