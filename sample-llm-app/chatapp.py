import streamlit as st

prompt = st.chat_input("Type your message here: ", max_chars=100)
if prompt:
    st.write(f"You typed: {prompt}")

with st.chat_message("user"):
    st.markdown("Hello, how are you?")
    
with st.chat_message("assistant"):
    st.markdown("I'm good, thank you! How can I assist you today?")
    
