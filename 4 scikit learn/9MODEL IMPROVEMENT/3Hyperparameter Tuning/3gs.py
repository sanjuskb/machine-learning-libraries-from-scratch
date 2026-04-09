'''
Great. Now we move to **Hyperparameter Tuning – PART 4**.

This is the **professional-grade workflow** you see in real ML projects and interviews.

We will do **GridSearchCV with Pipeline**.

Slow. Clear. Complete.

---

# GRIDSEARCHCV + PIPELINE

PART 4: END-TO-END WORKFLOW (THE RIGHT WAY)

---

## 1. WHY WE COMBINE GRIDSEARCHCV WITH PIPELINE

You already know two facts:

1. Preprocessing must be fit **only on training data**
2. Cross-validation splits data **multiple times**

Now think carefully:

During GridSearchCV:

* data is split many times
* each split has its own training part

So preprocessing must be:

* refit **inside each fold**
* using only that fold’s training data

Doing this manually is:

* error-prone
* almost impossible to manage

**Pipeline automates this safely.**

---

## 2. PROBLEM SETUP (CLEAR AND SMALL)

We reuse a dataset where scaling actually matters.

Features:

```
distance, battery
```

Target:

```
0 = safe
1 = unsafe
```

---

## 3. COMPLETE WORKING CODE (RUN AS IS)

'''
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

# Data
X = np.array([
    [1, 90],
    [2, 85],
    [3, 80],
    [8, 30],
    [9, 25],
    [10, 20]
])

y = np.array([0, 0, 0, 1, 1, 1])

# Pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier())
])

# Hyperparameter grid
param_grid = {
    "knn__n_neighbors": [1, 3, 5],
    "knn__weights": ["uniform", "distance"]
}

# GridSearchCV
grid = GridSearchCV(
    estimator=pipeline,
    param_grid=param_grid,
    cv=3
)

# Run grid search
grid.fit(X, y)

# Results
print("Best parameters:", grid.best_params_)
print("Best CV score:", grid.best_score_)


'''

---

## 4. IMPORTANT NEW SYNTAX (DO NOT SKIP)

### What does this mean?

```python
"knn__n_neighbors"
```

This means:

• `knn` → name of the step in Pipeline
• `n_neighbors` → parameter of KNN

Double underscore connects:

```
pipeline_step__parameter_name
```

Same for:

```python
"knn__weights"
```

---

## 5. WHAT HAPPENS INTERNALLY (THIS IS THE CORE)

Let’s expand **one combination**.

Example:

```
n_neighbors = 3
weights = "distance"
```

For this combination, GridSearchCV does:

### For fold 1:

1. scaler.fit(training_fold_1)
2. scaler.transform(training_fold_1)
3. train KNN (k=3, distance)
4. scaler.transform(test_fold_1)
5. test and score

### For fold 2:

Repeat with new train/test split

### For fold 3:

Repeat again

Then:

```
average score is computed
```

---

## 6. HOW MANY MODELS WERE TRAINED

Count them:

• n_neighbors values = 3
• weights values = 2
• total combinations = 6

• cv = 3 folds

Total trainings:

```
6 × 3 = 18 models
```

You wrote **one fit line**.
sklearn trained **18 models** safely.

---

## 7. WHY THIS IS THE CORRECT WAY

This workflow guarantees:

• no data leakage
• correct preprocessing per fold
• fair hyperparameter comparison
• reproducible results

This is **industry standard ML**.

---

## 8. WHAT `best_params_` REALLY MEANS

Example output:

```
{'knn__n_neighbors': 3, 'knn__weights': 'distance'}
```

Meaning:

Among all tested settings,
this combination performed best **on average across folds**.

---

## 9. WHAT `best_score_` REALLY MEANS

Example:

```
0.83
```

Meaning:

Using the best hyperparameters,
average cross-validation accuracy was 83%.

This is a **robust estimate**, not luck.

---

## 10. ONE SENTENCE TO LOCK THIS PART

GridSearchCV with Pipeline safely tunes hyperparameters by evaluating all given combinations using cross-validation while correctly applying preprocessing inside each fold.

---
---------------------------------------------------------------------------------------------------------


I’ll explain **only this line** deeply:

```python
"knn__weights": ["uniform", "distance"]
```

No extra topics. No skipping.

---

## 1. FIRST: WHAT “weights” MEANS IN KNN

KNN works like this:

> Look at the k nearest neighbors
> and decide the output based on them

But here is the key question:

👉 **Do all neighbors have equal influence?**
👉 Or should closer neighbors matter more?

That is exactly what `weights` controls.

---

## 2. CASE 1: weights = "uniform"

### Meaning

```python
weights = "uniform"
```

means:

> Every neighbor has **equal importance**

If k = 5:

* each neighbor votes equally
* distance does NOT change influence

---

### Example

Suppose k = 3 neighbors:

| Neighbor | Distance | Class |
| -------- | -------- | ----- |
| A        | 1 unit   | 1     |
| B        | 2 units  | 1     |
| C        | 9 units  | 0     |

Uniform weighting:

* A votes 1
* B votes 1
* C votes 0

Votes:

```
1 → 2 votes
0 → 1 vote
```

Prediction = **1**

Distance did not matter at all.

---

## 3. CASE 2: weights = "distance"

### Meaning

```python
weights = "distance"
```

means:

> Closer neighbors have **more influence**
> Farther neighbors have **less influence**

So distance matters directly.

---

### Same example again

| Neighbor | Distance | Class |
| -------- | -------- | ----- |
| A        | 1        | 1     |
| B        | 2        | 1     |
| C        | 9        | 0     |

Distance-based influence:

* A gets high weight
* B gets medium weight
* C gets very low weight

So the two close neighbors dominate strongly.

Prediction = **1**, but now for a **better reason**.

---

## 4. WHY THIS OPTION EXISTS (VERY IMPORTANT)

Uniform weighting is good when:

* data is clean
* noise is low
* clusters are well separated

Distance weighting is better when:

* noise exists
* far neighbors may be misleading
* closer points are more reliable

Neither is always best.

That’s why it is a **hyperparameter**.

---

## 5. WHY GRIDSEARCHCV TRIES BOTH

You do NOT know in advance:

* whether distance matters strongly
* whether uniform voting is enough

So GridSearchCV says:

> “Let me try both
> and see which one performs better
> across cross-validation folds”

That is exactly what you want.

---

## 6. WHY IT IS WRITTEN INSIDE param_grid

```python
param_grid = {
    "knn__n_neighbors": [1, 3, 5],
    "knn__weights": ["uniform", "distance"]
}
```

This means:

Try all combinations of:

* k values
* weighting strategies

So examples tested internally:

* k=3, uniform
* k=3, distance
* k=5, uniform
* k=5, distance

---

## 7. VERY IMPORTANT CLARITY

`weights` does NOT mean:

* feature weights
* model weights
* coefficients

It only controls:

> how neighbors vote

---

## 8. ONE SENTENCE TO LOCK THIS IN

In KNN, the weights hyperparameter decides whether all neighbors vote equally or closer neighbors have more influence than farther ones.

---






'''