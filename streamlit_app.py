import streamlit as st
import main
from streamlit import logger

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import sqlite3

app_logger = logger.get_logger("SMI_APP")
app_logger.info(f"SQLite version : {sqlite3.sqlite_version}")

st.title("About me -AI-Powered Personal Assistant")
st.text("This assistant helps to provide information about my profession experience, technical skills etc. ")

user_query = st.text_input("Ask question: ", max_chars=50)

btn = st.button("Find Answer")

if btn:
    placeholder = st.empty()
    placeholder.write("I am getting the answer...")

    response = main.get_answer(user_query, app_logger)

    placeholder.empty()
    st.write(response)