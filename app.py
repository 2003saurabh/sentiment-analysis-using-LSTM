import streamlit as st
import dill
import nltk
from nltk.corpus import stopwords
import re
from tensorflow.keras.preprocessing.sequence import pad_sequences

nltk.download('stopwords')
with open('model.pkl','rb') as m:
    model=dill.load(m)

with open('token.pkl','rb') as tok:
    token=dill.load(tok)

with open('preprocess.pkl','rb') as p:
    preprocessing=dill.load(p)

    st.title("Sentiment Analysis")
    st.write("Enter a movie review to analyze its sentiment (positive or negative):")

    # Text input for the user to enter a review
    user_review = st.text_area("Review", "")

    # Button to submit the review
    if st.button("predict sentiment"):
        if user_review:
            # Preprocess the review
            tokenized_review = preprocessing(user_review)

            # Make prediction
            prediction_prob = model.predict(tokenized_review)
            prediction = (prediction_prob > 0.5).astype(int)

            # Display the result
            sentiment = "Positive" if prediction[0][0] == 1 else "Negative"
            st.success(f"The sentiment of the review is: **{sentiment}**")
        else:
            st.warning("Please enter a review to analyze.")