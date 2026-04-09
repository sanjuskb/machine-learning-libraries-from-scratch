import pandas as pd

# Example scenario
# We want to predict delivery time based on distance and battery.
data = {
    "distance": [5, 10, 15, 20],
    "battery": [90, 80, 70, 60],
    "time": [10, 20, 30, 40]
}

df = pd.DataFrame(data)
X = df[["distance", "battery"]]
y=df["time"]
print(X.shape)
print(y.shape)
'''
OUTPUT:
(4, 2)
(4,)
it means 
Good, this is an important observation.
I will explain it slowly and clearly, with real meaning.

No new topics.
Only interpretation of what you saw.

WHAT THESE TWO LINES MEAN

(4, 2)
(4,)


FIRST LINE
X.shape gives (4, 2)

Real meaning

4 means number of examples
2 means number of features

So this tells you

There are 4 past observations
Each observation has 2 pieces of information

In your case
Each delivery has
distance
battery

So one row looks like

distance value , battery value

Machine learning logic

The model will learn patterns by comparing these two inputs with the output.

SECOND LINE
y.shape gives (4,)

Real meaning

4 means number of examples
There is no second number because y has only one value per example

So this tells you

There are 4 correct answers
One answer for each observation

In your case
Each delivery has one time value

'''

'''
What this really means

Each row is one past delivery
Each column is one measurable property

Nothing machine learning yet
Just structured past experience
-------------------------------------------
CREATING FEATURES X

X = df[["distance", "battery"]]


Real meaning

You are telling the model
These are the only things you are allowed to look at before prediction

X is a table
Rows are examples
Columns are features

If you remove a column here
The model will never know that information exists
-----------------------------------------------
CREATING TARGET y

y = df["time"]


Real meaning

This is the correct answer for each past example

During training
The model compares its prediction with y

During future prediction
y will not be available

That is why y is separated early and kept aside
--------------------------------------------------
SHAPES OF X AND y

print(X.shape)
print(y.shape)


Why this matters

Number of rows must match
Each feature row must map to exactly one answer

If shapes mismatch
Learning becomes logically impossible

'''
