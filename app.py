import streamlit as st
import google.generativeai as genai

st.title("My App")


genai.configure(api_key="AIzaSyAvb8GtklDGxcSbIEobJg13Ugt5rE_HcTE")

text = st.text_input("Ask question")

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

if st.button("click me"):
    response = chat.send_message(text)
    st.write(response.text)  