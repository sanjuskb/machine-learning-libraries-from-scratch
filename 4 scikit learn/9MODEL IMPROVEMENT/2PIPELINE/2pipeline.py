'''
Good. Now we do **Pipeline with full code**, exactly what you asked for earlier.

Only this topic.
Clean code.
Line by line explanation.
And I will explicitly show **how Pipeline prevents the preprocessing mistake** you were confused about.

---

## PIPELINE

PART 2: PIPELINE WITH COMPLETE CODE AND INTERNAL LOGIC

---

## 1. WHAT WE ARE BUILDING (VERY CLEAR GOAL)

We want a **single object** that does this safely:

1. split data
2. scale features
3. train model
4. predict

And guarantees:

* scaler is fit only on training data
* same scaler is used for test data
* no data leakage
* no forgetting steps

That object is a **Pipeline**.

---

## 2. SIMPLE DATA (NO CONFUSION)

We use one feature so logic is easy.

```
distance → time
```

---

'''


import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

# Create data
X = np.array([[10], [20], [30], [40], [50], [60]])
y = np.array([15, 25, 35, 45, 55, 65])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)

# Create pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])
print("X_train:",X_train)
print()
print("X_test:",X_test)
print()
print("y_train:",y_train)
print()
print("y_test:",y_test)
print()
print("pipeline:",pipeline)
print()
# Train pipeline
pipeline.fit(X_train, y_train)

#actually no need of this to show scalar is working we are printing these
print("Scaler mean:", pipeline.named_steps["scaler"].mean_)
print()
print("Scaler scale (std):", pipeline.named_steps["scaler"].scale_)
print()
print("Model coefficient:", pipeline.named_steps["model"].coef_)
print()
print("Model intercept:", pipeline.named_steps["model"].intercept_)
print()
X_train_scaled = pipeline.named_steps["scaler"].transform(X_train)
X_test_scaled = pipeline.named_steps["scaler"].transform(X_test)

print("Scaled X_train:", X_train_scaled)
print()
print("Scaled X_test:", X_test_scaled)
print()


# Predict
predictions = pipeline.predict(X_test)

print("Predictions:")
print(predictions)


