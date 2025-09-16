import streamlit as st
from sidebar import Sidebar


Sidebar().render()

if st.file_uploader("upload docs",accept_multiple_files=True):
    print("ok")
st.write(st.selectbox("mode",["Graph RAG","Naive RAG"]))


