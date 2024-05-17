import streamlit as st
import google.generativeai as genai

st.title("sentimental analysis")
text = st.text_input('Enter some text')
api_key = "AIzaSyAiZ0vNeb36Y--vlWy9SPCVVsZKfASsQ8w"
genai.configure(api_key=api_key)
model=genai.GenerativeModel("gemini-pro")

if st.button("Response"):
    response=model.generate_content(text + "tell me this is positive or negative")
    st.write(text)
    st.write('Gemini :',response.text)