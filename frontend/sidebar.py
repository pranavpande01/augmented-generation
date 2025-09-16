# sidebar.py
import streamlit as st

class Sidebar:
    def __init__(self):
        self.api_key = ""
        self.items = []

    def render(self):
        st.sidebar.title("Console")
        with st.sidebar:
            st.write("Files Uploaded:")
            

            if st.file_uploader("Add Items",accept_multiple_files=True):
                print("ok")


            if st.button("New Session", key="new_session_btn"):
                st.balloons()

        with st.sidebar.expander("Settings", expanded=False):
            self.api_key = st.text_input("API Key", type="password", key="api_key_input")
            if st.button("OK", key="ok_btn"):
                print("OK clicked. API Key:", self.api_key)

        with st.sidebar.expander("Advanced Settings", expanded=False):
            a=st.radio("Mode", ["Graph RAG", "Naive RAG","Graph+Naive RAG"], key="mode_radio")
            creativity= st.slider("creativity",0.0,1.0,0.7,key="creativity_slider")
            st.number_input("Top K",min_value=1,step=1,key="topk_input")
            b=st.number_input("Chunk Size",min_value=1,step=1,value=500,key="maxtokens_input",disabled=True if a=="Graph RAG" else False)
            st.number_input("Overlap",min_value=1,max_value=b,step=1,key="overlap_input",disabled=True if a=="Graph RAG" else False)

    def add_item(self):
        if "sidebar_items" not in st.session_state:
            st.session_state.sidebar_items = []
        st.session_state.sidebar_items.append(f"Item {len(st.session_state.sidebar_items) + 1}")
        st.experimental_rerun() 
    def new_session(self):
        st.session_state.sidebar_items = []
        st.experimental_rerun()
