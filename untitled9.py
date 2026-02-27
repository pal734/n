import streamlit as st
import google.generativeai as genai
st.title("Sentiment analysis ")
st.text_input("Enter your text")
 GOOGLE_API_KEY = os.environ.get("OPENAI_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
if 'sentiment' not in st.session_state:
  st.session_state.sentiment ={
      'positive': 'Positive',
      'negative': 'Negative',
      'neutral': 'Neutral'
  }
  def get_gemini_response(input_prompt, image_data=None):
  model = genai.GenerativeModel('gemini-2.5-flash')
  content = [input_prompt]
  if image_data:
    content.extend(image_data)

  try:
    response = model.generate_content(content)
    return response.text
  except Exception as e:
    return f"Error: {str(e)}"

def input_image_setup(uploaded_file):
  if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    image_parts = [
        {
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }
    ]
    return image_parts
  return None  
