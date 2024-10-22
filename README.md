# Screenshot
![Screenshot 2024-10-22 212555](https://github.com/user-attachments/assets/be75be71-60cf-49dd-9c6e-d5b9821adfb1)


# sentiment-analysis-using-LSTM

This is a sentiment analysis application built using Python, Streamlit, and TensorFlow/Keras. The app allows users to input text and receive sentiment predictions, classifying the text as either positive or negative.

## Features

- **User-Friendly Interface**: A simple web interface for users to input text.
- **Real-Time Predictions**: Instant feedback on the sentiment of the input text.
- **Custom Preprocessing**: Text is preprocessed for optimal performance of the model.

## Technologies Used

- **Python**: The primary programming language used for developing the application.
- **Streamlit**: A library for building interactive web applications easily.
- **TensorFlow/Keras**: Used for building and training the sentiment analysis model.
- **NLTK**: Natural Language Toolkit for text processing, including the use of stopwords.

## Installation
1. Clone the repository:
   
   ```bash
   git clone <repository_url>
   cd <repository_name>
   
3. Create a virtual environment and activate it:
   ``` bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
5. Install the required packages:
   ```
   pip install -r requirements.txt
7. Download the necessary NLTK resources:
   ```bash 
   import nltk
   nltk.download('stopwords') 

# Usage  
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
2. Open your web browser and navigate to https://saurabh-sentimentanalysis.streamlit.app/ to use the application
3. Enter any text in the input area and click the "Predict Sentiment" button to see the sentiment analysis result.

# Model Details
The model was trained on a dataset and uses an LSTM architecture to predict sentiment.
The text input is preprocessed to remove stopwords and tokenize the text before prediction.

# Acknowledgements
NLTK for natural language processing.
Streamlit for creating the interactive web application.
TensorFlow and Keras for building the machine learning model.
  





   
        

 
   
