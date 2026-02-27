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
 
