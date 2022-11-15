import streamlit as st
from database import create_table_license

def create_license():
    col1,col2=st.columns(2)
    with col1:
        lid=st.text_input
