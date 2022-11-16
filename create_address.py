import streamlit as st
from database import create_table_address
from database import add_data_address

def create_address():
    col1,col2=st.columns(2)
    with col1:
        aadhar=st.text_input("Enter aadhar details")
    with col2:
        street=st.text_input("Enter street details quick")
        city=st.text_input("Enter city")
        state_code=st.text_input("Enter state code quick")
    if st.button("add address "):
        create_table_address()
        add_data_address(aadhar,street,city,state_code)
        st.success("address successfully added")

