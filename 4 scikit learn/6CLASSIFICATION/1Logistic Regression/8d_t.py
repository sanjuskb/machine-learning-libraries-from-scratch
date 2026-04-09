from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# Dataset
data = {
    "distance": [5, 10, 20, 30],
    "battery": [90, 80, 40, 20],
    "delayed": [0, 0, 1, 1]
}

df = pd.DataFrame(data)

X = df[["distance", "battery"]]
y = df["delayed"]

# Train Decision Tree
model = DecisionTreeClassifier()
model.fit(X, y)

# Feature importance
print("Feature importance:", model.feature_importances_)
'''

HOW TO INTERPRET THE OUTPUT

Suppose output is:

[1.0  0.0]


This means:

distance importance = 100 percent

battery importance = 0 percent

Meaning:

the tree relied entirely on distance

battery was not needed

If output were:

[0.7  0.3]


Then:

distance contributed 70 percent

battery contributed 30 percent

8. IMPORTANT REALIZATION (VERY IMPORTANT)

Feature importance is:

Model specific

Data dependent

Not universal truth

A feature can be important in one dataset
and unimportant in another.

9. WHY FEATURE IMPORTANCE IS POWERFUL
Machine learning benefits

Helps understand model decisions

Helps remove useless features

Helps improve model performance

Human benefits

Explains why the model decided something

Builds trust

Helps debugging

This is why Decision Trees are used in:

finance

healthcare

rule-based systems

10. ONE SENTENCE THAT MUST STAY WITH YOU

Feature importance tells how much each feature helped the decision tree reduce confusion and make correct decisions.
----------------------------------------------------------------------
'''