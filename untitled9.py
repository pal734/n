import streamlit as st
 
st.title("Sentiment analysis ")
st.text_input("Enter your text")
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
