

# We use KNN, because hyperparameters are intuitive.

# Data:

import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

X = np.array([
    [1, 90],
    [2, 85],
    [3, 80],
    [8, 30],
    [9, 25],
    [10, 20]
])

y = np.array([0, 0, 0, 1, 1, 1])

'''2. WHAT WE WANT TO TUNE

KNN hyperparameters:

n_neighbors → how many neighbors

weights → uniform or distance

But this time, instead of a small fixed list, we give a large range.'''

# Pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("knn", KNeighborsClassifier())
])

# Hyperparameter distributions (large search space)
param_dist = {
    "knn__n_neighbors": randint(1, 20),
    "knn__weights": ["uniform", "distance"]
}

# RandomizedSearchCV
random_search = RandomizedSearchCV(
    estimator=pipeline,
    param_distributions=param_dist,
    n_iter=10,
    cv=3,
    random_state=42
)

# Run randomized search
random_search.fit(X, y)

# Results
print("Best parameters:", random_search.best_params_)
print("Best CV score:", random_search.best_score_)

'''
4. WHAT IS NEW HERE (IMPORTANT PARTS)
a. randint(1, 20)

This means:

n_neighbors can be any integer from 1 to 19


So possible values are:

1, 2, 3, 4, ..., 19


This is a large search space, not a small list.

b. n_iter = 10

This is the most important line.

It means:

“Randomly try only 10 hyperparameter combinations.”

Even though the total possible combinations are:

19 (k values) × 2 (weights) = 38


Only 10 random combinations will be tested.

5. WHAT RANDOMIZEDSEARCHCV DOES INTERNALLY (STEP BY STEP)

Let’s simulate it conceptually.

Step 1: Build the full search space

Possible examples:

k=1, weights=uniform
k=2, weights=distance
k=15, weights=uniform
k=7, weights=distance
...


There are 38 possible combinations.

Step 2: Randomly pick 10 combinations

Example (randomly selected):

k=3, weights=distance

k=17, weights=uniform

k=9, weights=distance

k=5, weights=uniform

k=14, weights=distance

k=2, weights=uniform

k=18, weights=distance

k=11, weights=uniform

k=6, weights=distance

k=8, weights=uniform

These are chosen randomly, but reproducibly because of random_state.

Step 3: For EACH combination, run cross-validation

For every one of those 10 combinations:

split data into 3 folds

train and test 3 times

compute average score

So total model trainings:

n_iter × cv = 10 × 3 = 30 trainings


You wrote ONE .fit() line.
sklearn trained 30 models internally.

6. HOW THE BEST PARAMETERS ARE CHOSEN

After evaluating all 10 combinations:

sklearn compares their average CV scores

selects the combination with the highest score

That becomes:

random_search.best_params_
random_search.best_score_

7. ADDRESSING YOUR BIG DOUBT DIRECTLY (IMPORTANT)

You asked:

“What if good values are not selected?”

Answer, clearly:

good hyperparameter regions are usually wide

random sampling with enough iterations almost always hits them

you control n_iter

cross-validation filters out lucky bad choices

That’s why this works in practice.

8. WHEN RANDOMIZEDSEARCHCV IS BETTER THAN GRIDSEARCHCV

Use RandomizedSearchCV when:

large ranges

many hyperparameters

limited time

early exploration phase

Use GridSearchCV when:

small, focused range

fine-tuning near optimum

9. VERY IMPORTANT FINAL CLARITY

RandomizedSearchCV does NOT replace thinking.

You still:

choose reasonable ranges

choose number of iterations

interpret results

It replaces brute-force, not intelligence.

10. ONE SENTENCE THAT SHOULD NOW BE SOLID

RandomizedSearchCV efficiently finds good hyperparameters by randomly sampling a limited number of combinations from large ranges and evaluating each with cross-validation.

'''
