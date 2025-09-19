import streamlit as st

class Panel():
    def __init__(self):
        self.api_key = ""
        self.items = [1,2,34]

    def render(self):
        st.chat_input("type here...")
        with st.chat_message("user",avatar="user"):
            st.markdown("Hello")