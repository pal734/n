import streamlit as st
 
st.title("Sentiment analysis ")
st.text_input("Enter your text")
 
import streamlit as st
from textblob import TextBlob
import emoji

def main():
    """Sentiment Analysis App with TextBlob"""

    st.title("Sentiment Analysis App")
    st.write(emoji.emojize('Analyze the sentiment of your text :smile:'))

    # Text input area for user
    raw_text = st.text_area("Enter Your Text Here", "Type something to analyze...")

    # Button to trigger analysis
    if st.button("Analyze Sentiment"):
        if raw_text:
            # Perform sentiment analysis using TextBlob
            blob = TextBlob(raw_text)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity

            # Determine overall sentiment and corresponding emoji
            if polarity > 0.0:
                sentiment_label = "Positive"
                custom_emoji = ':smile:'
                color = 'green'
            elif polarity < 0.0:
                sentiment_label = "Negative"
                custom_emoji = ':disappointed:'
                color = 'red'
            else:
                sentiment_label = "Neutral"
                custom_emoji = ':expressionless:'
                color = 'blue'

            # Display results
            st.subheader("Analysis Results:")
            st.markdown(f"**Overall Sentiment:** :{color}[{sentiment_label}] {emoji.emojize(custom_emoji)}")
            st.info(f"Polarity Score (range -1.0 to 1.0): **{polarity:.4f}**")
            st.info(f"Subjectivity Score (range 0.0 to 1.0): **{subjectivity:.4f}**")
            
            st.subheader("Sentiment Explanation:")
            st.write(
                "*   **Polarity:** A value between -1.0 (very negative) and 1.0 (very positive).\n"
                "*   **Subjectivity:** A value from 0.0 (very objective) to 1.0 (very subjective), indicating opinionated content."
            )

        else:
            st.warning("Please enter some text for analysis.")

if __name__ == '__main__':
    main()

