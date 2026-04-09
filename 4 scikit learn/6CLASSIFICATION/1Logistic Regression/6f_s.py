from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
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

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Create scaler
scaler = StandardScaler()

# Fit on training data and transform
X_train_scaled = scaler.fit_transform(X_train)

# Transform test data
X_test_scaled = scaler.transform(X_test)

# KNN model
model = KNeighborsClassifier(n_neighbors=3)

# Fit model
model.fit(X_train_scaled, y_train)

# Predict
predictions = model.predict(X_test_scaled)

print("Predictions:", predictions)
'''
11. WHAT IS HAPPENING INTERNALLY (STEP BY STEP)

scaler.fit learns mean and std from training data

scaler.transform rescales values

KNN stores scaled training data

For test data, scaled values are used

Distance is computed fairly

Nearest neighbors are correct

Voting gives reliable output

12. VERY IMPORTANT RULE (MEMORIZE THIS)

If an algorithm uses distance:

KNN

KMeans

PCA

Then feature scaling is mandatory.

If an algorithm uses trees:

Decision Tree

Random Forest

Scaling is NOT required.

ONE-LINE FINAL SUMMARY

KNN depends on distance, and feature scaling is required to prevent large-valued features from dominating distance calculations.

'''