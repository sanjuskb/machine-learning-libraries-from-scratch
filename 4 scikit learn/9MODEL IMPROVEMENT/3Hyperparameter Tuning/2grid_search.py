'''
Perfect. Now we move to **Hyperparameter Tuning – PART 3**.

This time:

* full **working code**
* **line by line**
* **what happens internally**
* no skipping
* no extra topics

Only **GridSearchCV**.

---

# GRIDSEARCHCV

PART 3: COMPLETE CODE + INTERNAL WORKING

---

## 1. PROBLEM SETUP (VERY SIMPLE, VERY CLEAR)

We will use **KNN**, because:

* it has a clear hyperparameter `k`
* tuning effect is easy to understand

Data:

```
X = distance
y = class (0 or 1)
```

---

## 2. COMPLETE WORKING CODE (RUN AS IS)

'''
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

# Create data
X = np.array([[1], [2], [3], [8], [9], [10]])
y = np.array([0, 0, 0, 1, 1, 1])

# Create model (no hyperparameters fixed yet)
model = KNeighborsClassifier()

# Hyperparameter grid
param_grid = {
    "n_neighbors": [1, 3, 5] #values of k(how the data should be grouped)
}

# Create GridSearchCV
grid = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=3
)

# Run grid search
grid.fit(X, y)

# Results
print("Best hyperparameter:", grid.best_params_)
print("Best cross-validation score:", grid.best_score_)

