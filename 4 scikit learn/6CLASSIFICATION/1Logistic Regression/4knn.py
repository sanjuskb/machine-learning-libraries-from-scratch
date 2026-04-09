import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

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
    X, y, test_size=0.25, random_state=42
)

# Create KNN model
model = KNeighborsClassifier(n_neighbors=3)

# Train model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

print("X_test:")
print(X_test)
print()

print("Predicted class:", predictions)

'''
This is very important:

In KNN, fit does NOT learn parameters.

It only:
• stores X_train
• stores y_train

That’s it.

No equations.
No coefficients.
No training process.

------------------------------
data=
5-->0
20-->1
30-->1

majority=class 1
so predicted value is class 1


'''