import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load the dataset
df = pd.read_csv("StudentsPerformance.csv")

# Convert "test preparation course" to binary feature
df["test_prep_done"] = df["test preparation course"].apply(lambda x: 1 if x == "completed" else 0)

# Create target variable (average score of math, reading, writing)
df["avg_score"] = df[["math score", "reading score", "writing score"]].mean(axis=1)

# Select features
X = df[["reading score", "writing score", "test_prep_done"]]
y = df["avg_score"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save the model to a file
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as 'model.pkl'")
