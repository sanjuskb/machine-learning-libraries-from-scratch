import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data={
    "distance":[5, 10, 15, 20, 25, 30],
    "battery": [90, 85, 80, 75, 70, 65],
    "time": [10, 18, 26, 34, 42, 50]
}
df=pd.DataFrame(data)
print(df)
print()

X = df[["distance", "battery"]]
y = df["time"]
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.33,
    random_state=42
)
print(X_train)
print()
print(X_test)
print()
print(y_train)
print()
print(y_test)
print()
model=LinearRegression()#CREATE THE MODEL OBJECT
model.fit(X_train, y_train)#TRAIN THE MODEL USING fit
predicted_time = model.predict(X_test)#MAKE PREDICTIONS USING predict

print("Predicted values:")
print(predicted_time)
print()

print("Actual values:")
print(y_test.values)
print()

score = model.score(X_test, y_test)
print("Model score:", score)

'''

This example will cover
dataset
features and target
train test split
model object
fit
predict
score

All in one place.

---

COMPLETE EXAMPLE
LINEAR REGRESSION MODEL
FROM ZERO TO PREDICTION

---

STEP 1
IMPORT REQUIRED LIBRARIES

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
```

Meaning

pandas is used to create and handle data
train_test_split is used to split data honestly
LinearRegression is the model we chose

Nothing has learned yet.

---

STEP 2
CREATE A SIMPLE DATASET

```python
data = {
    "distance": [5, 10, 15, 20, 25, 30],
    "battery": [90, 85, 80, 75, 70, 65],
    "time": [10, 18, 26, 34, 42, 50]
}

df = pd.DataFrame(data)
```

Meaning

Each row is one delivery example
distance and battery are properties
time is the result

This is past experience data.

---

STEP 3
SEPARATE FEATURES AND TARGET

```python
X = df[["distance", "battery"]]
y = df["time"]
```

Meaning

X contains inputs
distance and battery

y contains output
time

This separation is mandatory in machine learning.

---

STEP 4
SPLIT INTO TRAINING AND TESTING DATA

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.33,
    random_state=42
)
```

Meaning

Some examples are used for learning
Some are hidden for testing

random_state ensures same split every run.

---

STEP 5
CREATE THE MODEL OBJECT

```python
model = LinearRegression()
```

Meaning

You are choosing how the machine should learn
But learning has NOT started

The model is empty at this stage.

---

STEP 6
TRAIN THE MODEL USING fit

```python
model.fit(X_train, y_train)
```

Meaning

The model looks at training examples
Compares inputs with correct answers
Learns the relationship

This is the only step where learning happens.

---

STEP 7
MAKE PREDICTIONS USING predict

```python
predicted_time = model.predict(X_test)
```

Meaning

The model is given only inputs
distance and battery

It uses learned patterns
and guesses the delivery time

predict does not change the model.

---

STEP 8
COMPARE PREDICTIONS WITH REAL VALUES

```python
print("Predicted values:")
print(predicted_time)

print("Actual values:")
print(y_test.values)
```

Meaning

You are checking
how close the guesses are
to real answers

This shows how well learning worked.

---

STEP 9
CHECK MODEL PERFORMANCE USING score

```python
score = model.score(X_test, y_test)
print("Model score:", score)
```

Meaning

score tells
how well the model performs on unseen data

Closer to 1 means better
Closer to 0 means poor

This is evaluation.

---

MENTAL FLOW SUMMARY

Data collected
Features and target separated
Data split honestly
Model chosen
Model trained using fit
Predictions made using predict
Performance checked using score

This exact flow exists in
Logistic Regression
KNN
Deep Learning
Everything.

---

IMPORTANT REASSURANCE

You are not expected to feel mastery yet.
Understanding comes from rerunning and observing.

What matters is
you now know what each step is doing
and why it exists.

---
-------------------------------------------------------------------------------------------
ARE WE DONE WITH MODEL OBJECT

For now, yes.

You have learned everything that a beginner must know about a model object.

What you already understand:

Model is an object that represents an algorithm
Creating the model does not mean learning
fit is the only step where learning happens
predict is using learned knowledge
score is checking performance

This is the complete core of a model object.

Every scikit learn model follows this same pattern.

So at this stage, model object is complete.

Later, much later, you will see extra things like
model parameters
coefficients
intercepts

But those are not required now and would confuse you


'''


