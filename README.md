**Product Review Sentiment Analysis using NLP**

**Project Overview**
  * This project builds a Natural Language Processing (NLP) based Machine Learning model to classify product reviews as Positive or Negative.
  * The model uses TF-IDF vectorization and multiple classification algorithms to analyze and predict sentiment from customer reviews.

**Technologies Used**
Python

Pandas

NumPy

NLTK

Scikit-learn

Matplotlib

Seaborn

Joblib

**NLP & ML Workflow**
1. Data Cleaning & Preprocessing
2. Text Normalization (Lowercase, Remove Special Characters)
3. Stopword Removal
4. Sentiment Label Creation from Ratings
5. TF-IDF Feature Extraction
6. Train-Test Split
7. Model Training:
8. Logistic Regression
9. Naive Bayes
10. Random Forest
11. Model Comparison
12. Model Serialization (Saving Model & Vectorizer)
13. Prediction Function Implementation

**Project Structure**
product-review-sentiment-analysis-nlp/
│
├── data/
│   └── reviews.csv
│
├── notebooks/
│   └── sentiment_analysis.ipynb
│
├── models/
│   ├── sentiment_model.pkl
│   └── vectorizer.pkl
│
├── requirements.txt
└── README.md

**Model Performance**

-> Logistic Regression Accuracy: ~87%
-> Naive Bayes Accuracy: ~83.7%
-> Random Forest Accuracy: ~83.5%
(Best performing model selected and saved for prediction.)

**Key Learning Outcomes**

1. Text preprocessing techniques in NLP

2. TF-IDF vectorization for text representation

3. Comparison of multiple ML classification models

4. Model evaluation using accuracy, confusion matrix & classification report

5. Saving trained models for deployment

6. Building structured NLP project for GitHub portfolio

**How to Run the Project**
1️⃣ Clone the repository
git clone <your-repo-link>
cd product-review-sentiment-analysis-nlp
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run Jupyter Notebook
jupyter notebook

Open sentiment_analysis.ipynb and run all cells.

**Future Improvements**

Hyperparameter tuning

Add Neutral sentiment classification

Deploy using Streamlit

Use advanced models like LSTM or Transformer
