import pickle
import time

import matplotlib.pyplot as plt
import nltk
import pandas as pd
import streamlit as st
from nltk.stem import PorterStemmer
from wordcloud import WordCloud

# Download the NLTK data for stemming (if not already downloaded)
nltk.download('punkt')

# Load the model
model = pickle.load(open('twitter_sentiment.pkl', 'rb'))

st.title("Twitter Sentiment Analysis")

tweet = st.text_area("Enter your tweet(s) or upload a file", height=200)

# Function to perform stemming
def perform_stemming(text):
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in nltk.word_tokenize(text)]
    return ' '.join(stemmed_words)

# Function to analyze sentiment
def analyze_sentiment(tweet):
    tweet = perform_stemming(tweet)  # Stem the input tweet
    start = time.time()
    prediction = model.predict([tweet])
    end = time.time()
    prediction_time = round(end - start, 2)
    return prediction[0], prediction_time

if st.button('Predict'):
    sentiment, prediction_time = analyze_sentiment(tweet)
    st.write('Prediction time taken: ', prediction_time, 'seconds')
    st.write("Predicted Sentiment is: ", sentiment)

    # Sentiment Distribution
    sentiments = ['Positive', 'Neutral', 'Negative']
    sentiment_counts = {
        'Positive': 0,
        'Neutral': 0,
        'Negative': 0
    }
    sentiment_counts[sentiment] += 1

    st.subheader('Sentiment Distribution')
    fig, ax = plt.subplots()
    ax.bar(sentiments, [sentiment_counts[sent] for sent in sentiments])
    st.pyplot(fig)

    # Word Cloud
    st.subheader('Word Cloud')
    wordcloud = WordCloud().generate(tweet)
    st.image(wordcloud.to_array(), width=600)  # Adjust the width as needed


# Historical Sentiment Analysis
if st.checkbox("Historical Sentiment Analysis"):
    uploaded_file = st.file_uploader("Upload a file of tweets")
    if uploaded_file is not None:
        tweets = uploaded_file.read().decode('utf-8')
        tweets = tweets.splitlines()
        sentiments = []

        for tweet in tweets:
            sentiment, _ = analyze_sentiment(tweet)
            sentiments.append(sentiment)

        sentiment_df = pd.DataFrame(sentiments, columns=['Sentiment'])
        st.subheader('Historical Sentiment Analysis')
        st.write(sentiment_df)

        st.subheader('Sentiment Distribution in Historical Data')
        sentiment_distribution = sentiment_df['Sentiment'].value_counts()
        st.bar_chart(sentiment_distribution)
