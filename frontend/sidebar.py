# sidebar.py
import streamlit as st

class Sidebar:
    def __init__(self):
        self.api_key = ""
        self.items = []

    def render(self):
        with st.sidebar:
            st.write("Files Uploaded:")

            if st.button("➕ Add item", key="add_item_btn"):
                pass

            if st.button("New Session", key="new_session_btn"):
                pass

        with st.sidebar.expander("Settings", expanded=False):
            self.api_key = st.text_input("API Key", type="password", key="api_key_input")
            if st.button("OK", key="ok_btn"):
                print("OK clicked. API Key:", self.api_key)

        with st.sidebar.expander("Advanced Settings", expanded=False):
            st.text("yeah")
            st.radio("Mode", ["Graph RAG", "Naive RAG"], key="mode_radio")
    def add_item(self):
        if "sidebar_items" not in st.session_state:
            st.session_state.sidebar_items = []
        st.session_state.sidebar_items.append(f"Item {len(st.session_state.sidebar_items) + 1}")
        st.experimental_rerun() 
    def new_session(self):
        st.session_state.sidebar_items = []
        st.experimental_rerun()
