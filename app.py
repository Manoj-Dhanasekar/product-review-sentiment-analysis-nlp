import streamlit as st
import joblib
import re
from nltk.corpus import stopwords
import nltk

# Download stopwords (first time only)
nltk.download('stopwords')

# Load model and vectorizer
model = joblib.load("models/sentiment_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

stop_words = set(stopwords.words('english'))

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

# Streamlit UI
st.title("📝 Product Review Sentiment Analysis")
st.write("Enter a product review to predict sentiment.")

user_input = st.text_area("Enter Review Here:")

if st.button("Predict Sentiment"):
    if user_input:
        cleaned = clean_text(user_input)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)

        if prediction[0] == "positive":
            st.success("😊 Positive Review")
        else:
            st.error("😞 Negative Review")
    else:
        st.warning("Please enter a review.")