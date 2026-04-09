'''


---

# 🔹 LAYER 6: MODEL PERSISTENCE & PRACTICAL ML

We will cover **3 topics**, in this exact order:

1: Saving & Loading Models
2: Handling Missing Data
3: Handling Categorical Data

---

## TODAY: ONLY TOPIC 1:

### Saving & Loading Models

(joblib and pickle)

No other topic in this message.

---

## 1. FIRST: WHY SAVING A MODEL IS NEEDED (CORE IDEA)

Till now, you trained models like this:

```
model.fit(X_train, y_train)
```

But ask this very important question:

👉 What happens when the program stops
👉 Or laptop shuts down
👉 Or you want to use the model tomorrow

Answer: **Everything is lost**.

Training again:

* wastes time
* may give different results
* is not practical

So we need a way to **store the trained model permanently**.

This is called **model persistence**.

---

## 2. WHAT “SAVING A MODEL” ACTUALLY MEANS

Saving a model means:

> Storing the learned parameters and configuration
> of a trained model into a file
> so it can be reused later without retraining.

Important:

* not saving data
* not saving code
* saving the **trained brain** of the model

---

## 3. REAL HUMAN ANALOGY (VERY IMPORTANT)

Think of training a model like:

* studying for exams
* gaining knowledge

Saving the model is like:

* writing notes and storing them in a book

Loading the model is like:

* opening the book later
* using the knowledge immediately

No re-studying required.

---

## 4. TWO COMMON WAYS TO SAVE MODELS IN PYTHON

In scikit-learn, we mostly use:

1. joblib
2. pickle

Both do the same job:

* save Python objects to disk
* load them back later

---

## 5. WHICH ONE TO USE AND WHY

### pickle

* Python’s built-in tool
* works for many objects
* slower for large models

### joblib

* optimized for numpy and sklearn
* faster
* recommended for ML models

👉 In practice, **joblib is preferred**.

---

## 6. COMPLETE WORKING EXAMPLE (STEP BY STEP)

We will:

* train a model
* save it
* delete it mentally
* load it again
* predict using loaded model

---

### Step 1: Train a simple model
'''
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([3, 5, 7, 9, 11])

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "linear_model.pkl")

loaded_model = joblib.load("linear_model.pkl")

prediction = loaded_model.predict([[6]])
print(prediction)
print()
prediction = loaded_model.predict([[11]])
print(prediction)

'''
At this point:

* model has learned parameters
* but only exists in memory

---

### Step 2: Save the trained model using joblib

```python
import joblib

joblib.dump(model, "linear_model.pkl")
```

What this does internally:

* converts model object into bytes
* stores it in a file
* file now contains learned coefficients and intercept

---

### Step 3: Load the model later

```python
loaded_model = joblib.load("linear_model.pkl")
linear_model.pkl-->it is the file that was  created in the same model where trained data is available
```

What happens here:

* file is read
* model object is reconstructed
* learned parameters are restored

No training happens again.

---

### Step 4: Use the loaded model

```python
prediction = loaded_model.predict([[6]])
print(prediction)
```

This works **exactly** like the original model.

---

## 7. VERY IMPORTANT CLARITY (READ CAREFULLY)

When you load a model:

* you do NOT call fit again
* you directly call predict
* model behaves exactly as before

Saving and loading does NOT change the model.

---

## 8. WHERE THIS IS USED IN REAL LIFE (YOUR DRONE USE CASE)

Example workflow:

1. Train model on laptop
2. Save model file
3. Copy model file to drone system or server
4. Load model there
5. Use it to predict in real time

Training is done once.
Prediction happens many times.

---

## 9. COMMON MISTAKES (AVOID THESE)

* Retraining model after loading
* Forgetting to save preprocessing objects
* Saving model before training

Important rule:
👉 Always save **pipeline**, not just model

Example:

```
joblib.dump(pipeline, "full_pipeline.pkl")
```

This saves:

* scaler
* PCA
* model
  all together

---

## 10. ONE SENTENCE THAT MUST STICK

Saving and loading models allows you to reuse a trained machine learning model later without retraining it.

---




'''