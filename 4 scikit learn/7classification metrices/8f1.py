'''
Good. Now we move to **ONLY ONE TOPIC**, exactly as promised.

👉 **F1-score**
👉 with **complete code**
👉 and **clear internal working**
👉 nothing else mixed in

---

# F1-SCORE

(ONLY THIS TOPIC)

---

## 1. WHY F1-SCORE EXISTS (HUMAN LANGUAGE FIRST)

You now clearly know this:

* Precision cares about **false alarms**
* Recall cares about **missed cases**

The problem is:

👉 Improving precision often reduces recall
👉 Improving recall often reduces precision

So a question arises:

How do we judge a model **when both matter**?

That is why **F1-score exists**.

---

## 2. WHAT F1-SCORE MEANS (CLEAR MEANING)

F1-score answers this question:

**How good is the model when we want a balance between precision and recall?**

It does NOT favor only one.
It penalizes the model if **either** precision or recall is low.

---

## 3. IMPORTANT PROPERTY (VERY IMPORTANT)

F1-score is **high only when BOTH precision and recall are high**.

If:

* precision is high, recall is low → F1 is low
* recall is high, precision is low → F1 is low

So F1 forces balance.

---

## 4. F1-SCORE FORMULA (REFERENCE ONLY)

F1 = 2 × (Precision × Recall) / (Precision + Recall)

You do **not** need to memorize this.
What matters is the **logic**, not the formula.

---

## 5. COMPLETE CODE FOR F1-SCORE

We use the **same data again** so nothing feels new.

'''

import numpy as np
from sklearn.metrics import f1_score

# Actual values
y_test = np.array([1, 0, 1, 0, 1, 0])

# Predicted values
y_pred = np.array([1, 0, 0, 0, 1, 1])

# Calculate F1-score
f1 = f1_score(y_test, y_pred)

print("F1-score:", f1)


'''

---

## 6. WHAT HAPPENS INTERNALLY (STEP BY STEP)

Let us reuse what we already know.

From earlier steps:

Precision = 0.6666
Recall = 0.6666

Now apply the idea:

Step 1
Multiply precision and recall

0.6666 × 0.6666 ≈ 0.4444

Step 2
Add precision and recall

0.6666 + 0.6666 = 1.3332

Step 3
Combine them

F1 = 2 × 0.4444 / 1.3332
F1 ≈ 0.6666

So output is:

```text
F1-score: 0.6666666666666666
```

---

## 7. WHAT THIS NUMBER MEANS (HUMAN LANGUAGE)

An F1-score of 0.66 means:

The model is **moderately good**
at balancing false alarms and missed cases.

It is:

* not overly cautious
* not overly aggressive

---

## 8. WHEN F1-SCORE IS PREFERRED

F1-score is preferred when:

* dataset is imbalanced
* both types of mistakes matter
* accuracy alone is misleading

That is why:

* interviews ask F1-score
* companies use F1-score
* competitions rely on F1-score

---

## 9. CONNECTION TO CONFUSION MATRIX (IMPORTANT)

F1-score depends on:

* True Positives
* False Positives
* False Negatives

So again:

👉 Confusion matrix is the root
👉 F1-score is derived from it

Nothing magical.

---

## 10. ONE-LINE SUMMARY (LOCK THIS IN)

F1-score measures how well a model balances precision and recall into a single number.

---




'''