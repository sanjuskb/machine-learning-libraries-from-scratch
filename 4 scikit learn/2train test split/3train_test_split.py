from sklearn.model_selection import train_test_split
'''
Now understand this line word by word.

sklearn
This is the short name of scikit learn

model_selection
This module contains tools related to choosing and evaluating models

train_test_split
This is a function inside model_selection
'''
import pandas as pd

data = {
    "distance": [5, 10, 15, 20],
    "battery": [90, 80, 70, 60],
    "time": [10, 20, 30, 40]
}

df = pd.DataFrame(data)

X = df[["distance", "battery"]]
y = df["time"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)
'''
Real meaning step by step

X and y are given together
So rows stay aligned

test_size equals 0.25
This means one quarter of rows are hidden for testing

----------------------

When you give

random_state = 42 (any number will be given not only 42)

Python creates a random number generator
but with a fixed starting point.

From that starting point
it generates the same sequence of random numbers every time.

Because the sequence is the same
the same rows are chosen for testing every time.



The computer generates a fixed random pattern once
and follows that same pattern every run.

So

Run 1
row 3 chosen for test

Run 2
row 3 chosen for test

Run 3
row 3 chosen for test

Always the same, as long as
random_state stays the same
data stays the same
'''

print(X_train)
print()
print(X_test)
print()
print(y_train)
print()
print(y_test)
print()
'''
What you should notice

X_train has most rows
X_test has fewer rows

y_train matches X_train rows
y_test matches X_test rows

No mixing. No mismatch.

This is exactly what we want.
'''