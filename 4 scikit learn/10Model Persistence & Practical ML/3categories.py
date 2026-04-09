'''
# 🔹 LAYER 6

##  Handling Categorical Data

We will cover **ONLY THIS**, in this exact order:

PART 1
What categorical data is and why models cannot understand it

PART 2
LabelEncoder
what it does
how it works
when it is dangerous

PART 3
OneHotEncoder
what it does
why it exists
why it is usually correct



---

## PART 1: WHAT IS CATEGORICAL DATA

Categorical data means:

data that represents **categories or labels**, not numbers with magnitude.

Examples:

```
color = red, blue, green
city = Delhi, Mumbai, Chennai
zone = safe, unsafe
weather = sunny, rainy
```

These are **names**, not quantities.

---

### VERY IMPORTANT CLARITY

Even if categories look like text, they are **information**, not numbers.

For example:

```
safe vs unsafe
```

There is:

* no distance
* no ordering
* no arithmetic meaning

---

## WHY ML MODELS CANNOT HANDLE CATEGORICAL DATA DIRECTLY

ML models work using:

* addition
* multiplication
* distance
* gradients

They understand **numbers only**.

So this will FAIL:

```
model.fit(["red", "blue", "green"], y)
```

Because the model asks:

> How do I multiply red
> How far is blue from green

It makes no sense mathematically.

---

## SO WHAT DO WE DO

We **encode** categorical data into numbers.

Encoding means:

> converting categories into numbers
> in a way models can work with

---

## PART 2: LabelEncoder

Now we study **LabelEncoder**.

---

## WHAT LabelEncoder DOES

LabelEncoder:

> assigns a unique number to each category

Example:

```
["safe", "unsafe", "safe", "safe"]
```

Becomes:

```
safe   → 0
unsafe → 1
```

So encoded output:

```
[0, 1, 0, 0]
```

---

## COMPLETE WORKING CODE (RUN AS IS)
'''
from sklearn.preprocessing import LabelEncoder

zones = ["safe", "unsafe", "safe", "safe"]

encoder = LabelEncoder()
encoded_zones = encoder.fit_transform(zones)

print(encoded_zones)

'''
Output:

```
[0 1 0 0]
```

---

## WHAT HAPPENS INTERNALLY (VERY IMPORTANT)

When you call:

```python
encoder.fit(zones)
```

Internally:

* it finds all unique categories
* sorts them alphabetically
* assigns numbers starting from 0

So:

```
safe   → 0
unsafe → 1
```

Then:

```python
encoder.transform(zones)
```

Replaces each category with its number.

---

## WHY LabelEncoder IS DANGEROUS (THIS IS CRITICAL)

LabelEncoder creates **fake numerical meaning**.

Example:

```
safe   → 0
unsafe → 1
```

Now the model thinks:

```
unsafe > safe
1 > 0
```

But in reality:

* safe and unsafe have no numeric order
* no distance
* no magnitude

This can break models.

---

## VERY IMPORTANT EXAMPLE (READ CAREFULLY)

Suppose categories:

```
low, medium, high
```

LabelEncoder gives:

```
high   → 0
low    → 1
medium → 2
```

Now the model thinks:

```
medium > low > high
```

Which is WRONG.

This is **artificial ordering**.

---

## WHEN LabelEncoder IS ACTUALLY OK

LabelEncoder is safe ONLY when:

* encoding the **target variable**
* classes are labels, not features

Example:

```
y = ["cat", "dog", "dog", "cat"]
```

This is classification target.

Here:

* model does NOT do arithmetic on y
* order does not matter

So LabelEncoder is fine for **y**, not for **X**.

---

## VERY IMPORTANT RULE (LOCK THIS IN)

LabelEncoder should be used for target labels, not for input features.

---

## HUMAN UNDERSTANDING SUMMARY

LabelEncoder:

* replaces category names with numbers
* is simple
* but introduces fake ordering
* dangerous for input features

---

## ONE SENTENCE THAT MUST STICK

LabelEncoder converts categories into numeric labels but should generally be used only for target variables, not input features, because it introduces artificial ordering.

---




'''