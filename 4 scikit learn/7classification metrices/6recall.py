'''
Good. We continue **exactly one topic at a time**, no mixing.

Now we cover **ONLY ONE TOPIC**:

👉 **Recall**
👉 with **complete code**
👉 and **clear internal working**
👉 nothing else included

---

# RECALL

(ONLY THIS TOPIC)

---

## 1. WHAT RECALL MEANS (HUMAN LANGUAGE)

Recall answers this question:

**Out of all the real YES cases, how many did the model correctly catch?**

It does **not** care about false alarms.
It cares about **missed cases**.

---

## 2. WHY RECALL EXISTS (INTUITION)

Imagine this situation:

Some deliveries were actually delayed,
but the model predicted “not delayed”.

Those missed delays can cause:

* customer complaints
* wrong planning
* serious problems

Recall tells you **how good the model is at catching real problems**.

---

## 3. RECALL FORMULA (REFERENCE ONLY)

Recall = True Positives / (True Positives + False Negatives)

Meaning:
Correct YES predictions
divided by
all actual YES cases

---

## 4. COMPLETE CODE FOR RECALL

We again use the **same data** so nothing feels new.

'''
import numpy as np
from sklearn.metrics import recall_score

# Actual values
y_test = np.array([1, 0, 1, 0, 1, 0])

# Predicted values
y_pred = np.array([1, 0, 0, 0, 1, 1])

# Calculate recall
recall = recall_score(y_test, y_pred)

print("Recall:", recall)



'''

---

## 5. WHAT HAPPENS INTERNALLY (STEP BY STEP)

The function `recall_score` does this internally.

---

### Step 1

Find all cases where the **actual value is 1 (YES)**

From `y_test`:

```text
Index:   0  1  2  3  4  5
Actual:  1  0  1  0  1  0
```

Actual YES cases at indices:

* 0
* 2
* 4

Total actual YES cases = 3

---

### Step 2

Check how many of these were predicted correctly

Look at `y_pred` at those indices:

* Index 0 → predicted = 1 → correct
* Index 2 → predicted = 0 → missed
* Index 4 → predicted = 1 → correct

So:

True Positives = 2
False Negatives = 1

---

### Step 3

Apply formula

Recall = TP / (TP + FN)
Recall = 2 / (2 + 1)
Recall = 2 / 3
Recall = 0.6666

So output is:

```text
Recall: 0.6666666666666666
```

---

## 6. HOW THIS CONNECTS TO CONFUSION MATRIX

From confusion matrix:

* TP = 2
* FN = 1

Recall = TP / (TP + FN)
Recall = 2 / 3

Same result.

---

## 7. IMPORTANT REAL-WORLD MEANING

High recall means:

* model misses very few real problems
* most actual YES cases are detected

Low recall means:

* model fails to catch many real YES cases
* dangerous in safety-critical systems

---

## 8. ONE-LINE SUMMARY (LOCK THIS)

Recall measures how many actual positive cases the model correctly identified.

---




'''