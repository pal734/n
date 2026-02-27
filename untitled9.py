import streamlit as st
 
st.title("Sentiment analysis ")
st.text_input("Enter your text")
 
import streamlit as st
from textblob import TextBlob
import nltk

# Create a function to download needed data, cached for speed
@st.cache_resource
def download_nltk_data():
    nltk.download('punkt')
    nltk.download('brown')
    nltk.download('wordnet')

download_nltk_data()

# Your Streamlit app code
text = st.text_area("Enter text")
if st.button("Analyze"):
    blob = TextBlob(text)
    st.write(blob.sentiment)
from textblob import TextBlob

# The text you want to analyze
text = st.text_input("Enter your text")

# Create a TextBlob object
# Using the 'text' variable which is already defined in this cell
analysis = TextBlob(text)

# Access the sentiment property
# The sentiment property returns a named tuple of the form Sentiment(polarity, subjectivity)
polarity = analysis.sentiment.polarity
subjectivity = analysis.sentiment.subjectivity

# Print the results
print(f"Original Text: {text}")
print(f"Polarity: {polarity}")
print(f"Subjectivity: {subjectivity}")

# Classify the sentiment based on polarity
if polarity > 0:
    print("Sentiment: Positive 😊")
elif polarity < 0:
    print("Sentiment: Negative 😡")
else:
    print("Sentiment: Neutral 😐")

