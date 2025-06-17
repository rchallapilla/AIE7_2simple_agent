import streamlit as st
from agent import ask_agent

st.title("Ask Me Anything")
question = st.text_input("Your question")
if question:
    answer = ask_agent(question)
    st.write("Answer:", answer) 