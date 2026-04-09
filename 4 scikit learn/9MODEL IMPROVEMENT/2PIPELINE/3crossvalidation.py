'''
LAYER 5: MODEL IMPROVEMENT
TOPIC: CROSS-VALIDATION

PART 1: WHAT IT IS AND WHY TRAIN-TEST SPLIT IS NOT ENOUGH

Only understanding first.
No code yet.
No mixing.

1. FIRST: WHAT YOU ARE DOING RIGHT NOW

Until now, you do this:

split data once

train on training data

test on test data

get one score

This looks correct.
But there is a hidden problem.

2. THE REAL PROBLEM WITH A SINGLE TRAIN-TEST SPLIT

When you do:

train_test_split(random_state = 42)

the result depends on:

which rows go into training

which rows go into testing

If you change the random_state:

training data changes

test data changes

score changes

So the question is:

👉 Is the model really good
OR
👉 Did it just get a lucky split?

One split is not reliable.

3. SIMPLE HUMAN EXAMPLE (VERY IMPORTANT)

Imagine you are judging a student.

You give only one exam.

If the exam is easy:

student looks smart

If the exam is hard:

student looks weak

Is that fair?

No.

You need multiple exams.

That is exactly what cross-validation does.

4. WHAT CROSS-VALIDATION REALLY MEANS
Simple definition

Cross-validation means:

Train and test the model multiple times
on different parts of the data
and look at the overall performance.

So instead of one split, you use many splits.

5. K-FOLD CROSS-VALIDATION (THE STANDARD WAY)

This is the most common type.

What “K-Fold” means

You divide the data into K equal parts

Each part is called a fold

Example:
K = 5
→ data is divided into 5 folds

6. HOW K-FOLD WORKS (STEP BY STEP)

Suppose you have 10 data points
and K = 5.

Each fold has 2 points.

Now do this:

Round 1

Fold 1 → test

Fold 2–5 → train

Round 2

Fold 2 → test

Fold 1,3,4,5 → train

Round 3

Fold 3 → test

others → train

Round 4

Fold 4 → test

Round 5

Fold 5 → test

So:

every data point is tested exactly once

model is trained multiple times

7. WHAT YOU GET AT THE END

You do NOT get one score.

You get:

score 1

score 2

score 3

score 4

score 5

Then you usually take:

the average score

That average is much more reliable.

8. WHY THIS IS BETTER THAN ONE SPLIT

Cross-validation:

reduces luck factor

uses all data efficiently

gives stable performance estimate

reveals model consistency

One split can lie.
Cross-validation rarely lies.

9. VERY IMPORTANT CLARITY

Cross-validation is:

NOT a new model

NOT a new algorithm

NOT used in final deployment

It is used to:

evaluate models

compare models

tune hyperparameters

10. CONNECT TO PIPELINE (IMPORTANT)

When using cross-validation:

preprocessing must happen inside each fold

scaler must be fit only on training part of each fold

This is WHY:
👉 Pipeline + Cross-Validation are used together.

ONE-LINE SUMMARY (LOCK THIS IN)

Cross-validation evaluates a model by training and testing it multiple times on different data splits to get a reliable performance estimate.

'''