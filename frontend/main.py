import streamlit as st

with st.sidebar.expander("Settings",expanded=False):
    st.text_input("API Key",type="password")
    if st.button("OK",type="primary"):
        print("ok")

if st.file_uploader("upload docs",accept_multiple_files=True):
    print("ok")
st.write(st.selectbox("mode",["Graph RAG","Naive RAG"]))


