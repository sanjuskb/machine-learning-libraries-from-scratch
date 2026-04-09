import numpy as np
from sklearn.metrics import accuracy_score

# Actual values
y_test = np.array([1, 0, 1, 0, 1, 0])

# Predicted values
y_pred = np.array([1, 0, 0, 0, 1, 1])

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

'''


---

## 4. WHAT HAPPENS INTERNALLY (STEP BY STEP)

Internally, `accuracy_score` does something like this:

### Step 1

Compare values one by one

| Index | Actual | Predicted | Correct? |
| ----- | ------ | --------- | -------- |
| 0     | 1      | 1         | Yes      |
| 1     | 0      | 0         | Yes      |
| 2     | 1      | 0         | No       |
| 3     | 0      | 0         | Yes      |
| 4     | 1      | 1         | Yes      |
| 5     | 0      | 1         | No       |

---

### Step 2

Count correct predictions

Correct = 4
Wrong = 2

---

### Step 3

Divide by total predictions

Total = 6

Accuracy = 4 / 6 = 0.6666

So output is:

```text
Accuracy: 0.6666666666666666
```

Which means:
66.67 percent accuracy.

---

## 5. HOW THIS CONNECTS TO CONFUSION MATRIX

From confusion matrix we had:

* TP = 2
* TN = 2
* FP = 1
* FN = 1

Correct predictions = TP + TN = 4
Total predictions = 6

Accuracy = (TP + TN) / Total
Accuracy = 4 / 6

Same result.

---

## 6. IMPORTANT LIMITATION (VERY IMPORTANT)

Accuracy does **not** tell:

* what kind of mistakes happened
* whether false alarms or missed cases are more

That’s why accuracy alone is **not enough**.

But accuracy is still useful as a **first check**.

---

## 7. ONE-LINE SUMMARY (LOCK THIS)

Accuracy tells the percentage of total predictions that the model got right.

---


'''