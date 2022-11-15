import streamlit as st
import  pandas as pd
from database import create_table_inspector
from database import add_data_inspector
# from database import checker


def create_inspector():

    col1,col2=st.columns(2)
    with col1:
        id=st.text_input("Enter inspector id")
        # iname=st.text("Enter inspector name")
    with col2:
        iname = st.text_input("Enter inspector name")
        passwd=st.text_input("Enter password")\


    if st.button("Add inspector"):

        create_table_inspector()
        add_data_inspector(id,iname,passwd)
        st.success("Created inspector")