'''
---

## 3. LINE BY LINE EXPLANATION (NO ASSUMPTIONS)

---

### Step 1: Create the model

```python
model = KNeighborsClassifier()
```

Important:

* model is NOT trained
* no value for `n_neighbors` chosen yet
* this is just a template

---

### Step 2: Create hyperparameter grid

```python
param_grid = {
    "n_neighbors": [1, 3, 5]
}
```

Meaning:

Try these values:

* k = 1
* k = 3
* k = 5

GridSearchCV will try **all of them**.

---

### Step 3: Create GridSearchCV object

```python
grid = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=3
)
```

This means:

* estimator → which model to tune
* param_grid → what values to try
* cv = 3 → use 3 fold cross validation

At this point:

* no training has happened yet

---

## 4. WHAT HAPPENS DURING `grid.fit(X, y)` (THIS IS THE CORE)

This ONE line:

```python
grid.fit(X, y)
```

does a LOT internally.

Let’s break it down.

---

## 5. INTERNAL STEP BY STEP (VERY IMPORTANT)

### Hyperparameter combinations

Only one hyperparameter:

```
n_neighbors = [1, 3, 5]
```

So combinations are:

* k = 1
* k = 3
* k = 5

---

### For EACH k value, GridSearchCV does:

#### Step A: Split data into 3 folds (cv = 3)

Example (conceptual):

* fold 1 test, fold 2+3 train
* fold 2 test, fold 1+3 train
* fold 3 test, fold 1+2 train

---

#### Step B: Train and test model 3 times

For k = 1:

```
train model (k=1) → test → score_1
train model (k=1) → test → score_2
train model (k=1) → test → score_3
```

Average these scores.

---

#### Step C: Repeat for k = 3 and k = 5

So total model trainings:

```
3 k values × 3 folds = 9 trainings

(
PART A
Why we do
3 k values × 3 folds = 9 trainings
and what exactly happens in each iteration

PART B
If we are giving k values ourselves, how can the model ever be “perfect”
Is GridSearchCV checking everything or only what we give?

No code. Only logic and clarity.

PART A

WHY 1 × 3, 3 × 3, 5 × 3
AND WHAT EXACTLY HAPPENS INSIDE

Step 1: Understand the two independent loops

GridSearchCV has two nested loops:

Loop over hyperparameter values (k values)

Loop over cross-validation folds (cv)

These are independent.

Think of it like:

“For each hyperparameter choice
  test it across multiple data splits”

Step 2: Your specific case

You gave:

param_grid = {
    "n_neighbors": [1, 3, 5]
}

cv = 3


So:

• number of hyperparameter choices = 3
• number of folds per choice = 3

That’s where 3 × 3 comes from.

Step 3: Let’s simulate EVERYTHING step by step

Your full dataset:

Index   X    y
0       1    0
1       2    0
2       3    0
3       8    1
4       9    1
5      10    1


cv = 3
So sklearn divides data into 3 folds (conceptually):

Fold A

[1, 2]


Fold B

[3, 8]


Fold C

[9, 10]


Now we begin.

Step 4: First hyperparameter choice
k = 1

Now GridSearchCV says:

“Let me test k = 1 robustly.”

That means: test it on all folds.

Iteration 1.1

Test on Fold A
Train on Fold B + Fold C

• train model with k = 1
• test on Fold A
• compute score → score_1

Iteration 1.2

Test on Fold B
Train on Fold A + Fold C

• train model with k = 1
• test on Fold B
• compute score → score_2

Iteration 1.3

Test on Fold C
Train on Fold A + Fold B

• train model with k = 1
• test on Fold C
• compute score → score_3

Now for k = 1

GridSearchCV computes:

average_score_k1 = (score_1 + score_2 + score_3) / 3


This answers:

“Does k = 1 work consistently, or only sometimes?”

Step 5: Second hyperparameter choice
k = 3

Everything repeats from scratch.

New model each time.

Iteration 2.1

k = 3
test Fold A
train Fold B + Fold C

Iteration 2.2

k = 3
test Fold B
train Fold A + Fold C

Iteration 2.3

k = 3
test Fold C
train Fold A + Fold B

Compute:

average_score_k3

Step 6: Third hyperparameter choice
k = 5

Again, full repetition.

Iteration 3.1
Iteration 3.2
Iteration 3.3

Compute:

average_score_k5

Step 7: Why this MUST be done

If we tested k = 1 on only one fold, the score might be:

• lucky
• unlucky
• misleading

By testing across all folds, we ensure:

• stability
• reliability
• robustness

That is why:

number of trainings = 
number of k values × number of folds


So yes:

3 × 3 = 9 trainings


And ALL are necessary.

)
```

You only wrote **one line**, sklearn did 9 trainings.

---

## 6. HOW GRIDSEARCHCV DECIDES THE BEST ONE

After all runs:

* it compares average scores
* selects the k with highest average score

That is stored as:

```python
grid.best_params_
grid.best_score_
```

---

## 7. WHAT `best_params_` MEANS

Example output:

```
{'n_neighbors': 3}
```

Meaning:

> Among all tested values,
> k = 3 performed best on average.

---

## 8. WHAT `best_score_` MEANS

Example output:

```
0.83
```

Meaning:

> With k = 3,
> average cross-validation accuracy was 83 percent.

This is a **robust score**, not luck.

---

## 9. VERY IMPORTANT CLARITY

GridSearchCV:

* trains many models internally
* uses cross validation for each
* chooses best hyperparameters
* does NOT magically improve data
* only finds best settings

---

## 10. ONE SENTENCE THAT SHOULD CLICK NOW

GridSearchCV systematically tries all given hyperparameter values, evaluates each using cross validation, and selects the one that performs best on average.

---
------------------------------------------------------------------------------------------------
PART B

YOUR SECOND DOUBT (VERY IMPORTANT)

“We are giving k values by our own
so how will the perfect model be built?
It is not checking all values.”

This is a brilliant question.

Let’s answer it honestly.

Step 1: The truth (no sugar coating)

GridSearchCV does NOT search all possible values.

It searches only the values you give it.

This is intentional.

Step 2: Why GridSearchCV does NOT try all values

Ask yourself:

For KNN, how many possible k values exist?

If dataset has 10,000 points:

k = 1, 2, 3, 4, ..., 9999


Trying all is:

• extremely slow
• unnecessary
• wasteful

So we limit the search space.

Step 3: Your role as an ML engineer

GridSearchCV is not intelligent.

YOU are responsible for:

• choosing a reasonable range
• based on intuition and experience

Example:

For KNN:
• k too small → overfitting
• k too large → underfitting

So you might choose:

k = [3, 5, 7, 9, 11]


That already covers:
• small
• medium
• large

No need to try 1000 values.

Step 4: Important concept
“Best among given options”

GridSearchCV finds:

the best hyperparameters
among the values you provided

Not globally best in the universe.

And that is perfectly fine in real ML.

Step 5: Why this still works in real life

Because:

• performance curve is usually smooth
• best value lies in a region, not a single number
• once near optimal, exact value doesn’t matter much

So searching intelligently > searching exhaustively.

Step 6: What if we want wider exploration?

That’s why RandomizedSearchCV exists.

Instead of:
• checking all values in a grid

It:
• samples randomly from large ranges

We will do that next.

FINAL LOCK-IN (VERY IMPORTANT)

Read this twice.

GridSearchCV does not magically find the best hyperparameters in the universe; it evaluates all combinations you provide, uses cross-validation to measure their stability, and selects the best performing one among them.



'''