'''

---

## 4. NOW LINE-BY-LINE EXPLANATION (IMPORTANT)

---

### Step 1: Data creation

```python
X = [[10], [20], [30], [40], [50], [60]]
y = [15, 25, 35, 45, 55, 65]
```

Meaning:

* X is input feature
* y is target
* each row corresponds to one example

---

### Step 2: Train test split

```python
X_train, X_test, y_train, y_test = train_test_split(...)
```

Now:

* training data is isolated
* test data is untouched
* pipeline must respect this separation

---

### Step 3: Creating the Pipeline (CORE STEP)

```python
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])
```

This means:

Create a **fixed sequence**:

1. First apply StandardScaler
2. Then apply LinearRegression

Pipeline remembers this order forever.

---

### Step 4: pipeline.fit(X_train, y_train)

THIS IS THE MOST IMPORTANT PART.

When you call:

```python
pipeline.fit(X_train, y_train)
```

Internally, Pipeline does this:

#### Step 4.1

```python
scaler.fit(X_train)
```

Scaler learns:

* mean of training data
* standard deviation of training data

Test data is NOT touched.

---

#### Step 4.2

```python
X_train_scaled = scaler.transform(X_train)
```

Training data is scaled.

---

#### Step 4.3

```python
model.fit(X_train_scaled, y_train)
```

Model learns from **scaled training data**.

All steps are automatic.
You did not write them manually.

---

### Step 5: pipeline.predict(X_test)

When you call:

```python
pipeline.predict(X_test)
```

Pipeline internally does:

#### Step 5.1

```python
X_test_scaled = scaler.transform(X_test)
```

Uses the SAME scaler fitted on training data.

---

#### Step 5.2

```python
model.predict(X_test_scaled)
```

Predicts output.

You never risk:

* refitting scaler
* using wrong statistics
* forgetting a step

---

## 5. THIS ANSWERS YOUR CONFUSION DIRECTLY

You asked:

> what does using different preprocessing for train and test mean

Pipeline **makes it impossible** to do that by mistake.

There is:

* one scaler
* one rule
* one workflow

---

## 6. WHY PIPELINE IS A BIG DEAL (REAL ML)

Without pipeline:

* easy to forget steps
* easy to leak data
* messy experiments

With pipeline:

* clean
* safe
* professional
* interview-ready

---

## 7. VERY IMPORTANT RULE (LOCK THIS IN)

Anything that has:

* fit
* transform

should usually go **inside a pipeline**.

---

## ONE SENTENCE THAT SHOULD CLICK NOW

A pipeline guarantees that preprocessing is learned only from training data and applied consistently to all future data.
--------------------------------------------------------------------------------------------------------
You are saying:

“I printed X_train and X_test, they are NOT scaled.
Predictions are perfect.
So where is scaling happening?
It looks like scaler is doing nothing.”

This is the exact right question to ask at this stage.
Now I’ll clear this completely, step by step, with zero hand-waving.

1. FIRST, THE MOST IMPORTANT TRUTH (READ THIS CAREFULLY)

👉 Pipeline NEVER modifies your original X_train or X_test variables.
👉 Scaling happens internally, not in-place.

That is the key misunderstanding.

So when you do:

print(X_train)


You will never see scaled values there.

Pipeline works like this:

original X  → (copy) → scaled X → model


Your original X stays untouched.

2. WHY YOU SEE PERFECT PREDICTIONS (THIS IS NOT MAGIC)

Your data is:

X: 10, 20, 30, 40, 50, 60
y: 15, 25, 35, 45, 55, 65


This relationship is perfectly linear:

y = x + 5


Linear Regression is scale-invariant, meaning:

If you scale X, the model coefficients change,
but predictions remain the same.

So:

with scaler → predictions correct

without scaler → predictions correct

That’s why scaling appears “useless” here.

This is not because scaler didn’t work
but because this dataset is too perfect and simple.

3. PROOF THAT SCALING ACTUALLY HAPPENED (NO ASSUMPTIONS)

Let’s prove it, not explain it.

Add this AFTER pipeline.fit(...)
print("Scaler mean:", pipeline.named_steps["scaler"].mean_)
print("Scaler scale (std):", pipeline.named_steps["scaler"].scale_)
print("Model coefficient:", pipeline.named_steps["model"].coef_)
print("Model intercept:", pipeline.named_steps["model"].intercept_)

What this proves

mean_ → scaler DID compute training mean

scale_ → scaler DID compute training std

model coef → trained on scaled values, not raw ones

If scaler was not used, these values would not exist.

4. WHERE EXACTLY SCALING HAPPENS (INVISIBLE BUT REAL)

When you run:

pipeline.fit(X_train, y_train)


Pipeline internally does this exact thing:

# hidden internal steps
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
model.fit(X_train_scaled, y_train)


But:

X_train_scaled is an internal variable

you never printed it

sklearn does not overwrite X_train

So of course you don’t see it.

5. LET ME SHOW YOU THE SCALED DATA EXPLICITLY

Add this line:

X_train_scaled = pipeline.named_steps["scaler"].transform(X_train)
X_test_scaled = pipeline.named_steps["scaler"].transform(X_test)

print("Scaled X_train:", X_train_scaled)
print("Scaled X_test:", X_test_scaled)


Now you WILL see scaling.

This removes all doubt.

6. WHY PIPELINE PRINTS NOTHING BY DEFAULT

Because pipeline is designed for:

safety

correctness

production usage

Not for teaching.

It assumes:

“If you asked for a pipeline, you know preprocessing happens.”

So it hides intermediate outputs.

7. WHY THIS EXAMPLE HIDES THE BENEFIT (IMPORTANT)

In your example:

only one feature

perfectly linear

no outliers

no competing feature scales

So scaling does not change predictions.

This is expected and correct.

In real data:

multiple features

different units

distance-based models

PCA, KNN, KMeans

Without scaling:

results break badly

8. ONE CRITICAL LINE THAT SHOULD CLICK NOW

Pipeline does scale the data, but it does so on internal copies, leaving your original variables unchanged.

9. FINAL MENTAL CHECK (VERY IMPORTANT)

Answer these:

Did scaler compute mean and std? → YES

Did model train on scaled data? → YES

Did X_train change visually? → NO (by design)

Are predictions still correct? → YES

That means everything worked exactly as intended.
---




'''
