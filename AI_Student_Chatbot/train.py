import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
data = pd.read_csv("dataset.csv")

# Input and output
X = data["Question"]
y = data["Intent"]

# Convert text into numbers
vectorizer = TfidfVectorizer()

X_vector = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()

model.fit(X_vector, y)

# Save model
joblib.dump(model, "model.pkl")

# Save vectorizer
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained successfully!")