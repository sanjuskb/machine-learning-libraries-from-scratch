import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Create dataset
data = {
    "distance": [5, 10, 20, 30],
    "delayed": [0, 0, 1, 1]
}

df = pd.DataFrame(data)

X = df[["distance"]]
y = df["delayed"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=42
)

# Create model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)
print("Intercept (A):", model.intercept_)
print("Coefficient (B):", model.coef_)


# Predict class
predictions = model.predict(X_test)

# Predict probability
probabilities = model.predict_proba(X_test)

print("X_test:")
print(X_test)
print()

print("Predicted class:", predictions)
print("Predicted probabilities:", probabilities)
'''


---

## LOGISTIC REGRESSION

CODING + INTERNAL WORKING (STEP BY STEP)

---

## COMPLETE CODE FIRST (DO NOT PANIC, WE WILL DECODE IT)

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Create dataset
data = {
    "distance": [5, 10, 20, 30],
    "delayed": [0, 0, 1, 1]
}

df = pd.DataFrame(data)

X = df[["distance"]]
y = df["delayed"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=42
)

# Create model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Predict class
predictions = model.predict(X_test)

# Predict probability
probabilities = model.predict_proba(X_test)

print("X_test:")
print(X_test)
print()

print("Predicted class:", predictions)
print("Predicted probabilities:", probabilities)
```

---

# NOW WE EXPLAIN EVERYTHING SLOWLY

---

## PART 1

DATA AND PROBLEM TYPE

### Machine-learning explanation

* Input feature: distance
* Output target: delayed (binary)
* This is a **binary classification problem**

Logistic Regression is chosen because:

* Output is categorical (0 or 1)
* We want probabilities

### Human explanation

We want to answer:
“Will the delivery be delayed or not?”

Yes or No
That is exactly what Logistic Regression is for.

---

## PART 2

WHAT model.fit REALLY DOES

```python
model.fit(X_train, y_train)
```

### Machine-learning explanation

The model assumes this equation:

```
z = A + B × distance
probability = 1 / (1 + e^(-z))
```

During `fit`, the model:

* Adjusts A (intercept)
* Adjusts B (coefficient)

So that:

* For delayed = 1 → probability close to 1
* For delayed = 0 → probability close to 0

It minimizes **log loss**, not squared error.

### Human explanation

The model is learning:

* At what distance delays usually happen
* How sharply delay probability increases with distance

It tunes two knobs:

* One shifts the decision left or right (A)
* One controls steepness (B)

---

## PART 3

PRINT LEARNED PARAMETERS (VERY IMPORTANT)

Add this after `fit`:

```python
print("Intercept (A):", model.intercept_)
print("Coefficient (B):", model.coef_)
```

Example output (approx):

```
Intercept (A): [-5.5]
Coefficient (B): [[0.3]]
```

This means the learned rule is:

```
z = -5.5 + 0.3 × distance
```

---

## PART 4

WHAT model.predict_proba DOES

```python
probabilities = model.predict_proba(X_test)
```

### Machine-learning explanation

For EACH test input, it returns:

```
[ P(class=0), P(class=1) ]
```

Example output:

```
[[0.95, 0.05],
 [0.08, 0.92]]
```

### Human explanation

For each distance:

* First number → chance of NOT delayed
* Second number → chance of delayed

The model is saying:
“I am X percent confident in each option.”

---

## PART 5

WHAT model.predict DOES

```python
predictions = model.predict(X_test)
```

### Machine-learning explanation

It simply does:

```
if P(class=1) >= 0.5:
    return 1
else:
    return 0
```

### Human explanation

The model looks at probability and decides:

* Confidence high → say YES
* Confidence low → say NO

---

## PART 6

FULL MANUAL CALCULATION (THIS IS THE CORE)

Assume learned equation:

```
z = -5.5 + 0.3 × distance
```

### Case 1: distance = 10

Step 1: calculate z

```
z = -5.5 + 0.3 × 10
z = -5.5 + 3
z = -2.5
```

Step 2: apply sigmoid

```
probability = 1 / (1 + e^(2.5))
probability ≈ 0.075
```

Step 3: threshold

```
0.075 < 0.5 → predicted class = 0
```

Meaning: not delayed

---

### Case 2: distance = 30

Step 1: calculate z

```
z = -5.5 + 0.3 × 30
z = -5.5 + 9
z = 3.5
```

Step 2: apply sigmoid

```
probability = 1 / (1 + e^(-3.5))
probability ≈ 0.97
```

Step 3: threshold

```
0.97 ≥ 0.5 → predicted class = 1
```

Meaning: delayed

---

## WHAT YOU SHOULD UNDERSTAND NOW (VERY IMPORTANT)

Logistic Regression:

* Does NOT predict classes directly
* First predicts probability
* Then converts probability to class
* Uses sigmoid to stay between 0 and 1
* Uses threshold to make decisions

---

## ONE-LINE CORE TRUTH

Logistic Regression is just Linear Regression + sigmoid + decision threshold.
--------------------------------------------------------------------------------------------


---

## YOUR OUTPUT (WE WILL DECODE THIS)

```text
Predicted class: [0 1]

Predicted probabilities:
[[7.60307922e-01 2.39692078e-01]
 [3.15536490e-04 9.99684464e-01]]
```

---

# PART 1

WHAT “Predicted class” MEANS

### Machine learning meaning

```python
predictions = model.predict(X_test)
```

This returns the **final decision** for each test example.

Each value is:

* 0 → class 0
* 1 → class 1

So:

```text
[0 1]
```

means:

* For the first test input → predicted class = 0
* For the second test input → predicted class = 1

This is the **final YES / NO answer**.

---

### Human meaning

Think of this as the model saying:

* First case → NOT delayed
* Second case → DELAYED

This is the **decision**, not the confidence.

---

# PART 2

WHAT “Predicted probabilities” MEANS

Now this line:

```python
probabilities = model.predict_proba(X_test)
```

This does **NOT** give the decision.

It gives the **confidence** behind the decision.

---

## VERY IMPORTANT RULE (MEMORIZE THIS)

For each row:

```text
[ P(class = 0) , P(class = 1) ]
```

First number → probability of class 0
Second number → probability of class 1

They always add up to **1**.

---

# PART 3

DECODE YOUR FIRST ROW

```text
[7.60307922e-01  2.39692078e-01]
```

First, convert scientific notation:

* 7.60307922e-01 = 0.7603
* 2.39692078e-01 = 0.2397

So this row becomes:

```text
[0.7603 , 0.2397]
```

### Machine meaning

* P(class = 0) = 0.7603
* P(class = 1) = 0.2397

Since probability of class 1 < 0.5
→ predicted class = 0

That matches:

```text
Predicted class → 0
```

---

### Human meaning

For the **first test distance**, the model is saying:

“There is a **76 percent chance** this delivery is NOT delayed
and a **24 percent chance** it IS delayed.”

So it confidently chooses **not delayed**.

---

# PART 4

DECODE YOUR SECOND ROW

```text
[3.15536490e-04  9.99684464e-01]
```

Convert scientific notation:

* 3.15536490e-04 = 0.000315
* 9.99684464e-01 = 0.999684

So:

```text
[0.000315 , 0.999684]
```

### Machine meaning

* P(class = 0) = 0.03 percent
* P(class = 1) = 99.97 percent

Since probability of class 1 ≥ 0.5
→ predicted class = 1

That matches:

```text
Predicted class → 1
```

---

### Human meaning

For the **second test distance**, the model is saying:

“I am **almost 100 percent sure** this delivery WILL be delayed.”

So it confidently chooses **delayed**.

---

# PART 5

HOW `predict` USES `predict_proba`

Internally, this is what happens:

```python
if P(class = 1) >= 0.5:
    predicted_class = 1
else:
    predicted_class = 0
```

So:

* `predict_proba` → confidence
* `predict` → final decision

---

# PART 6

CONNECT EVERYTHING TO ONE SIMPLE STORY

For EACH test input, the model does this:

1. Compute probability of both classes
2. Check which probability is larger
3. Return that class as prediction

That is all.

---

## ONE-LINE FINAL MEANING (IMPORTANT)

Predicted probabilities tell **how confident** the model is,
predicted class tells **what final decision** the model makes.

---

## CHECKPOINT QUESTION (JUST FOR YOU)

If probability output was:

```text
[0.49 , 0.51]
```

What would predicted class be?

Answer: **1**
Because 0.51 ≥ 0.5

---
------------------------------------------------------------------------------------------------------------



---

## 1. WHAT DOES “CLASS” MEAN (CORE IDEA)

### Machine learning meaning

A **class** is a possible category that an output can belong to.

In classification problems, the output is **not a number**, it is a **label**.

---

### Human meaning

A class is just a **type of answer**.

Examples from real life

* Email → spam or not spam
* Exam → pass or fail
* Delivery → delayed or not delayed

Each possible answer is a **class**.

---

## 2. WHAT IS CLASS 0 AND CLASS 1

### Machine learning meaning

In binary classification (two possible outcomes):

* Class 0 represents one category
* Class 1 represents the other category

These are **labels**, not values, not ranks, not good or bad.

The model does not understand words like
“delayed” or “not delayed”.

It only understands **numbers**, so we encode classes as 0 and 1.

---

### Human meaning

Class 0 and Class 1 are just **names**, like:

* Switch OFF = 0
* Switch ON = 1

or

* NO = 0
* YES = 1

There is **nothing special** about 0 or 1.
They are just convenient labels.

---

### In YOUR example

You defined:

```text
delayed = 0  → not delayed
delayed = 1  → delayed
```

So:

* Class 0 means → delivery is NOT delayed
* Class 1 means → delivery IS delayed

That is all.

---

## 3. WHY THE MODEL TALKS ABOUT PROBABILITIES

### Machine learning meaning

Logistic Regression does **not directly say** class 0 or class 1.

It first asks:

“How confident am I that this input belongs to each class?”

So it computes probabilities for **each class**.

---

### Human meaning

Instead of directly saying YES or NO,
the model first says:

* “I am 76 percent sure it is NOT delayed”
* “I am 24 percent sure it IS delayed”

Then it picks the stronger one.

This is how humans think too.

---

## 4. WHY THERE ARE **4 VALUES** IN PROBABILITIES

This is the key confusion. Let us resolve it cleanly.

### Rule you must remember forever

```
number of probability values
= number of test samples × number of classes
```

---

### In YOUR case

* Number of test samples = 2
* Number of classes = 2 (class 0 and class 1)

So:

```
2 × 2 = 4 values
```

That is why you see **4 numbers**.

---

## 5. WHAT EACH OF THOSE 4 VALUES MEANS (CLEAR MAPPING)

Your output was:

```text
Predicted probabilities:
[
  [0.7603 , 0.2397],
  [0.0003 , 0.9997]
]
```

Let us label everything clearly.

---

### FIRST ROW → FIRST TEST INPUT

This row belongs to **test example 1**.

```text
[0.7603 , 0.2397]
```

Meaning:

* 76 percent chance → class 0 (not delayed)
* 24 percent chance → class 1 (delayed)

So model chooses **class 0**.

---

### SECOND ROW → SECOND TEST INPUT

This row belongs to **test example 2**.

```text
[0.0003 , 0.9997]
```

Meaning:

* 0.03 percent chance → class 0 (not delayed)
* 99.97 percent chance → class 1 (delayed)

So model chooses **class 1**.

---

## 6. HOW THIS CONNECTS TO “PREDICTED CLASS”

You also saw:

```text
Predicted class: [0 1]
```

This is simply:

* First test input → class 0
* Second test input → class 1

The probabilities **explain why** those decisions were made.

---

## 7. ONE SIMPLE SENTENCE THAT SUMS IT UP

Classes are just category labels,
class 0 and class 1 are names for those categories,
and the 4 probability values exist because the model gives confidence for each class for each test input.

---









'''