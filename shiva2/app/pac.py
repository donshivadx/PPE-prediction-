# pac.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.model_selection import train_test_split
import random

# Load your Protection Suit Industry Dataset
# Replace 'your_dataset.csv' with the actual file path or URL of your dataset
df = pd.read_csv("../protection_suits_dataset.csv")

# Fill missing labels with a random choice
df['Requirement'].fillna(df['Requirement'].sample().values[0], inplace=True)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['Description'], df['Requirement'], test_size=0.2, random_state=42)

# Convert text data to numerical features using TF-IDF vectorization
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
tfidf_X_train = tfidf_vectorizer.fit_transform(X_train)
tfidf_X_test = tfidf_vectorizer.transform(X_test)

# Initialize Passive Aggressive Classifier
pac_classifier = PassiveAggressiveClassifier(max_iter=50)
pac_classifier.fit(tfidf_X_train, y_train)

# Function to get PAC prediction
def get_pac_prediction(order, suit_type, customization):
    # Vectorize the user input using the same TF-IDF vectorizer
    user_input_description = f"{order} {suit_type} with {customization}"
    tfidf_user_input = tfidf_vectorizer.transform([user_input_description])

    # Predict the well-suited requirement
    prediction = pac_classifier.predict(tfidf_user_input)

    return prediction[0]
