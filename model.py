import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
data = pd.read_csv("../data/dataset.csv")

# Features & labels
X = data["text"]
y = data["emotion"]

# Vectorization
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Model
model = LogisticRegression()
model.fit(X_vec, y)

def predict_emotion(text):
    text_vec = vectorizer.transform([text])
    return model.predict(text_vec)[0]