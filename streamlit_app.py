import streamlit as st
import main

st.title("About me -AI-Powered Personal Assistant")
st.text("This assistant helps to provide information about my profession experience, technical skills etc. ")

user_query = st.text_input("Ask question: ", max_chars=50)

btn = st.button("Find Answer")

if btn:
    placeholder = st.empty()
    placeholder.write("I am getting the answer...")

    response = main.get_answer(user_query)

    placeholder.empty()
    st.write(response)